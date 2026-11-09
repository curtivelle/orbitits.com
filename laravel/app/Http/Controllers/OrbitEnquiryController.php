<?php
namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Mail;
use Throwable;

class OrbitEnquiryController extends Controller
{
    public function __invoke(Request $request)
    {
        $recipient = config('services.orbit_enquiries.to');
        $ready = (bool) config('services.orbit_enquiries.enabled', false)
            && !in_array(config('mail.default'), ['log', 'array'], true)
            && filter_var($recipient, FILTER_VALIDATE_EMAIL)
            && filter_var(config('mail.from.address'), FILTER_VALIDATE_EMAIL);
        if ($request->isMethod('get')) {
            return response()->json(['ready' => (bool) $ready, 'token' => csrf_token()])->header('Cache-Control', 'no-store');
        }
        $data = $request->validate([
            'name' => 'required|string|max:100', 'company' => 'nullable|string|max:150',
            'email' => 'required|email|max:200', 'service' => 'required|string|max:200',
            'package' => 'required|string|max:100', 'message' => 'required|string|min:10|max:5000',
            'privacy' => 'accepted', 'website' => 'nullable|string|max:0',
        ]);
        if (trim($data['name']) === '' || strlen(trim($data['message'])) < 10) {
            return response()->json(['ok' => false, 'message' => 'Provide a name and meaningful project details.'], 422);
        }
        if (!$ready) {
            return response()->json(['ok' => false, 'message' => 'Server enquiry delivery is not enabled. Please call or prepare an email.'], 503);
        }
        $body = 'OrbitIT enquiry' . "\n\n";
        foreach (['name', 'company', 'email', 'service', 'package', 'message'] as $key) {
            $body .= ucfirst($key) . ': ' . ($data[$key] ?? '') . "\n";
        }
        try {
            Mail::raw($body, function ($mail) use ($recipient, $data) {
                $mail->to($recipient)->replyTo($data['email'])->subject('OrbitIT website enquiry');
            });
        } catch (Throwable $error) {
            return response()->json(['ok' => false, 'message' => 'Delivery could not be confirmed. Please call or prepare an email.'], 503);
        }
        return response()->json(['ok' => true]);
    }
}
