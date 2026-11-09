@extends('orbit.layouts.app')
@section('title', 'Page not found | OrbitIT Solution Limited')
@section('description', 'The requested page could not be found.')
@section('content')
<section class="page-intro"><div class="container"><div class="breadcrumbs"><a href="{{ route('orbit.home') }}">Home</a><span>/</span>Page not found</div><p class="eyebrow">404 / PAGE NOT FOUND</p><h1>This page is<br>out of orbit.</h1><p class="intro-text">The page may have moved. Use the navigation to find your next step.</p></div><div class="intro-orbit" aria-hidden="true"></div></section><section class="section"><div class="container"><a class="btn btn-ink" href="{{ route('orbit.home') }}">Back to home ↗</a> <a class="btn btn-outline" href="{{ route('orbit.services') }}">Explore services</a></div></section>
@endsection
@section('canonical', '404.html')
