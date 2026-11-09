<?php
declare(strict_types=1);

// Deployment settings belong in the server environment, never in public HTML.
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');
session_set_cookie_params([
    'httponly' => true,
    'secure' => isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off',
    'samesite' => 'Lax',
]);
session_start();

function respond(int $status, array $data): never {
    http_response_code($status);
    echo json_encode($data, JSON_UNESCAPED_SLASHES);
    exit;
}
function field(string $key, int $maximum): string {
    $value = $_POST[$key] ?? '';
    if (!is_string($value) || strlen($value) > $maximum) {
        respond(422, ['ok' => false, 'message' => 'An enquiry field is invalid or too long.']);
    }
    return trim($value);
}
$recipient = (string) getenv('ORBIT_CONTACT_TO');
$sender = (string) getenv('ORBIT_MAIL_FROM');
$ready = getenv('ORBIT_MAIL_ENABLED') === '1'
    && filter_var($recipient, FILTER_VALIDATE_EMAIL)
    && filter_var($sender, FILTER_VALIDATE_EMAIL)
    && str_ends_with(strtolower($sender), '@orbitits.com');
$method = $_SERVER['REQUEST_METHOD'] ?? 'GET';
if ($method === 'GET' && ($_GET['action'] ?? '') === 'token') {
    $_SESSION['orbit_token'] ??= bin2hex(random_bytes(32));
    respond(200, ['ready' => (bool) $ready, 'token' => $_SESSION['orbit_token']]);
}
if ($method !== 'POST') {
    header('Allow: GET, POST');
    respond(405, ['ok' => false, 'message' => 'Use the website enquiry form.']);
}
if ((int) ($_SERVER['CONTENT_LENGTH'] ?? 0) > 20000) {
    respond(413, ['ok' => false, 'message' => 'The enquiry is too large.']);
}
$csrf = field('csrf', 128);
if (!isset($_SESSION['orbit_token']) || !hash_equals($_SESSION['orbit_token'], $csrf)) {
    respond(403, ['ok' => false, 'message' => 'Please refresh the page and try again.']);
}
$name = field('name', 100);
$company = field('company', 150);
$email = field('email', 200);
$service = field('service', 200);
$package = field('package', 100);
$message = field('message', 5000);
if (field('website', 200) !== '') {
    respond(422, ['ok' => false, 'message' => 'The enquiry could not be accepted.']);
}
if ($name === '' || strlen($message) < 10 || !filter_var($email, FILTER_VALIDATE_EMAIL)
    || preg_match('/[\r\n]/', $email) || field('privacy', 5) !== '1') {
    respond(422, ['ok' => false, 'message' => 'Provide your name, a valid email, project details and privacy acknowledgement.']);
}
if (!$ready) {
    respond(503, ['ok' => false, 'message' => 'Server enquiry delivery is not enabled. Please call or prepare an email instead. Nothing has been sent.']);
}
if (time() - (int) ($_SESSION['orbit_last_sent'] ?? 0) < 60) {
    respond(429, ['ok' => false, 'message' => 'Please wait a minute before sending another enquiry.']);
}
$text = "OrbitIT project enquiry\n\nName: $name\nCompany: $company\nEmail: $email\nService: $service\nPackage reference: $package\n\n$message";
$headers = ['From' => $sender, 'Reply-To' => $email, 'Content-Type' => 'text/plain; charset=UTF-8'];
if (!@mail($recipient, 'OrbitIT website enquiry', $text, $headers)) {
    respond(503, ['ok' => false, 'message' => 'The mail transport did not accept your enquiry. Please call or prepare an email instead.']);
}
$_SESSION['orbit_last_sent'] = time();
respond(200, ['ok' => true]);
