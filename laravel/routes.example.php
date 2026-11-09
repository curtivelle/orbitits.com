<?php
use Illuminate\Support\Facades\Route;

Route::view('/', 'orbit.index')->name('orbit.home');
Route::view('/services', 'orbit.services')->name('orbit.services');
Route::view('/web-development', 'orbit.web-development')->name('orbit.web-development');
Route::view('/seo-services', 'orbit.seo-services')->name('orbit.seo-services');
Route::view('/digital-marketing', 'orbit.digital-marketing')->name('orbit.digital-marketing');
Route::view('/aeo-geo-services', 'orbit.aeo-geo-services')->name('orbit.aeo-geo-services');
Route::view('/ui-ux-design', 'orbit.ui-ux-design')->name('orbit.ui-ux-design');
Route::view('/domain-hosting', 'orbit.domain-hosting')->name('orbit.domain-hosting');
Route::view('/e-commerce-solutions', 'orbit.e-commerce-solutions')->name('orbit.e-commerce-solutions');
Route::view('/it-consultancy', 'orbit.it-consultancy')->name('orbit.it-consultancy');
Route::view('/mobile-app-development', 'orbit.mobile-app-development')->name('orbit.mobile-app-development');
Route::view('/graphics-design', 'orbit.graphics-design')->name('orbit.graphics-design');
Route::view('/video-editing-production', 'orbit.video-editing-production')->name('orbit.video-editing-production');
Route::view('/social-media-management', 'orbit.social-media-management')->name('orbit.social-media-management');
Route::view('/pricing', 'orbit.pricing')->name('orbit.pricing');
Route::view('/about', 'orbit.about')->name('orbit.about');
Route::view('/team', 'orbit.team')->name('orbit.team');
Route::view('/our-clients', 'orbit.our-clients')->name('orbit.our-clients');
Route::view('/portfolio', 'orbit.portfolio')->name('orbit.portfolio');
Route::view('/blog', 'orbit.blog')->name('orbit.blog');
Route::view('/planning-a-business-website', 'orbit.planning-a-business-website')->name('orbit.planning-a-business-website');
Route::view('/choosing-a-service-package', 'orbit.choosing-a-service-package')->name('orbit.choosing-a-service-package');
Route::view('/content-that-answers-questions', 'orbit.content-that-answers-questions')->name('orbit.content-that-answers-questions');
Route::view('/faq', 'orbit.faq')->name('orbit.faq');
Route::view('/contact', 'orbit.contact')->name('orbit.contact');
Route::view('/privacy', 'orbit.privacy')->name('orbit.privacy');
Route::view('/terms', 'orbit.terms')->name('orbit.terms');
Route::view('/service-policy', 'orbit.service-policy')->name('orbit.service-policy');
Route::view('/cookies', 'orbit.cookies')->name('orbit.cookies');

Route::match(['get', 'post'], '/enquiry', [\App\Http\Controllers\OrbitEnquiryController::class, '__invoke'])->middleware('throttle:5,1')->name('orbit.enquiry');
