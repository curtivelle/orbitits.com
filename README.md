# OrbitIT responsive HTML template

Open **http://localhost/orbitits.com/** with XAMPP Apache running, or open `index.html` directly. No Node build, CDN, external fonts, API keys or database is required. Bootstrap 5.3.3 CSS and bundle are included locally with their license notices.

## Included

- Home, Services, About and Contact pages.
- Responsive Bootstrap grid and mobile navigation.
- Original logo extracted from the supplied letterhead, plus an original SVG globe illustration.
- Service category filters, Bootstrap FAQ accordion, service selection carried into the contact page, and an accessible project-brief generator with copy support.
- Keyboard focus styles, skip navigation, labelled form controls and reduced-motion support.
- Equivalent Blade views with a shared layout, header and footer in `laravel/resources/views/orbit/`.

## Edit and rebuild

Edit `src/pages/*.html` and `src/partials/*.html`, then run:

```powershell
python build.py
```

This regenerates the four root HTML files and Blade views. Edit styles in `assets/css/style.css` and behaviour in `assets/js/main.js`. Asset files need no compilation. Edit page titles and descriptions in `build.py`. Generated HTML pages are complete documents; their core content does not depend on JavaScript.

## Laravel integration

1. Copy `laravel/resources/views/orbit/` into your Laravel application's `resources/views/orbit/`.
2. Copy the contents of this project's `assets/` directory into your Laravel application's `public/assets/orbit/`.
3. Merge the routes from `laravel/routes.example.php` into `routes/web.php`. Review the example `/` route against any existing homepage route first.
4. Clear compiled views with `php artisan view:clear` and open your application.

Blade asset references already use `asset('assets/orbit/...')`; navigation uses the example named routes. No controllers, models, middleware or database changes are required for this static template. A Laravel application has not been installed here, so Blade rendering must be checked in the target app.

## Contact form behaviour

The form deliberately prepares a brief locally. It does **not** send email, make network requests or persist form information. Copying uses the Clipboard API when available; otherwise it selects the text for manual copying. The published telephone link uses the number on the supplied letterhead. No email address was provided in the source documents.

For a real enquiry workflow, replace the brief-generator submit handler with a Laravel POST route, add `@csrf`, implement server validation and a mail/CRM handler, then provide an appropriate privacy notice. Do not present a success message until that backend confirms submission.

## Source and editorial notes

Source documents were read from `C:\Users\Hp\Downloads\orbitits.com`:

- **OIT Pad (1).pdf**: existing logo, domain and telephone number.
- **Certificate of Incorporation** and **IN01**: legal company name, company number 17341168, incorporation on 15 July 2026, company type and SIC activities 62012, 62020, 62090 and 71200.
- **AD01 OrbitIT Solution Limited.pdf**, filed 2 September 2026: later registered office, used in preference to the older South Row address on the letterhead and IN01. The PDF spells the first element `TENACE,106-2`; the template preserves this wording. Confirm that wording before publication. This is based on supplied documents, not a live register lookup.
- Articles and share-capital documents are legal records rather than website marketing material. Personal addresses, birth details, ownership information and the source PDFs are not included in the website.

Service descriptions, process and principles are proposed website copy based on the registered business activity categories. They are not evidence of completed work, certifications or contractual service commitments. No client logos, testimonials, performance statistics or portfolio claims have been invented.

## Verification

All four pages returned HTTP 200 through local XAMPP. Local links, asset paths, fragment targets, unique IDs and single H1 headings were checked. JavaScript syntax and the example PHP route file passed syntax checks. Browser-based visual and device verification was unavailable in the authoring session; review at desktop, tablet and mobile widths before publication. Laravel runtime and enquiry delivery are not tested or activated.
