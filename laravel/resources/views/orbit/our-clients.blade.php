@extends('orbit.layouts.app')
@section('title', 'Our clients | OrbitIT Solution Limited')
@section('description', 'OrbitIT client listing.')
@section('content')
<section class="page-intro"><div class="container"><div class="breadcrumbs"><a href="{{ route('orbit.home') }}">Home</a><span>/</span>Our clients</div><p class="eyebrow">CONNECTIONS</p><h1>Our clients</h1><p class="intro-text"></p></div><div class="intro-orbit" aria-hidden="true"></div></section><section class="section clients-section"><div class="container"><div class="clients-grid" aria-label="Client listing"></div></div></section>
@endsection
@section('canonical', 'our-clients.html')
