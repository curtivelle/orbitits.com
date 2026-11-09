"""Local structural, pricing, URL and non-sending enquiry checks."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, urlencode
from urllib.request import urlopen, build_opener, HTTPCookieProcessor, Request
from urllib.error import HTTPError
import sys, json, http.cookiejar, xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'src'))
from catalog import PACKAGES, SERVICES, TEAM
BASE='http://localhost/orbitits.com/'
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[];self.links=[];self.h1=0;self.main=0;self.titles=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='main':self.main+=1
        if tag=='title':self.titles+=1
        for key in ('src','href'):
            if key in a:self.links.append(a[key])

pages={}
for path in ROOT.glob('*.html'):
    content=path.read_text(encoding='utf-8')
    p=Page();p.feed(content);pages[path.name]=p
    assert p.h1==1 and p.main==1 and p.titles==1,(path.name,'document structure')
    assert len(p.ids)==len(set(p.ids)),(path.name,'duplicate IDs')
    for marker in ['[Provide','[Confirm','[Project','[Real name','pending-label','draft-notice','tailoreditbd.com']:
        assert marker not in content,(path.name,'unresolved old content',marker)
    assert (ROOT/'laravel/resources/views/orbit'/path.name.replace('.html','.blade.php')).exists()
for name,p in pages.items():
    for target in p.links:
        url=urlsplit(target)
        if url.scheme or url.netloc: continue
        filename=unquote(url.path) or name
        assert (ROOT/filename).exists(),(name,'missing asset/link',target)
        if url.fragment and filename.endswith('.html'):
            assert url.fragment in pages[filename].ids,(name,'missing fragment',target)
    with urlopen(BASE+name,timeout=10) as response: assert response.status==200
print(f'PASS: {len(pages)} HTML pages, HTTP 200, local assets, anchors, headings and Blade counterparts')
assert [p['price'] for p in PACKAGES]==[40,70,80,95,110,120,185,260,320,350,400,450,505]
pricing=(ROOT/'pricing.html').read_text(encoding='utf-8')
assert pricing.count('class="price-card')==13
for p in PACKAGES:
    assert 'id="'+p['id']+'"' in pricing
    assert f"<span>£</span>{p['price']}" in pricing
for s in SERVICES:assert (ROOT/(s['slug']+'.html')).exists()
for _,_,email,photo in TEAM:
    assert (ROOT/'assets/images/team-member'/photo).exists()
    assert f'mailto:{email}@orbitits.com' in (ROOT/'team.html').read_text(encoding='utf-8')
for svg in (ROOT/'assets/images').glob('*.svg'):ET.parse(svg)
ET.parse(ROOT/'sitemap.xml')
print('PASS: 13 exact GBP prices (including confirmed £350), 12 service pages, 4 real supplied photos, vector/XML syntax')
for alias,target in [('about-us/','about.html'),('web-development/','web-development.html'),('seo-services-in-bangladesh/','seo-services.html'),('contact/','contact.html')]:
    with urlopen(BASE+alias) as response:assert response.url==BASE+target,(alias,response.url)
for hidden in ['src/catalog.py','laravel/routes.example.php','.git/config','README.md','INFORMATION-NEEDED.md']:
    try:urlopen(BASE+hidden);raise AssertionError(('private file exposed',hidden))
    except HTTPError as error:assert error.code==403,(hidden,error.code)
try:urlopen(BASE+'nonexistent-orbit-verification-page');raise AssertionError('Missing 404')
except HTTPError as error:assert error.code==404 and b'out of orbit' in error.read()
print('PASS: reference-path redirects, source/internal-file restrictions, custom HTTP 404')
opener=build_opener(HTTPCookieProcessor(http.cookiejar.CookieJar()))
with opener.open(BASE+'contact.php?action=token') as response:config=json.load(response)
assert config['ready'] is False,'Mail is enabled; stop non-sending checks until configuration is reviewed'
def post(data,status):
    try:opener.open(Request(BASE+'contact.php',urlencode(data).encode()));raise AssertionError('Unexpected success')
    except HTTPError as error:
        assert error.code==status,(status,error.code,error.read())
        result=json.load(error);assert result.get('ok') is False
post({'csrf':'invalid'},403)
post({'csrf':config['token'],'name':'Test'},422)
post({'csrf':config['token'],'name':'Local verification','company':'','email':'verify@example.invalid','service':'IT consultancy','package':'it-session','message':'Local validation only. No email should be sent.','privacy':'1','website':''},503)
print('PASS: contact CSRF, required fields, disabled-mail response; no enquiry email sent')
