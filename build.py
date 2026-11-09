"""Build static pages and equivalent Laravel Blade views. Python standard library only."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
import sys
from html import escape, unescape
sys.path.insert(0, str(ROOT / 'src'))
from site_content import generate
from graphics import generate_graphics
BASE_PATH = '/' if '--production' in sys.argv else '/orbitits.com/'
PAGES = generate(ROOT)
generate_graphics(ROOT)


HEAD = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{description}"><meta name="theme-color" content="#102e52"><meta name="robots" content="index, follow"><link rel="canonical" href="https://orbitits.com/{canonical}">
<link rel="icon" href="assets/images/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/vendor/bootstrap/bootstrap.min.css"><link rel="stylesheet" href="assets/css/orbit.css">
</head><body id="top">'''
SCRIPTS = '<script src="assets/vendor/bootstrap/bootstrap.bundle.min.js"></script><script src="assets/js/orbit.js"></script></body></html>\n'

def blade(text):
    text = re.sub(r'(href|src)="(assets/[^\"]+)"', lambda m: m[1] + '="{{ asset(\'assets/orbit/' + m[2][7:] + '\') }}"', text)
    for page in PAGES:
        text = text.replace(page + '.html', "{{ route('orbit." + ('home' if page == 'index' else page) + "') }}")
    text = text.replace('action="contact.php"', 'action="{{ route(\'orbit.enquiry\') }}" data-endpoint="{{ route(\'orbit.enquiry\') }}"')
    return text

views = ROOT / 'laravel/resources/views/orbit'
(views / 'partials').mkdir(parents=True, exist_ok=True)
(views / 'layouts').mkdir(exist_ok=True)
header = (ROOT / 'src/partials/header.html').read_text(encoding='utf-8')
footer = (ROOT / 'src/partials/footer.html').read_text(encoding='utf-8')
for page, (title, description) in PAGES.items():
    content = (ROOT / f'src/pages/{page}.html').read_text(encoding='utf-8')
    active_header = header.replace(f'data-page="{page}"', f'data-page="{page}" aria-current="page"').replace(f'class="nav-link" data-page="{page}"', f'class="nav-link active" data-page="{page}"')
    html = HEAD.format(title=escape(unescape(title)), description=escape(description), canonical='' if page == 'index' else page+'.html') + '\n' + active_header + '\n<main id="main">' + content + '</main>\n' + footer + SCRIPTS
    (ROOT / f'{page}.html').write_text(html, encoding='utf-8')
    (views / f'{page}.blade.php').write_text("@extends('orbit.layouts.app')\n@section('title', '" + title.replace("'", "\\'") + "')\n@section('description', '" + description.replace("'", "\\'") + "')\n@section('content')\n" + blade(content) + "\n@endsection\n@section('canonical', '" + ('' if page == 'index' else page+'.html') + "')\n", encoding='utf-8')
blade_header = blade(header)
for page in PAGES:
    route = 'home' if page == 'index' else page
    blade_header = blade_header.replace(f'class="nav-link" data-page="{page}"', "class=\"nav-link {{ request()->routeIs('orbit." + route + "') ? 'active' : '' }}\" data-page=\"" + page + "\" {{ request()->routeIs('orbit." + route + "') ? 'aria-current=page' : '' }}")
(views / 'partials/header.blade.php').write_text(blade_header, encoding='utf-8')
(views / 'partials/footer.blade.php').write_text(blade(footer), encoding='utf-8')
layout = blade(HEAD.replace('{title}', "@yield('title')").replace('{description}', "@yield('description')").replace('{canonical}', "@yield('canonical')")) + "\n@include('orbit.partials.header')\n<main id=\"main\">@yield('content')</main>\n@include('orbit.partials.footer')\n" + blade(SCRIPTS)
layout = re.sub(r'<link rel="canonical"[^>]+>', '<link rel="canonical" href="{{ url()->current() }}">', layout)
(views / 'layouts/app.blade.php').write_text(layout, encoding='utf-8')
print(f'Built {len(PAGES)} static HTML pages and Laravel Blade views.')

# Public discovery files and explicit compatibility redirects for the reference site paths.
urls = ['https://orbitits.com/' + ('' if key=='index' else key+'.html') for key in PAGES if key!='404']
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+u+'</loc></url>' for u in urls)+'</urlset>\n',encoding='utf-8')
(ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nDisallow: /src/\nDisallow: /laravel/\nDisallow: /tests/\nSitemap: https://orbitits.com/sitemap.xml\n',encoding='utf-8')
aliases={'about-us':'about','our-clients':'our-clients','seo-services-in-bangladesh':'seo-services','aeo-geo-services-in-bangladesh':'aeo-geo-services'}
for key in PAGES:
    if key not in ['index','404']: aliases.setdefault(key,key)
rules=['Options -Indexes','DirectoryIndex index.html','ErrorDocument 404 '+BASE_PATH+'404.html','<IfModule mod_rewrite.c>','RewriteEngine On','RewriteBase '+BASE_PATH,'RewriteRule ^(?:src|laravel|tests|\\.release|\\.git)(?:/|$) - [F,L]','RewriteRule ^(?:README|INFORMATION-NEEDED|LAUNCH-NOTES)\\.md$ - [F,L]','RewriteRule ^(?:build|verify)\\.py$ - [F,L]']
for old,new in aliases.items(): rules.append('RewriteRule ^'+old+'/?$ '+new+'.html [R=301,L]')
rules+=['</IfModule>','<IfModule mod_headers.c>','Header always set X-Content-Type-Options "nosniff"','Header always set Referrer-Policy "strict-origin-when-cross-origin"','Header always set X-Frame-Options "SAMEORIGIN"','</IfModule>','<FilesMatch "^(?:README|INFORMATION-NEEDED|LAUNCH-NOTES)\\.md$|^(?:build|verify)\\.py$">','Require all denied','</FilesMatch>']
(ROOT/'.htaccess').write_text('\n'.join(rules)+'\n',encoding='utf-8')
routes="<?php\nuse Illuminate\\Support\\Facades\\Route;\n\n"
for page in PAGES:
    if page!='404': routes+="Route::view('"+('/' if page=='index' else '/'+page)+"', 'orbit."+page+"')->name('orbit."+('home' if page=='index' else page)+"');\n"
(ROOT/'laravel/routes.example.php').write_text(routes.replace('\\\\','\\'),encoding='utf-8')

with (ROOT/'laravel/routes.example.php').open('a',encoding='utf-8') as output:
    output.write("\nRoute::match(['get', 'post'], '/enquiry', [\\App\\Http\\Controllers\\OrbitEnquiryController::class, '__invoke'])->middleware('throttle:5,1')->name('orbit.enquiry');\n")
