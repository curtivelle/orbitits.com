<?php
// Merge this entry into the array returned by config/services.php.
return [
    'orbit_enquiries' => [
        'enabled' => env('ORBIT_MAIL_ENABLED', false),
        'to' => env('ORBIT_CONTACT_TO'),
    ],
];
