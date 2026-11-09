<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>@yield('title')</title><meta name="description" content="@yield('description')"><meta name="theme-color" content="#102e52"><meta name="robots" content="index, follow"><link rel="canonical" href="{{ url()->current() }}">
<link rel="icon" href="{{ asset('assets/orbit/images/favicon.svg') }}" type="image/svg+xml">
<link rel="stylesheet" href="{{ asset('assets/orbit/vendor/bootstrap/bootstrap.min.css') }}"><link rel="stylesheet" href="{{ asset('assets/orbit/css/orbit.css') }}">
</head><body id="top">
@include('orbit.partials.header')
<main id="main">@yield('content')</main>
@include('orbit.partials.footer')
<script src="{{ asset('assets/orbit/vendor/bootstrap/bootstrap.bundle.min.js') }}"></script><script src="{{ asset('assets/orbit/js/orbit.js') }}"></script></body></html>
