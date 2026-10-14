# Builds the cecilfc.org multi-page site. Run: python3 build.py
import pathlib

ROOT = pathlib.Path(__file__).parent
PHYS = "Chesland Soccer Complex, 401 Elk Forest Rd, Elkton, MD 21921"

PAGES = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("programs.html", "Programs"),
    ("fields.html", "Fields"),
    ("governance.html", "Governance"),
    ("contact.html", "Contact"),
]

CSS = """:root{--pitch:#1F4D3A;--pitch-2:#2B6A50;--deep:#143426;--chalk:#F7F8F3;--ink:#1B2421;--muted:#55645E;--line:#D5DCD4;--yellow:#E9B925}
*{box-sizing:border-box}
body{margin:0;background:var(--chalk);color:var(--ink);font:17px/1.6 Barlow,system-ui,sans-serif;overflow-wrap:break-word}
a{color:var(--pitch-2);text-underline-offset:2px}
a:focus-visible{outline:3px solid var(--yellow);outline-offset:2px}
h1,h2,h3{font-family:'Barlow Condensed',Barlow,sans-serif;line-height:1.1;margin:0}
.wrap{max-width:980px;margin:0 auto;padding:0 20px}
.bar{background:var(--deep);color:#CFE3D7;font-size:.9rem}
.bar .wrap{padding-top:.45rem;padding-bottom:.45rem}
.bar a{color:#fff;font-weight:600}
.top{background:var(--pitch);color:#fff;border-bottom:4px solid #fff}
.top .wrap{display:flex;flex-wrap:wrap;align-items:center;gap:.4rem 1.4rem;padding-top:.8rem;padding-bottom:.8rem}
.brand{font:700 1.6rem 'Barlow Condensed',sans-serif;color:#fff;text-decoration:none;margin-right:auto;line-height:1.1}
.brand small{display:block;font:500 .78rem Barlow,sans-serif;color:#CFE3D7;letter-spacing:.02em}
nav{display:flex;flex-wrap:wrap;gap:.2rem 1.1rem}
nav a{color:#DCEBE2;text-decoration:none;font-weight:600;padding:.2rem 0;border-bottom:2px solid transparent}
nav a:hover{color:#fff}
nav a[aria-current=page]{color:#fff;border-bottom-color:var(--yellow)}
.hero{background:var(--pitch);color:#fff;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;right:-140px;top:50%;width:420px;height:420px;margin-top:-210px;border:4px solid rgba(255,255,255,.14);border-radius:50%}
.hero .wrap{padding-top:2.8rem;padding-bottom:3.2rem;position:relative;z-index:1}
.hero h1{font-size:clamp(2.8rem,8vw,5rem);font-weight:700;margin:.2rem 0 .6rem}
.hero p{font-size:1.2rem;max-width:36rem;margin:0 0 1.4rem;color:#E6F1EA}
.pagehead{background:var(--pitch);color:#fff}
.pagehead .wrap{padding-top:2rem;padding-bottom:2rem}
.pagehead h1{font-size:clamp(2.2rem,6vw,3.4rem)}
.btns{display:flex;flex-wrap:wrap;gap:.7rem}
.btn{display:inline-block;max-width:100%;padding:.7rem 1.1rem;border-radius:5px;font-weight:600;text-decoration:none;border:2px solid #fff}
.btn.primary{background:#fff;color:var(--pitch)}
.btn.ghost{color:#fff}
section{padding:2.6rem 0;border-bottom:1px solid var(--line)}
section h2{font-size:2rem;margin-bottom:.8rem}
section h3{font-size:1.35rem;margin:1.2rem 0 .3rem}
.grid{display:grid;gap:1.3rem}
@media(min-width:760px){.two{grid-template-columns:1.2fr 1fr}.three{grid-template-columns:repeat(3,1fr)}}
.card{background:#fff;border:1px solid var(--line);border-top:5px solid var(--pitch);border-radius:6px;padding:1.1rem 1.25rem}
.card h3{margin-top:0}
.card p{margin:.3rem 0 .6rem;color:var(--muted)}
.facts{align-self:start;background:#fff;border:1px solid var(--line);border-radius:8px;padding:1.3rem 1.4rem}
.facts h3{margin-top:0;margin-bottom:.7rem}
dl{margin:0;display:grid;grid-template-columns:max-content 1fr;gap:.45rem 1.2rem}
dt{font-weight:600}dd{margin:0}
blockquote{margin:0;padding-left:1.1rem;border-left:4px solid var(--pitch)}
.cite{color:var(--muted);font-size:.92rem}
ul.clean{padding-left:1.2rem}ul.clean li{margin-bottom:.35rem}
table{border-collapse:collapse;width:100%;background:#fff}
th,td{text-align:left;padding:.55rem .7rem;border-bottom:1px solid var(--line);vertical-align:top}
th{font-weight:600;background:#EEF2EC}
footer{background:var(--deep);color:#CFE3D7;padding:2rem 0;font-size:.95rem}
footer a{color:#fff}
footer .cols{display:grid;gap:1rem}
@media(min-width:760px){footer .cols{grid-template-columns:1.4fr 1fr 1fr}}
footer h3{color:#fff;font-size:1.1rem;margin-bottom:.3rem}
footer p{margin:.2rem 0}
@media(max-width:520px){dl{grid-template-columns:1fr;gap:.1rem}dd{margin-bottom:.6rem}.hero::after{display:none}}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600&family=Barlow+Condensed:wght@600;700&display=swap">'

LD = """<script type="application/ld+json">{"@context":"https://schema.org","@type":"SportsOrganization","name":"Cecil Soccer League, Inc.","alternateName":"Cecil FC","url":"https://cecilfc.org/","sameAs":["https://www.cecilsoccer.org/"],"sport":"Soccer","nonprofitStatus":"Nonprofit501c3","taxID":"52-1311485","email":"info@cecilsoccer.org","telephone":"+1-410-670-7347","address":{"@type":"PostalAddress","streetAddress":"401 Elk Forest Rd","addressLocality":"Elkton","addressRegion":"MD","postalCode":"21921","addressCountry":"US"},"location":{"@type":"Place","name":"Chesland Soccer Complex","address":{"@type":"PostalAddress","streetAddress":"401 Elk Forest Rd","addressLocality":"Elkton","addressRegion":"MD","postalCode":"21921","addressCountry":"US"}}}</script>"""


def shell(fname, title, desc, body, hero=None):
    nav = "".join(
        f'<a href="{f}"{" aria-current=\"page\"" if f == fname else ""}>{t}</a>' for f, t in PAGES
    )
    head = hero or f'<div class="pagehead"><div class="wrap"><h1>{title}</h1></div></div>'
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Cecil Soccer League, Inc. (Cecil FC)</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://cecilfc.org/{'' if fname == 'index.html' else fname}">
{FONTS}<link rel="stylesheet" href="style.css">{LD if fname == 'index.html' else ''}
</head><body>
<div class="bar"><div class="wrap">cecilfc.org is an official website of <strong>Cecil Soccer League, Inc.</strong>, a 501(c)(3) nonprofit. Registration and team pages: <a href="https://www.cecilsoccer.org/">cecilsoccer.org</a></div></div>
<header class="top"><div class="wrap"><a class="brand" href="index.html">Cecil FC<small>Cecil Soccer League, Inc.</small></a><nav aria-label="Main">{nav}</nav></div></header>
{head}
<main>{body}</main>
<footer><div class="wrap cols">
<div><h3>Cecil Soccer League, Inc. (Cecil FC)</h3><p>501(c)(3) nonprofit &middot; EIN 52-1311485</p><p>Youth soccer in Cecil County, Maryland.</p></div>
<div><h3>Physical address</h3><p>Chesland Soccer Complex<br>401 Elk Forest Rd<br>Elkton, MD 21921</p></div>
<div><h3>Mailing address</h3><p>P.O. Box 1406<br>Elkton, MD 21922-1406</p><p><a href="mailto:info@cecilsoccer.org">info@cecilsoccer.org</a><br><a href="tel:+14106707347">(410) 670-7347</a></p></div>
</div><div class="wrap"><p style="margin-top:1.2rem">&copy; 2026 Cecil Soccer League, Inc. All rights reserved. Main website: <a href="https://www.cecilsoccer.org/">cecilsoccer.org</a></p></div></footer>
</body></html>
"""


HOME = shell("index.html", "Home",
    "Cecil FC is the youth soccer program of Cecil Soccer League, Inc., a 501(c)(3) nonprofit at Chesland Soccer Complex in Elkton, Maryland.",
    f"""
<section><div class="wrap grid two">
<div><h2>Who we are</h2>
<p><strong>Cecil Soccer League, Inc.</strong> is a nonprofit youth soccer organization serving Cecil County, Maryland, and the surrounding area. Our programs play as <strong>Cecil FC</strong>. We run spring, fall, and winter indoor seasons of instructional youth soccer for players ages 4 to 18, with approximately 1,200 participants each year.</p>
<p>The league is run by volunteer officers, directors, and coaches, and is recognized by the IRS as a 501(c)(3) tax-exempt organization.</p>
<p><a href="about.html">More about the league</a></p></div>
<div class="facts"><h3>At a glance</h3><dl>
<dt>Legal name</dt><dd>Cecil Soccer League, Inc.</dd>
<dt>Also known as</dt><dd>Cecil FC</dd>
<dt>Tax status</dt><dd>501(c)(3), exempt since 1991</dd>
<dt>EIN</dt><dd>52-1311485</dd>
<dt>Home field</dt><dd>{PHYS}</dd>
<dt>Mailing</dt><dd>P.O. Box 1406, Elkton, MD 21922-1406</dd>
</dl></div></div></section>
<section><div class="wrap"><h2>Programs</h2><div class="grid three">
<div class="card"><h3>Recreational</h3><p>Spring and fall seasons for players of all experience levels.</p><a href="programs.html#rec">Learn more</a></div>
<div class="card"><h3>Competitive</h3><p>Travel teams by birth year, with annual tryouts.</p><a href="programs.html#competitive">Learn more</a></div>
<div class="card"><h3>Winter indoor</h3><p>Off-season indoor play at the Cecil Arena.</p><a href="programs.html#indoor">Learn more</a></div>
</div></div></section>
<section><div class="wrap grid two">
<div><h2>Where we play</h2><p>Our home is the <strong>Chesland Soccer Complex</strong> at 401 Elk Forest Rd in Elkton, part of Cecil County's Chesland Park. The league has managed its soccer facilities under a lease with Cecil County since 2002.</p><p><a href="fields.html">Fields and directions</a></p></div>
<div><h2>Get in touch</h2><p>General questions: <a href="mailto:info@cecilsoccer.org">info@cecilsoccer.org</a><br>Board of Directors: <a href="mailto:board@cecilsoccer.org">board@cecilsoccer.org</a><br>Phone: <a href="tel:+14106707347">(410) 670-7347</a></p><p><a href="contact.html">All contact information</a></p></div>
</div></section>""",
    hero="""<div class="hero"><div class="wrap"><h1>Cecil FC</h1><p>Recreational, competitive, and winter indoor youth soccer for Cecil County families, run by volunteers.</p><div class="btns"><a class="btn primary" href="https://www.cecilsoccer.org/">Register at cecilsoccer.org</a><a class="btn ghost" href="about.html">About the league</a></div></div></div>""")

ABOUT = shell("about.html", "About",
    "About Cecil Soccer League, Inc.: mission, history, and organization details.",
    """
<section><div class="wrap"><h2>Our mission</h2>
<blockquote>Cecil Soccer League is committed to maximizing the potential of all athletes and dedicated to developing in each player a love of soccer. We will encourage positive character development by teaching the fundamentals of Sportsmanship, Teamwork, Self-Improvement, Respect, Discipline and Exercise. We will provide training and educational opportunities for players, coaches and referees participating in Cecil Soccer League. We strive to build a safe family-oriented soccer experience for our players through Teams (Representative &amp; Recreational), Tournaments, Leagues and Soccer Camps. Above all else, Cecil Soccer League is about having fun while competing in the game we love, SOCCER!</blockquote>
<p class="cite">Mission statement of Cecil Soccer League, Inc.</p></div></section>
<section><div class="wrap grid two">
<div><h2>Our purpose</h2>
<p>Cecil Soccer League is organized exclusively for charitable and educational purposes, to promote sportsmanship and the development of youth soccer players through competition within and outside the State of Maryland. To do that, the league:</p>
<ul class="clean"><li>Runs recreational league play for the youth of Cecil County and the surrounding area</li><li>Forms competitive teams that play in leagues and tournaments</li><li>Recruits and trains volunteer coaches</li><li>Provides and maintains fields, uniforms, and equipment</li><li>Hosts tournaments and camps</li></ul>
<h2 style="margin-top:1.6rem">Our history</h2>
<p>Cecil Soccer League was recognized as a 501(c)(3) tax-exempt organization in 1991. In 2002 the league entered a long-term lease and management agreement with Cecil County to plan, build, maintain, and operate the soccer facilities at Chesland Park, which became the Chesland Soccer Complex. Volunteers have built and maintained the complex since.</p></div>
<div class="facts"><h3>Organization details</h3><dl>
<dt>Legal name</dt><dd>Cecil Soccer League, Inc.</dd>
<dt>Program name</dt><dd>Cecil FC</dd>
<dt>Type</dt><dd>Maryland nonprofit corporation</dd>
<dt>Tax status</dt><dd>501(c)(3) tax-exempt (since 1991)</dd>
<dt>EIN</dt><dd>52-1311485</dd>
<dt>Physical address</dt><dd>Chesland Soccer Complex<br>401 Elk Forest Rd<br>Elkton, MD 21921</dd>
<dt>Mailing address</dt><dd>P.O. Box 1406<br>Elkton, MD 21922-1406</dd>
<dt>Participants</dt><dd>About 1,200 per year</dd>
<dt>Websites</dt><dd><a href="https://www.cecilsoccer.org/">cecilsoccer.org</a><br>cecilfc.org</dd>
</dl></div></div></section>""")

PROGRAMS = shell("programs.html", "Programs",
    "Recreational, competitive, and winter indoor youth soccer programs of Cecil Soccer League, Inc.",
    """
<section id="rec"><div class="wrap"><h2>Recreational soccer</h2>
<p>Spring and fall recreational seasons for players of all skill levels, from first-time players up through high school age. Teams are formed by the league, coached by parent volunteers, and play at the Chesland Soccer Complex. The focus is fun, fundamentals, and sportsmanship.</p>
<p><a href="https://www.cecilsoccer.org/">Registration and season details at cecilsoccer.org</a></p></div></section>
<section id="competitive"><div class="wrap"><h2>Competitive (travel) soccer</h2>
<p>Cecil FC competitive teams are organized by birth year for players looking for a higher level of play. Players are selected through annual tryouts, and teams compete in regional leagues and tournaments. The league registers its competitive players with the Maryland State Youth Soccer Association.</p>
<p><a href="https://www.cecilsoccer.org/competitive-csl/">Travel teams and tryout information</a></p></div></section>
<section id="indoor"><div class="wrap"><h2>Winter indoor</h2>
<p>An off-season indoor program played at the Cecil Arena, 2706 North East Rd, North East, MD 21901.</p></div></section>
<section><div class="wrap"><h2>Tournaments, camps, and scholarships</h2>
<ul class="clean"><li><strong>Tournaments:</strong> the league hosts tournaments at Chesland, including the Chesapeake Cup and the Fall Blast.</li><li><strong>Camps and clinics:</strong> training opportunities for players and coaches.</li><li><strong>John Jones Memorial College Scholarship:</strong> the league&rsquo;s college scholarship program.</li></ul></div></section>
<section><div class="wrap"><h2>Coaches and referees</h2>
<p>All coaches are volunteers. The league supports coach education and licensing and encourages older players to become certified referees.</p></div></section>""")

FIELDS = shell("fields.html", "Fields",
    "Chesland Soccer Complex, 401 Elk Forest Rd, Elkton, MD: home fields of Cecil Soccer League, Inc.",
    f"""
<section><div class="wrap grid two">
<div><h2>Chesland Soccer Complex</h2>
<p><strong>401 Elk Forest Rd, Elkton, MD 21921</strong></p>
<p>The Chesland Soccer Complex is the league's home field and physical location. It sits within Cecil County's Chesland Park. Under a 2002 lease and management agreement with Cecil County, Cecil Soccer League plans, maintains, and operates the soccer facilities on about 88 acres of the park.</p>
<p>The complex has full-size 11v11 fields and smaller fields for younger age groups, plus parking and a playground.</p>
<p><a href="https://www.google.com/maps/search/?api=1&query=401+Elk+Forest+Rd+Elkton+MD+21921">Directions (Google Maps)</a> &middot; <a href="https://www.cecilsoccer.org/information/field-map/">Field map</a></p></div>
<div class="facts"><h3>Visiting Chesland</h3><dl>
<dt>Address</dt><dd>{PHYS}</dd>
<dt>Owner</dt><dd>Cecil County, Maryland</dd>
<dt>Operator</dt><dd>Cecil Soccer League, Inc.</dd>
</dl></div></div></section>
<section><div class="wrap"><h2>Cecil Arena (winter indoor)</h2><p>2706 North East Rd, North East, MD 21901</p></div></section>""")

GOV = shell("governance.html", "Governance",
    "Governance of Cecil Soccer League, Inc.: board of directors, bylaws, affiliations, and nonprofit status.",
    """
<section><div class="wrap grid two">
<div><h2>Board of Directors</h2>
<p>Cecil Soccer League, Inc. is governed by a volunteer Board of Directors under the league's bylaws. The board sets policy, approves budgets, oversees the league's finances and facilities, and elects the league's officers.</p>
<h3>Officers and directors</h3>
<table><thead><tr><th>Role</th><th>Responsibility</th></tr></thead><tbody>
<tr><td>President</td><td>Chairs the board and oversees league operations</td></tr>
<tr><td>Vice President, Recreational</td><td>Recreational program</td></tr>
<tr><td>Vice President, Competitive (Travel)</td><td>Competitive program</td></tr>
<tr><td>Treasurer</td><td>Finances, records, and filings</td></tr>
<tr><td>Secretary</td><td>Minutes, notices, and official records</td></tr>
<tr><td>Director of Coaching</td><td>Coach development and licensing</td></tr>
<tr><td>Director of Facilities</td><td>Chesland Soccer Complex operations</td></tr>
<tr><td>Director of Marketing</td><td>Outreach and sponsorships</td></tr>
</tbody></table>
<p>Contact the board at <a href="mailto:board@cecilsoccer.org">board@cecilsoccer.org</a>.</p></div>
<div class="facts"><h3>Nonprofit status</h3><dl>
<dt>Organization</dt><dd>Cecil Soccer League, Inc.</dd>
<dt>IRS status</dt><dd>501(c)(3) public charity</dd>
<dt>EIN</dt><dd>52-1311485</dd>
<dt>Annual filing</dt><dd>IRS Form 990</dd>
<dt>Physical address</dt><dd>401 Elk Forest Rd, Elkton, MD 21921</dd>
</dl></div></div></section>
<section><div class="wrap"><h2>Affiliations</h2>
<p>Cecil Soccer League is a member of the <strong>Maryland State Youth Soccer Association (MSYSA)</strong>, <strong>US Youth Soccer</strong>, and the <strong>United States Soccer Federation</strong>, and follows their rules and policies. All players, coaches, and teams are registered through MSYSA.</p></div></section>
<section><div class="wrap"><h2>Policies</h2>
<ul class="clean"><li><strong>Non-discrimination:</strong> the league does not discriminate on the basis of race, ethnic origin, age, religion, sex, or disability in its membership, board, committees, staff, or participants.</li><li><strong>Bylaws:</strong> the league is governed by bylaws adopted by its Board of Directors.</li><li><strong>Refunds:</strong> refund requests are made in writing to info@cecilsoccer.org, as described on cecilsoccer.org.</li></ul></div></section>""")

CONTACT = shell("contact.html", "Contact",
    "Contact Cecil Soccer League, Inc. (Cecil FC): addresses, email, and phone.",
    f"""
<section><div class="wrap grid three">
<div class="card"><h3>Physical address</h3><p>Chesland Soccer Complex<br>401 Elk Forest Rd<br>Elkton, MD 21921</p><a href="https://www.google.com/maps/search/?api=1&query=401+Elk+Forest+Rd+Elkton+MD+21921">Directions</a></div>
<div class="card"><h3>Mailing address</h3><p>Cecil Soccer League, Inc.<br>P.O. Box 1406<br>Elkton, MD 21922-1406</p></div>
<div class="card"><h3>Email &amp; phone</h3><p>General: <a href="mailto:info@cecilsoccer.org">info@cecilsoccer.org</a><br>Board: <a href="mailto:board@cecilsoccer.org">board@cecilsoccer.org</a><br><a href="tel:+14106707347">(410) 670-7347</a></p></div>
</div></section>
<section><div class="wrap"><h2>Registration questions</h2><p>Registration, schedules, and team information are on our main website, <a href="https://www.cecilsoccer.org/">cecilsoccer.org</a>.</p></div></section>""")

(ROOT / "style.css").write_text(CSS)
for name, html in [("index.html", HOME), ("about.html", ABOUT), ("programs.html", PROGRAMS), ("fields.html", FIELDS), ("governance.html", GOV), ("contact.html", CONTACT)]:
    (ROOT / name).write_text(html)
print("built", len(PAGES), "pages")
