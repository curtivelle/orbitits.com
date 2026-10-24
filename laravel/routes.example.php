<?php
// Add these routes to your Laravel routes/web.php (adjust paths if needed).
use Illuminate\Support\Facades\Route;

Route::view('/', 'orbit.index')->name('orbit.home');
Route::view('/services', 'orbit.services')->name('orbit.services');
Route::view('/about', 'orbit.about')->name('orbit.about');
Route::view('/contact', 'orbit.contact')->name('orbit.contact');
