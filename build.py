"""Build static pages and equivalent Laravel Blade views. Python standard library only."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
PAGES = {
    'index': ('OrbitIT Solution Limited | Software & IT Solutions', 'Software development, IT consultancy, technology services and technical testing from OrbitIT Solution Limited in Milton Keynes.'),
    'services': ('Our Services | OrbitIT Solution Limited', 'Explore software development, IT consultancy, technology services and technical testing with OrbitIT Solution Limited.'),
    'about': ('About Us | OrbitIT Solution Limited', 'Learn about OrbitIT Solution Limited, a technology company registered in England and Wales, company number 17341168.'),
    'contact': ('Contact | OrbitIT Solution Limited', 'Discuss your technology project with OrbitIT Solution Limited. Call +44 7459 506031 or prepare a project brief.'),
}

HEAD = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{description}"><meta name="theme-color" content="#102e52">
<link rel="icon" href="assets/images/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/vendor/bootstrap/bootstrap.min.css"><link rel="stylesheet" href="assets/css/style.css">
</head><body id="top">'''
SCRIPTS = '<script src="assets/vendor/bootstrap/bootstrap.bundle.min.js"></script><script src="assets/js/main.js"></script></body></html>\n'

def blade(text):
    text = re.sub(r'(href|src)="(assets/[^\"]+)"', lambda m: m[1] + '="{{ asset(\'assets/orbit/' + m[2][7:] + '\') }}"', text)
    for page in PAGES:
        text = text.replace(page + '.html', "{{ route('orbit." + ('home' if page == 'index' else page) + "') }}")
    return text

views = ROOT / 'laravel/resources/views/orbit'
(views / 'partials').mkdir(parents=True, exist_ok=True)
(views / 'layouts').mkdir(exist_ok=True)
header = (ROOT / 'src/partials/header.html').read_text(encoding='utf-8')
footer = (ROOT / 'src/partials/footer.html').read_text(encoding='utf-8')
for page, (title, description) in PAGES.items():
    content = (ROOT / f'src/pages/{page}.html').read_text(encoding='utf-8')
    active_header = header.replace(f'data-page="{page}"', f'data-page="{page}" aria-current="page"').replace(f'class="nav-link" data-page="{page}"', f'class="nav-link active" data-page="{page}"')
    html = HEAD.format(title=title, description=description) + '\n' + active_header + '\n<main id="main">' + content + '</main>\n' + footer + SCRIPTS
    (ROOT / f'{page}.html').write_text(html, encoding='utf-8')
    (views / f'{page}.blade.php').write_text("@extends('orbit.layouts.app')\n@section('title', '" + title + "')\n@section('description', '" + description + "')\n@section('content')\n" + blade(content) + "\n@endsection\n", encoding='utf-8')
blade_header = blade(header)
for page in PAGES:
    route = 'home' if page == 'index' else page
    blade_header = blade_header.replace(f'class="nav-link" data-page="{page}"', "class=\"nav-link {{ request()->routeIs('orbit." + route + "') ? 'active' : '' }}\" data-page=\"" + page + "\" {{ request()->routeIs('orbit." + route + "') ? 'aria-current=page' : '' }}")
(views / 'partials/header.blade.php').write_text(blade_header, encoding='utf-8')
(views / 'partials/footer.blade.php').write_text(blade(footer), encoding='utf-8')
layout = blade(HEAD.replace('{title}', "@yield('title')").replace('{description}', "@yield('description')")) + "\n@include('orbit.partials.header')\n<main id=\"main\">@yield('content')</main>\n@include('orbit.partials.footer')\n" + blade(SCRIPTS)
(views / 'layouts/app.blade.php').write_text(layout, encoding='utf-8')
print('Built 4 static HTML pages and Laravel Blade views.')
