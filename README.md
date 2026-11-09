# OrbitIT — HTML / Laravel-friendly website

Local preview: http://localhost/orbitits.com/

## Built

30 pages: home, service directory, 12 service detail pages, pricing, company, team, clients, delivery approach, journal, 3 articles, FAQ, contact, privacy, terms, service/refund policy, cookies and 404. Matching Blade views are included.

Tailored IT BD was read for page/service coverage; its files were not modified. OrbitIT has independent frontend, content and original SVG graphics. Bangladesh contact details, client logos, reviews, affiliations and performance claims were not copied.

13 one-off GBP prices: £40, £70, £80, £95, £110, £120, £185, £260, £320, £350, £400, £450, £505. The owner confirmed £350. Handwritten demand categories are not published as sales claims. Each package defines deliverables, limits and exclusions; there is no automatic order or subscription.

Four supplied photographs are used. Proposed mailboxes: robi@orbitits.com, mithu@orbitits.com, arvi@orbitits.com, tushar@orbitits.com. The owner will activate these. CEO comes from the supplied filename and director from the incorporation filing. Other people are labelled Team member without invented roles or biographies.

Clients remain empty. Unavailable social links, hours and biographies are omitted. WhatsApp now uses the owner-confirmed +44 7466 741958. Public placeholders, draft notice and noindex were removed under the latest instruction to bypass missing information; this does not establish operational verification.

## Edit and build

- src/catalog.py: services, prices and team.
- src/site_content.py: page content, shared components and policies.
- src/graphics.py: original vector graphics.
- assets/css/orbit.css and assets/js/orbit.js: active frontend.

Run `python build.py` to regenerate HTML, Blade, graphics, routes, sitemap, robots and Apache rules. Generated page fragments are not the editorial source. Earlier style.css, main.js and globe files remain but are not loaded. Bootstrap 5.3.3 is local with its original license notices. No CDN, remote font, analytics or tracking widget is required.

Run `python build.py --production` for domain-root RewriteBase and 404 paths. Run `python build.py` again for local XAMPP paths. The intended canonical domain is https://orbitits.com/, not proof of live TLS verification.

## Enquiry delivery

contact.php implements validation, session CSRF, honeypot, session send interval and configured sender. It is disabled until configured and returns explicit failure rather than false success. Email-app/copy fallback states when nothing has been sent. PHP mail transport acceptance does not prove inbox delivery.

Set these only in the server environment:

    ORBIT_MAIL_ENABLED=1
    ORBIT_CONTACT_TO=your-active-destination-mailbox
    ORBIT_MAIL_FROM=your-verified-sender@orbitits.com

Configure a real PHP mail transport, sender-domain authentication and mailboxes before enabling; test actual receipt. Apply appropriate production server rate limits as well as session controls. Never add credentials, identity or bank files to this project.

## Laravel

1. Copy laravel/resources/views/orbit to resources/views/orbit in the target app.
2. Copy assets contents to public/assets/orbit.
3. Merge laravel/routes.example.php into routes/web.php; review existing homepage routes first.
4. Copy laravel/app/Http/Controllers/OrbitEnquiryController.php into the app and merge the entry from laravel/services-config.example.php into config/services.php.
5. Configure normal Laravel mail settings, ORBIT_MAIL_ENABLED and ORBIT_CONTACT_TO in the environment. Log/array mailers do not enable readiness.
6. Clear cached views/configuration as appropriate; verify routes and actual receipt.

Blade uses named routes, asset('assets/orbit/...'), a current-URL canonical, CSRF and throttling. The target Laravel app was not installed here; runtime integration is not claimed.

## Business facts and policies

Legal name ORBITIT SOLUTION LIMITED, number 17341168, incorporation 15 July 2026, England and Wales jurisdiction and activity codes come from the supplied PDFs. Registered address follows the later AD01 and preserves TENACE,106-2; confirm its current spelling. No live register check is claimed. A registered office is not represented as a staffed operating office.

Policies contain substantive baseline wording that the owner should review against real operations. They do not certify legal compliance or bank acceptance. Drafting references: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/the-right-to-be-informed/what-privacy-information-should-we-provide/ and https://www.legislation.gov.uk/uksi/2013/3134/part/3 . The refund policy links to the legislation and preserves applicable consumer rights.

## Deploy and verify

Publish only HTML, assets, contact.php, robots, sitemap and production .htaccess. Source/Git/internal files are denied by Apache and excluded from the public ZIP under .release/. Do not publish Laravel source/examples as static files. INFORMATION-NEEDED.md records remaining owner items privately.

Run `python verify.py`, `node --check assets/js/orbit.js` and PHP syntax checks. Local checks pass for all 30 pages, links/assets/anchors, exact prices, supplied photos, SVG/XML, redirects, internal-file restrictions, custom 404 and non-sending contact validation.

Computer Use stopped because it could not determine the current browser URL confidently enough to enforce policy. Desktop/mobile visual inspection is not verified. Live TLS, mailbox activation, inbox receipt, target Laravel runtime and bank approval are not verified. No bank account was accessed or submitted.

## WhatsApp update ? 4 November 2026

All public telephone references use +44 7466 741958. The primary form prepares name, company, email, service, package and project details into a WhatsApp chat at https://wa.me/447466741958 . The client must press Send in WhatsApp. No server email setup is required for this active flow; optional PHP/Laravel mail handlers remain inactive. The privacy text explains the WhatsApp handoff. Mailbox creation is needed only for the separate email contact links.
