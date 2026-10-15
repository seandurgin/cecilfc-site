# Builds the cecilfc.org multi-page site. Run: python3 build.py
# Look, wording and photos carried over from cecilsoccer.org (Cecil FC brand: black, gold, red, white).
import pathlib

ROOT = pathlib.Path(__file__).parent
PHYS = "Chesland Soccer Complex, 401 Elk Forest Rd, Elkton, MD 21921"
MAPS_CHES = "https://www.google.com/maps/search/?api=1&query=401+Elk+Forest+Rd+Elkton+MD+21921"
MAPS_ARENA = "https://www.google.com/maps/search/?api=1&query=Cecil+Arena+2706+North+East+Rd+North+East+MD+21901"
CSL = "https://www.cecilsoccer.org"

PAGES = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("programs.html", "Programs"),
    ("tournaments.html", "Tournaments"),
    ("fields.html", "Fields"),
    ("photos.html", "Photos"),
    ("governance.html", "Governance"),
    ("contact.html", "Contact"),
]

CSS = """:root{--black:#0a0a0a;--ink:#1d1d1d;--gold:#eac300;--gold-2:#f5d63d;--red:#c8102e;--red-2:#a50d26;--paper:#f6f5f1;--line:#e3e1da;--muted:#5d5d5d}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 'Open Sans',Helvetica,Arial,sans-serif;overflow-wrap:break-word}
img{max-width:100%;height:auto;display:block}
a{color:var(--red);text-underline-offset:2px}
a:focus-visible,.btn:focus-visible{outline:3px solid var(--gold);outline-offset:2px}
h1,h2,h3{font-family:Oswald,'Arial Narrow',sans-serif;line-height:1.15;margin:0;text-transform:uppercase;letter-spacing:.01em}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
.bar{background:var(--red);color:#fff;font-size:.85rem}
.bar .wrap{padding-top:.4rem;padding-bottom:.4rem}
.bar a{color:#fff;font-weight:700}
.top{background:var(--black);color:#fff;border-bottom:5px solid var(--gold);position:sticky;top:0;z-index:5}
.top .wrap{display:flex;flex-wrap:wrap;align-items:center;gap:.4rem 1.4rem;padding-top:.55rem;padding-bottom:.55rem}
.brand{display:flex;align-items:center;gap:.7rem;color:#fff;text-decoration:none;margin-right:auto}
.brand img{width:58px;height:58px}
.brand span{font:600 1.55rem/1 Oswald,sans-serif;text-transform:uppercase}
.brand small{display:block;font:600 .72rem 'Open Sans',sans-serif;color:var(--gold);letter-spacing:.06em;margin-top:.25rem}
nav{display:flex;flex-wrap:wrap;gap:.15rem 1rem}
nav a{color:#e9e9e9;text-decoration:none;font:500 .98rem Oswald,sans-serif;text-transform:uppercase;letter-spacing:.03em;padding:.2rem 0;border-bottom:3px solid transparent}
nav a:hover{color:var(--gold)}
nav a[aria-current=page]{color:#fff;border-bottom-color:var(--gold)}
.hero{position:relative;color:#fff;background:#000 url(img/fire-presidents-cup.jpg) center 35%/cover}
.hero::before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.88) 0%,rgba(0,0,0,.65) 55%,rgba(0,0,0,.25) 100%)}
.hero .wrap{position:relative;padding-top:4rem;padding-bottom:4.4rem}
.hero .kicker{color:var(--gold);font:600 1rem Oswald,sans-serif;text-transform:uppercase;letter-spacing:.12em;margin:0}
.hero h1{font-size:clamp(2.5rem,7vw,4.6rem);margin:.3rem 0 .8rem;max-width:14ch}
.hero p{font-size:1.15rem;max-width:34rem;margin:0 0 1.6rem;color:#f1f1f1}
.stripe{height:10px;background:repeating-linear-gradient(135deg,var(--gold) 0 22px,var(--black) 22px 44px)}
.pagehead{background:var(--black);color:#fff}
.pagehead .wrap{padding-top:2.2rem;padding-bottom:2.2rem}
.pagehead h1{font-size:clamp(2.1rem,6vw,3.3rem)}
.pagehead p{margin:.4rem 0 0;color:#d6d6d6;max-width:44rem}
.btns{display:flex;flex-wrap:wrap;gap:.7rem}
.btn{display:inline-block;max-width:100%;padding:.72rem 1.25rem;border-radius:3px;font:600 1rem Oswald,sans-serif;text-transform:uppercase;letter-spacing:.04em;text-decoration:none;border:2px solid transparent}
.btn.primary{background:var(--gold);color:var(--black)}
.btn.primary:hover{background:var(--gold-2)}
.btn.red{background:var(--red);color:#fff}
.btn.red:hover{background:var(--red-2)}
.btn.ghost{color:#fff;border-color:#fff}
section{padding:2.8rem 0}
section+section{border-top:1px solid var(--line)}
section.dark{background:var(--black);color:#eee;border:0}
section.dark h2{color:#fff}
section.dark a:not(.btn){color:var(--gold)}
section h2{font-size:2rem;margin-bottom:.9rem}
section h2::after{content:"";display:block;width:56px;height:4px;background:var(--gold);margin-top:.45rem}
section h3{font-size:1.3rem;margin:1.3rem 0 .35rem}
.grid{display:grid;gap:1.4rem}
@media(min-width:780px){.two{grid-template-columns:1fr 1fr}.two-w{grid-template-columns:1.35fr 1fr}.three{grid-template-columns:repeat(3,1fr)}}
.card{background:#fff;border:1px solid var(--line);border-radius:6px;overflow:hidden;display:flex;flex-direction:column}
.card>img{aspect-ratio:3/1;object-fit:cover;width:100%}
.card .body{padding:1rem 1.2rem 1.2rem;display:flex;flex-direction:column;gap:.4rem;flex:1}
.card h3{margin:0}
.card p{margin:0;color:var(--muted)}
.card .more{margin-top:auto;font-weight:700}
.panel{align-self:start;background:#fff;border:1px solid var(--line);border-top:5px solid var(--red);border-radius:6px;padding:1.3rem 1.4rem}
.panel h3{margin-top:0;margin-bottom:.7rem}
dl{margin:0;display:grid;grid-template-columns:max-content 1fr;gap:.45rem 1.2rem}
dt{font-weight:700}dd{margin:0}
blockquote{margin:0;padding:1.2rem 1.4rem;background:#fff;border-left:6px solid var(--gold);border-radius:4px;font-size:1.05rem}
.cite{color:var(--muted);font-size:.92rem}
ul.clean{padding-left:1.2rem;margin:.4rem 0}ul.clean li{margin-bottom:.35rem}
table{border-collapse:collapse;width:100%;background:#fff}
th,td{text-align:left;padding:.55rem .7rem;border-bottom:1px solid var(--line);vertical-align:top}
th{font-weight:700;background:#efede6}
.tablewrap{overflow-x:auto}
.shot{border-radius:6px;border:1px solid var(--line)}
figure{margin:0}
figcaption{font-size:.9rem;color:var(--muted);padding:.5rem .1rem 0}
.gallery{display:grid;gap:1.2rem;grid-template-columns:repeat(auto-fill,minmax(280px,1fr))}
.gallery img{aspect-ratio:4/3;object-fit:cover;width:100%;border-radius:6px}
.callout{background:var(--gold);color:var(--black);border-radius:6px;padding:1.2rem 1.4rem}
.callout h3{margin:0 0 .3rem}
.callout p{margin:0}
.callout a{color:var(--black);font-weight:700}
.badge{display:inline-block;background:var(--red);color:#fff;font:600 .78rem Oswald,sans-serif;text-transform:uppercase;letter-spacing:.06em;padding:.15rem .55rem;border-radius:3px}
footer{background:var(--black);color:#cfcfcf;padding:2.4rem 0 1.4rem;font-size:.95rem;border-top:5px solid var(--gold)}
footer a{color:var(--gold)}
footer .cols{display:grid;gap:1.2rem}
@media(min-width:780px){footer .cols{grid-template-columns:auto 1.3fr 1fr 1fr}}
footer img{width:84px;height:84px}
footer h3{color:#fff;font-size:1.05rem;margin-bottom:.35rem}
footer p{margin:.2rem 0}
footer .legal{border-top:1px solid #2c2c2c;margin-top:1.6rem;padding-top:1rem;font-size:.88rem}
@media(max-width:560px){dl{grid-template-columns:1fr;gap:.1rem}dd{margin-bottom:.6rem}.brand img{width:46px;height:46px}.top{position:static}}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&family=Oswald:wght@500;600&display=swap">'

LD = """<script type="application/ld+json">{"@context":"https://schema.org","@type":"SportsOrganization","name":"Cecil Soccer League, Inc.","alternateName":"Cecil FC","url":"https://cecilfc.org/","logo":"https://cecilfc.org/img/cfc-logo.png","sameAs":["https://www.cecilsoccer.org/","https://www.facebook.com/CecilSoccer/","https://www.instagram.com/cecilsoccer/"],"sport":"Soccer","nonprofitStatus":"Nonprofit501c3","taxID":"52-1311485","email":"info@cecilsoccer.org","telephone":"+1-410-670-7347","address":{"@type":"PostalAddress","streetAddress":"401 Elk Forest Rd","addressLocality":"Elkton","addressRegion":"MD","postalCode":"21921","addressCountry":"US"},"location":{"@type":"Place","name":"Chesland Soccer Complex","address":{"@type":"PostalAddress","streetAddress":"401 Elk Forest Rd","addressLocality":"Elkton","addressRegion":"MD","postalCode":"21921","addressCountry":"US"}}}</script>"""


def shell(fname, title, desc, body, hero=None, sub=""):
    nav = "".join(
        f'<a href="{f}"{" aria-current=\"page\"" if f == fname else ""}>{t}</a>' for f, t in PAGES
    )
    head = hero or f'<div class="pagehead"><div class="wrap"><h1>{title}</h1>{f"<p>{sub}</p>" if sub else ""}</div></div>'
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Cecil Soccer League, Inc. (Cecil FC)</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://cecilfc.org/{'' if fname == 'index.html' else fname}">
<link rel="icon" href="img/cfc-logo.png">
{FONTS}<link rel="stylesheet" href="style.css">{LD if fname == 'index.html' else ''}
</head><body>
<div class="bar"><div class="wrap">cecilfc.org is an official website of <strong>Cecil Soccer League, Inc.</strong>, a 501(c)(3) nonprofit. Registration and team pages: <a href="{CSL}/">cecilsoccer.org</a></div></div>
<header class="top"><div class="wrap"><a class="brand" href="index.html"><img src="img/logo.png" alt="Cecil FC logo" width="58" height="58"><span>Cecil FC<small>Cecil Soccer League, Inc.</small></span></a><nav aria-label="Main">{nav}</nav></div></header>
{head}
<div class="stripe" aria-hidden="true"></div>
<main>{body}</main>
<footer><div class="wrap cols">
<div><img src="img/cfc-logo.png" alt="" width="84" height="84"></div>
<div><h3>Cecil Soccer League, Inc. (Cecil FC)</h3><p>501(c)(3) nonprofit &middot; EIN 52-1311485</p><p>An established youth soccer league in Cecil County, Maryland.</p><p><a href="https://www.facebook.com/CecilSoccer/">Facebook</a> &middot; <a href="https://www.instagram.com/cecilsoccer/">Instagram</a></p></div>
<div><h3>Physical address</h3><p>Chesland Soccer Complex<br>401 Elk Forest Rd<br>Elkton, MD 21921</p></div>
<div><h3>Mailing address</h3><p>P.O. Box 1406<br>Elkton, MD 21922-1406</p><p><a href="mailto:info@cecilsoccer.org">info@cecilsoccer.org</a><br><a href="tel:+14106707347">(410) 670-7347</a></p></div>
</div><div class="wrap legal">&copy; 2026 Cecil Soccer League, Inc. All rights reserved. Main website: <a href="{CSL}/">cecilsoccer.org</a></div></footer>
</body></html>
"""


def card(img, alt, title, text, href, link="Learn more"):
    return f'<div class="card"><img src="img/{img}" alt="{alt}" loading="lazy"><div class="body"><h3>{title}</h3><p>{text}</p><a class="more" href="{href}">{link} &rarr;</a></div></div>'


COACH = """<h3>Coaching a team</h3>
<p>All coaches are volunteers and are often a parent of a player in the program. Consider it a rewarding opportunity to support the community and have fun. <strong>Head coaches receive a 100% reimbursement</strong> of their child&rsquo;s registration (one child per coach), applied when the season ends.</p>
<p>Each coach must:</p>
<ul class="clean"><li>Complete a TeamSnap coach registration form</li><li>Complete a GotSport registration form (sent in the TeamSnap confirmation email)</li><li>Complete coaching requirements in GotSport: background check, CDC concussion course, and SafeSport training</li></ul>
<p class="cite">Coaching requirements are valid for one year and restart every July 1.</p>"""

HOME = shell("index.html", "Home",
    "Cecil FC is the youth soccer program of Cecil Soccer League, Inc., a 501(c)(3) nonprofit at Chesland Soccer Complex in Elkton, Maryland.",
    f"""
<section><div class="wrap grid two-w">
<div><h2>Who are we?</h2>
<p>We are an established soccer league located in Cecil County, Maryland. Whether you are interested in a <strong>Recreational</strong>, <strong>Competitive</strong> and/or <strong>Winter (indoor)</strong> program, we would love for your family to become part of our family!</p>
<p><strong>Cecil Soccer League, Inc.</strong> is a volunteer-run, 501(c)(3) nonprofit. Our programs play as <strong>Cecil FC</strong>, serving roughly 1,200 players ages 4 to 18 each year at the Chesland Soccer Complex in Elkton.</p>
<p><a href="about.html">More about the league &rarr;</a></p></div>
<div class="panel"><h3>At a glance</h3><dl>
<dt>Legal name</dt><dd>Cecil Soccer League, Inc.</dd>
<dt>Also known as</dt><dd>Cecil FC</dd>
<dt>Tax status</dt><dd>501(c)(3) nonprofit</dd>
<dt>EIN</dt><dd>52-1311485</dd>
<dt>Home field</dt><dd>{PHYS}</dd>
<dt>Mailing</dt><dd>P.O. Box 1406, Elkton, MD 21922-1406</dd>
</dl></div></div></section>
<section><div class="wrap"><h2>Our programs</h2><div class="grid three">
{card("league-header.jpg", "Cecil Soccer League Recreational Soccer banner", "Recreational", "Fun, safe, and competitive soccer for every kid, from U3 through high school. Spring and fall at Chesland.", "programs.html#rec")}
{card("club-header.jpg", "Cecil Soccer Club Competitive Soccer banner", "Competitive (travel)", "Travel teams from U9 up through high school, led by licensed coaches. Tryouts every spring.", "programs.html#travel")}
{card("cecil-arena.jpg", "The Cecil Arena", "Winter indoor", "Games-only indoor rec at the Cecil Arena, January through February.", "programs.html#indoor")}
</div></div></section>
<section class="dark"><div class="wrap grid two">
<div><span class="badge">Now open</span><h2 style="margin-top:.6rem">Winter Indoor Rec 2027</h2>
<p>Season runs <strong>January 2 &ndash; February 27, 2027</strong> at the Cecil Arena. Divisions U6 through U18.</p>
<ul class="clean"><li>Regular registration (Oct 14 &ndash; Nov 30): <strong>$90</strong></li><li>Late registration (Dec 1 &ndash; Dec 11): <strong>$110</strong></li></ul>
<div class="btns" style="margin-top:1rem"><a class="btn primary" href="{CSL}/recreation-csl/winter-indoor-rec/">Register for winter indoor</a></div></div>
<div><span class="badge">November 14 &amp; 15</span><h2 style="margin-top:.6rem">18th Annual Cecil Fall Blast</h2>
<p>One-day tournament, three games guaranteed. Boys on November 14, girls on November 15, U8&ndash;U16. Application deadline <strong>October 26, 2026</strong>.</p>
<div class="btns" style="margin-top:1rem"><a class="btn red" href="tournaments.html#fall-blast">Tournament details</a></div></div>
</div></section>
<section><div class="wrap grid two">
<figure><img class="shot" src="img/john-jones.jpg" alt="Cecil FC John Jones Memorial Scholarship banner" loading="lazy"></figure>
<div><h2>John Jones Memorial College Scholarship</h2>
<p>John Jones was instrumental in building the Chesland Soccer Complex and the Bard Cameron Sports Park. Each year Cecil Soccer awards two $1,500 scholarships in his name to graduating seniors who best exemplify community service, academic excellence, and good sportsmanship.</p>
<p><a href="programs.html#scholarship">Scholarship details &rarr;</a></p></div>
</div></section>
<section><div class="wrap grid two">
<div><h2>Where we play</h2><p>Outdoor rec and home travel games are played at the <strong>Chesland Soccer Complex</strong>, 401 Elk Forest Rd, Elkton. The league has operated the complex under a lease with Cecil County since 2002. Winter indoor games are at the <strong>Cecil Arena</strong> in North East.</p><p><a href="fields.html">Field map and directions &rarr;</a></p></div>
<div class="callout"><h3>Stay in the loop</h3><p>Get registration openings, schedules, and field updates by email. <a href="http://eepurl.com/ghSJK9">Join our mailing list &rarr;</a></p><p style="margin-top:.6rem">Questions? <a href="mailto:info@cecilsoccer.org">info@cecilsoccer.org</a> &middot; <a href="tel:+14106707347">(410) 670-7347</a></p></div>
</div></section>""",
    hero=f"""<div class="hero"><div class="wrap"><p class="kicker">Cecil County, Maryland</p><h1>Welcome to Cecil Soccer Club</h1><p>Recreational, competitive, and winter indoor youth soccer for Cecil County families, run by volunteers.</p><div class="btns"><a class="btn primary" href="{CSL}/recreation-csl/">Recreational soccer</a><a class="btn ghost" href="{CSL}/competitive-csl/tryout-info-2/">Competitive tryouts</a></div></div></div>""")

ABOUT = shell("about.html", "About",
    "About Cecil Soccer League, Inc.: mission, history, policies, and organization details.",
    f"""
<section><div class="wrap"><h2>Mission statement</h2>
<blockquote>Cecil Soccer League is committed to maximizing the potential of all athletes and dedicated to developing in each player a love of soccer. We will encourage positive character development by teaching the fundamentals of Sportsmanship, Teamwork, Self-Improvement, Respect, Discipline and Exercise. We will provide training and educational opportunities for players, coaches and referees participating in Cecil Soccer League. We strive to build a safe family-oriented soccer experience for our players through Teams (Representative &amp; Recreational), Tournaments, Leagues and Soccer Camps. Above all else, Cecil Soccer League is about having fun while competing in the game we love, SOCCER!</blockquote></div></section>
<section><div class="wrap grid two-w">
<div><h2>Who are we?</h2>
<p>We are an established soccer league located in Cecil County, MD. Whether you are interested in a Recreational, Competitive and/or Winter (indoor) program, we would love for your family to become part of our family!</p>
<h3>Our purpose</h3>
<p>Cecil Soccer League is organized exclusively for charitable and educational purposes, to promote sportsmanship and the development of youth soccer players through competition within and outside the State of Maryland. To do that, the league:</p>
<ul class="clean"><li>Runs recreational league play for the youth of Cecil County and the surrounding area</li><li>Forms competitive teams that play in leagues and tournaments</li><li>Recruits and trains volunteer coaches</li><li>Provides and maintains fields, uniforms, and equipment</li><li>Hosts tournaments and camps</li></ul>
<h3>Our history</h3>
<p>Cecil Soccer League was recognized as a 501(c)(3) tax-exempt organization in 1991. In 2002 the league entered a long-term lease and management agreement with Cecil County to plan, build, maintain, and operate the soccer facilities at Chesland Park, which became the Chesland Soccer Complex. Volunteers have built and cared for the complex ever since.</p></div>
<div class="panel"><h3>Organization details</h3><dl>
<dt>Legal name</dt><dd>Cecil Soccer League, Inc.</dd>
<dt>Program name</dt><dd>Cecil FC</dd>
<dt>Type</dt><dd>Maryland nonprofit corporation</dd>
<dt>Tax status</dt><dd>501(c)(3) tax-exempt</dd>
<dt>EIN</dt><dd>52-1311485</dd>
<dt>Physical address</dt><dd>Chesland Soccer Complex<br>401 Elk Forest Rd<br>Elkton, MD 21921</dd>
<dt>Mailing address</dt><dd>P.O. Box 1406<br>Elkton, MD 21922-1406</dd>
<dt>Participants</dt><dd>About 1,200 per year</dd>
<dt>Websites</dt><dd><a href="{CSL}/">cecilsoccer.org</a><br>cecilfc.org</dd>
</dl></div></div></section>
<section><div class="wrap grid two">
<div><h2>Refund policy</h2>
<p>At Cecil Soccer League it is our goal to provide the best soccer experience possible. We understand that situations occur after a player registers where the player is unable to participate due to financial, medical, or personal conflicts.</p>
<ul class="clean">
<li>All refund requests must be made in writing by email to <a href="mailto:info@cecilsoccer.org">info@cecilsoccer.org</a>. Include the player&rsquo;s name and date of birth, the registering parent&rsquo;s name, email, and phone, and the reason for the request.</li>
<li>All refunds are subject to a $10 processing fee per player.</li>
<li>Requests received before open registration closes are considered for up to 100% of the registration fee, less the fee.</li>
<li>Requests received after registration closes but before opening day are considered for up to 50%, less the fee.</li>
<li>No refunds after the first game of the season. Special circumstances (injury, a move, etc.) are considered case by case.</li>
<li>No refunds for not being placed on a requested team, or because practice times or locations are inconvenient.</li>
</ul>
<p>The Executive Board reviews each request and provides a resolution.</p></div>
<div><h2>Check policy</h2>
<p>By paying with a check, you agree that if your check is dishonored or returned for any reason, you authorize us to re-present it electronically (or by paper draft) to your bank for the amount of the check plus any fees permitted by state law.</p>
<p>Checks can be mailed to:<br><strong>Cecil Soccer League, Inc.<br>P.O. Box 1406<br>Elkton, MD 21922-1406</strong></p>
<figure style="margin-top:1.4rem"><img class="shot" src="img/chesland-cleanup.jpg" alt="Volunteers and players at a Chesland Soccer Complex cleanup day" loading="lazy"><figcaption>Volunteers at a Chesland cleanup day.</figcaption></figure></div>
</div></section>""", sub="An established, volunteer-run youth soccer league in Cecil County, Maryland.")

PROGRAMS = shell("programs.html", "Programs",
    "Recreational, competitive (travel), and winter indoor youth soccer programs of Cecil Soccer League, Inc., plus the John Jones Memorial College Scholarship.",
    f"""
<section id="rec"><div class="wrap grid two-w">
<div><h2>Recreational soccer</h2>
<p>The Recreational Program is geared toward providing a fun, competitive, and safe soccer environment for kids. All kids are welcome, and the league strives to make it a positive experience for players and their families.</p>
<p>Winning is not the #1 goal, and there are no playoffs. Coaches and parents are encouraged to teach good sportsmanship, self-reliance, and teamwork. The emphasis is on participation and on improving skills, coordination, and strategy: fun first.</p>
<h3>Seasons</h3>
<ul class="clean"><li><strong>Fall:</strong> 8-game season at Chesland, September to early November. Fall 2026 runs September 12 &ndash; November 7.</li><li><strong>Spring:</strong> 8 games over 7 weeks at Chesland, April to May. Registration opens in early February.</li></ul>
<h3>Registration pricing</h3>
<table><thead><tr><th>Window</th><th>Price</th></tr></thead><tbody><tr><td>Early bird</td><td>$99</td></tr><tr><td>Regular</td><td>$109</td></tr><tr><td>Late</td><td>$124</td></tr></tbody></table>
<h3>Divisions</h3>
<p>U3/4, U5/6, U7/8, U9/10, U11/12, U13/14, and a High School division. U3&ndash;U6 play weekend games only; U7/8 and up have weekly practices.</p>
<h3>Equipment</h3>
<ul class="clean"><li>Red/white Cecil Soccer recreational jersey (order through Soccer.com or on site at Chesland)</li><li>Shin pads covered by soccer socks; black shorts recommended</li><li>Soccer cleats or athletic shoes (no boots or sandals)</li><li>No jewelry during games</li></ul>
{COACH}
<div class="btns" style="margin-top:1.2rem"><a class="btn red" href="{CSL}/recreation-csl/fall-rec/">Fall rec details</a><a class="btn red" href="{CSL}/recreation-csl/spring-rec/">Spring rec details</a></div></div>
<figure><img class="shot" src="img/fall-rec-2026.jpg" alt="Fall 2026 Rec Soccer flyer: season September 12 to November 7, boys and girls ages U4 to U17" loading="lazy"><figcaption>Fall 2026 recreational season flyer.</figcaption></figure>
</div></section>
<section id="travel"><div class="wrap grid two-w">
<div><h2>Competitive (travel) soccer</h2>
<img class="shot" src="img/club-header.jpg" alt="Cecil Soccer Club Competitive Soccer banner" loading="lazy" style="margin-bottom:1rem">
<p>The Cecil FC competitive program fields travel teams starting at U9 and continuing through our high school program. Travel coaches are trained and hold licenses through US Youth Soccer.</p>
<p>Playing competitive soccer creates an environment that lets players compete at the highest levels of high school and potentially at the collegiate level.</p>
<h3>Tryouts</h3>
<p>We offer an affordable, fun, and competitive soccer environment where players can develop their skills and love for the game. Tryouts are held each spring at the Chesland Soccer Complex for the following season, with separate boys and girls sessions. Starting in fall 2026, Cecil FC follows the age group chart shown here.</p>
<p>Interested in coaching? Email <a href="mailto:info@cecilsoccer.org">info@cecilsoccer.org</a>.</p>
<div class="btns" style="margin-top:1rem"><a class="btn red" href="{CSL}/competitive-csl/tryout-info-2/">Tryout information</a><a class="btn red" href="{CSL}/competitive-csl/coaching-staff-2/">Coaching staff</a></div></div>
<figure><img class="shot" src="img/age-chart-2627.jpg" alt="Cecil FC 2026/27 travel season age group chart, U8 through U19 by birth date range" loading="lazy"><figcaption>2026/27 travel season age group chart.</figcaption></figure>
</div></section>
<section id="indoor"><div class="wrap grid two-w">
<div><h2>Winter indoor rec</h2>
<p>A games-only indoor season at the <strong>Cecil Arena</strong>, 2706 North East Rd, North East, MD 21901. There are no practices during winter rec.</p>
<dl style="margin:1rem 0"><dt>Season</dt><dd>January 2 &ndash; February 27, 2027</dd><dt>Divisions</dt><dd>U6 coed, then boys and girls divisions from U8 to U18</dd><dt>Regular</dt><dd>$90 (October 14 &ndash; November 30)</dd><dt>Late</dt><dd>$110 (December 1 &ndash; December 11)</dd></dl>
<p><strong>Uniforms:</strong> U4/U6 players receive team t-shirts. U8 and older wear red and white Adidas jerseys ordered through Soccer.com; red/white reversible jerseys from prior seasons are allowed. Allow at least two weeks for delivery.</p>
<div class="btns"><a class="btn primary" href="{CSL}/recreation-csl/winter-indoor-rec/">Register for winter indoor</a></div></div>
<figure><img class="shot" src="img/cecil-arena.jpg" alt="Exterior of the Cecil Arena indoor facility" loading="lazy"><figcaption>The Cecil Arena, home of winter indoor soccer.</figcaption></figure>
</div></section>
<section id="scholarship"><div class="wrap grid two">
<figure><img class="shot" src="img/john-jones.jpg" alt="Cecil FC John Jones Memorial Scholarship banner" loading="lazy"></figure>
<div><h2>John Jones Memorial College Scholarship</h2>
<p>John Jones was instrumental in the development and construction of the Chesland Soccer Complex and the Bard Cameron Sports Park. His faithful and selfless contributions to youth sports in Cecil County exemplify the meaning of volunteering and community service. John passed away in the summer of 2016.</p>
<p>Cecil Soccer awards two <strong>$1,500 scholarships</strong> in John&rsquo;s name to graduating seniors who best exemplify the spirit of community service, academic excellence, and good sportsmanship. Applicants must plan to attend college after graduation.</p>
<p><a href="{CSL}/more/john-jones-memorial-college-scholarship-2/">Instructions and application &rarr;</a></p></div>
</div></section>
<section><div class="wrap"><h2>Coaches and referees</h2>
<p>All coaches are volunteers. The league supports coach education and licensing and encourages older players to become certified referees. See the <a href="{CSL}/more/coachs-corner/">Coach&rsquo;s Corner</a> and <a href="{CSL}/more/referee-corner/">Referee Corner</a> on cecilsoccer.org.</p></div></section>""",
    sub="Recreational, competitive, and winter indoor soccer for players ages 4 to 18.")

TOURN = shell("tournaments.html", "Tournaments",
    "Tournaments hosted by Cecil FC at the Chesland Soccer Complex: the Chesapeake Cup and the Cecil Fall Blast.",
    f"""
<section id="fall-blast"><div class="wrap grid two-w">
<div><span class="badge">Application deadline October 26, 2026</span><h2 style="margin-top:.6rem">18th Annual Cecil Fall Blast</h2>
<dl style="margin:1rem 0">
<dt>Dates</dt><dd>November 14, 2026 (boys) &middot; November 15, 2026 (girls)</dd>
<dt>Format</dt><dd>One-day tournament, three games guaranteed</dd>
<dt>Age groups</dt><dd>U8&ndash;U16 boys and girls (mixed teams accepted in boys divisions)</dd>
<dt>Cost</dt><dd>$650 (U8&ndash;U10) &middot; $725 (U11&ndash;U16)<br>$50 per team discount for any club sending 5 teams</dd>
<dt>Small-sided</dt><dd>U8&ndash;U10 play 7v7; U11&ndash;U12 play 9v9</dd>
</dl>
<p>The Tournament Committee reserves the right to combine age groups if appropriate.</p>
<div class="btns"><a class="btn red" href="{CSL}/tournaments/fall-blast-3/">Register and documents</a></div></div>
<figure><img src="img/fall-blast-logo.jpg" alt="2026 Cecil Fall Blast logo, hosted by Cecil Football Club" loading="lazy" style="max-width:380px;margin:0 auto"></figure>
</div></section>
<section id="chesapeake-cup"><div class="wrap grid two-w">
<div><h2>Chesapeake Cup</h2>
<p>Cecil FC&rsquo;s spring tournament, now in its 31st year, is a one-day GotSport event with three games guaranteed for U8&ndash;U16 boys and girls teams. The 2026 Cup was played April 4, 2026.</p>
<dl style="margin:1rem 0">
<dt>Cost (2026)</dt><dd>$650 (U8&ndash;U10) &middot; $725 (U11&ndash;U16)<br>$50 per team discount for any club sending 5 teams</dd>
<dt>Guest players</dt><dd>Up to five per team, within the age group&rsquo;s roster maximum</dd>
<dt>Fields</dt><dd>Chesland Soccer Complex and Bo Manor</dd>
</dl>
<div class="btns"><a class="btn red" href="{CSL}/tournaments/chesapeake-cup/">Chesapeake Cup page</a></div></div>
<figure><img class="shot" src="img/chesapeake-cup-photo.jpg" alt="31st Annual Chesapeake Cup 2026 flyer" loading="lazy"><figcaption>31st Annual Chesapeake Cup flyer.</figcaption></figure>
</div></section>
<section><div class="wrap"><div class="callout"><h3>Tournament contact</h3><p>Questions about Cecil FC tournaments? Email <a href="mailto:info@cecilsoccer.org">info@cecilsoccer.org</a> or call <a href="tel:+14106707347">(410) 670-7347</a>.</p></div></div></section>""",
    sub="Cecil FC hosts two tournaments a year at the Chesland Soccer Complex.")

FIELDS = shell("fields.html", "Fields",
    "Chesland Soccer Complex, 401 Elk Forest Rd, Elkton, MD (home fields of Cecil Soccer League, Inc.) and the Cecil Arena in North East, MD.",
    f"""
<section><div class="wrap grid two-w">
<div><h2>Chesland Soccer Complex</h2>
<p><strong>401 Elk Forest Rd, Elkton, MD 21921</strong></p>
<p>Outdoor rec soccer and home travel soccer games are played at the Chesland Soccer Complex. It is the league&rsquo;s home field and physical location, within Cecil County&rsquo;s Chesland Park. Under a 2002 lease and management agreement with Cecil County, Cecil Soccer League plans, maintains, and operates the soccer facilities on about 88 acres of the park.</p>
<div class="btns" style="margin-top:1rem"><a class="btn red" href="{MAPS_CHES}">Directions (Google Maps)</a></div></div>
<div class="panel"><h3>Visiting Chesland</h3><dl>
<dt>Address</dt><dd>{PHYS}</dd>
<dt>Owner</dt><dd>Cecil County, Maryland</dd>
<dt>Operator</dt><dd>Cecil Soccer League, Inc.</dd>
<dt>Used for</dt><dd>Spring and fall rec, home travel games, tournaments</dd>
</dl></div></div></section>
<section><div class="wrap"><h2>Chesland field map</h2>
<figure><a href="img/chesland-field-map.jpg"><img class="shot" src="img/chesland-field-map.jpg" alt="Aerial field map of the Chesland Soccer Complex showing numbered fields, the barn, parking, trash cans, and first aid" loading="lazy"></a><figcaption>Chesland Soccer Complex field map. Select the map to open it full size.</figcaption></figure></div></section>
<section><div class="wrap grid two">
<figure><img class="shot" src="img/cecil-arena.jpg" alt="Exterior of the Cecil Arena" loading="lazy"></figure>
<div><h2>Cecil Arena</h2><p><strong>2706 North East Road, North East, MD 21901</strong></p><p>Indoor winter rec soccer and indoor travel soccer games are held at the Cecil Arena.</p><div class="btns" style="margin-top:1rem"><a class="btn red" href="{MAPS_ARENA}">Directions (Google Maps)</a></div></div>
</div></section>""",
    sub="Where Cecil FC plays: Chesland Soccer Complex in Elkton and the Cecil Arena in North East.")

PHOTOS = [
    ("fire-presidents-cup.jpg", "Cecil Fire players and coaches holding the Presidents Cup trophy and banner", "Cecil Fire, Presidents Cup champions"),
    ("express-champs.jpg", "Cecil Express girls team with trophy and team banner", "Cecil Express, Spirit United 2015 champions"),
    ("express-indoor-champs.jpg", "Cecil Express players with medals after the Kirkwood indoor league", "Cecil Express, 1st place in the 2015 Kirkwood Soccer Club competitive indoor league (U12)"),
    ("rebels-union-escorts.jpg", "Young Cecil players on the field with Philadelphia Union players before a match", "U9 Cecil Rebels as player escorts for the Philadelphia Union at the Lamar Hunt US Open Cup"),
    ("union-night.jpg", "Cecil Soccer families on the field at the Philadelphia Union stadium", "Cecil Soccer Night with the Philadelphia Union"),
    ("chesland-cleanup.jpg", "Volunteers and players at a Chesland cleanup day", "Chesland cleanup day volunteers"),
]

PHOTOS_PAGE = shell("photos.html", "Photos",
    "Photos of Cecil FC teams, volunteers, and events.",
    f"""
<section><div class="wrap"><h2>Cecil FC through the years</h2>
<div class="gallery">{"".join(f'<figure><img src="img/{f}" alt="{a}" loading="lazy"><figcaption>{c}</figcaption></figure>' for f, a, c in PHOTOS)}</div>
<p style="margin-top:1.6rem">More photos are on the <a href="{CSL}/more/pictures/">cecilsoccer.org pictures page</a>, <a href="https://www.facebook.com/CecilSoccer/">Facebook</a>, and <a href="https://www.instagram.com/cecilsoccer/">Instagram</a>.</p></div></section>""",
    sub="Teams, volunteers, and special events from around the league.")

GOV = shell("governance.html", "Governance",
    "Governance of Cecil Soccer League, Inc.: board of directors, bylaws, affiliations, and nonprofit status.",
    """
<section><div class="wrap grid two-w">
<div><h2>Board of Directors</h2>
<p>Cecil Soccer League, Inc. is governed by a volunteer Board of Directors under the league's bylaws. The board sets policy, approves budgets, oversees the league's finances and facilities, and elects the league's officers.</p>
<h3>Officers and directors</h3>
<div class="tablewrap"><table><thead><tr><th>Position</th><th>Name</th></tr></thead><tbody>
<tr><th colspan="2">Executive Board</th></tr>
<tr><td>President</td><td>Chris Smith</td></tr>
<tr><td>Vice President &amp; Director of Travel Soccer</td><td>Don Dzedzy</td></tr>
<tr><td>Vice President &amp; Director of Recreational Soccer</td><td>Jen Casto</td></tr>
<tr><td>Treasurer</td><td>Jeff Brizuela</td></tr>
<tr><td>Secretary</td><td>Wade Harvey</td></tr>
<tr><td>Director of Coaching</td><td>Sam Jones</td></tr>
<tr><th colspan="2">Voting Board Directors</th></tr>
<tr><td>Director of Facilities (Chesland Operations)</td><td>Sean Durgin</td></tr>
<tr><td>Equipment Manager</td><td>Heather Jones</td></tr>
<tr><td>Director of Marketing</td><td>Amy Sley</td></tr>
<tr><td>Tournament Directors</td><td>Jeff Privett and Ed Valladares</td></tr>
<tr><td>Field Manager</td><td>Dan Dekowski</td></tr>
<tr><td>Registrar</td><td><em>Vacant</em></td></tr>
</tbody></table></div>
<p class="cite">Officers and directors as elected at the October 11, 2026 board meeting.</p>
<p>Contact the board at <a href="mailto:board@cecilsoccer.org">board@cecilsoccer.org</a>.</p></div>
<div class="panel"><h3>Nonprofit status</h3><dl>
<dt>Organization</dt><dd>Cecil Soccer League, Inc.</dd>
<dt>IRS status</dt><dd>501(c)(3) public charity</dd>
<dt>EIN</dt><dd>52-1311485</dd>
<dt>Annual filing</dt><dd>IRS Form 990</dd>
<dt>Physical address</dt><dd>401 Elk Forest Rd, Elkton, MD 21921</dd>
</dl></div></div></section>
<section><div class="wrap"><h2>Affiliations</h2>
<p>Cecil Soccer League is a member of the <strong>Maryland State Youth Soccer Association (MSYSA)</strong>, <strong>US Youth Soccer</strong>, and the <strong>United States Soccer Federation</strong>, and follows their rules and policies. All games are played under FIFA Laws of the Game as modified by US Youth Soccer, MSYSA, and Cecil Soccer.</p></div></section>
<section><div class="wrap"><h2>Policies</h2>
<ul class="clean"><li><strong>Non-discrimination:</strong> the league does not discriminate on the basis of race, ethnic origin, age, religion, sex, or disability in its membership, board, committees, staff, or participants.</li><li><strong>Bylaws:</strong> the league is governed by bylaws adopted by its Board of Directors.</li><li><strong>Sideline conduct:</strong> coaches are expected to control their players and sidelines. Abusive or disrespectful behavior is not tolerated and can lead to suspension or expulsion.</li><li><strong>Refunds:</strong> see the <a href="about.html">refund policy</a>.</li></ul></div></section>""",
    sub="How Cecil Soccer League, Inc. is organized and governed.")

CONTACT = shell("contact.html", "Contact",
    "Contact Cecil Soccer League, Inc. (Cecil FC): addresses, email, phone, and hours.",
    f"""
<section><div class="wrap grid three">
<div class="panel"><h3>Physical address</h3><p>Chesland Soccer Complex<br>401 Elk Forest Rd<br>Elkton, MD 21921</p><p><a href="{MAPS_CHES}">Directions &rarr;</a></p></div>
<div class="panel"><h3>Mailing address</h3><p>Cecil Soccer League, Inc.<br>P.O. Box 1406<br>Elkton, MD 21922-1406</p></div>
<div class="panel"><h3>Phone &amp; email</h3><p><a href="tel:+14106707347">(410) 670-7347</a><br>Monday &ndash; Friday, 9:00 AM &ndash; 8:00 PM ET</p><p>General: <a href="mailto:info@cecilsoccer.org">info@cecilsoccer.org</a><br>Board: <a href="mailto:board@cecilsoccer.org">board@cecilsoccer.org</a></p></div>
</div></section>
<section><div class="wrap grid two">
<div><h2>Stay connected</h2><p>Subscribe to receive all program updates: registration openings, schedules, and field news.</p><div class="btns"><a class="btn primary" href="http://eepurl.com/ghSJK9">Join the mailing list</a></div><p style="margin-top:1rem">Follow us on <a href="https://www.facebook.com/CecilSoccer/">Facebook</a> and <a href="https://www.instagram.com/cecilsoccer/">Instagram</a>.</p></div>
<div><h2>Sponsor Cecil FC</h2><p>We are always looking to partner with local businesses. Email <a href="mailto:info@cecilsoccer.org">info@cecilsoccer.org</a> to learn about sponsorship.</p><h3>Registration questions</h3><p>Registration, schedules, and team pages are on our main website, <a href="{CSL}/">cecilsoccer.org</a>.</p></div>
</div></section>""",
    sub="We&rsquo;d love to hear from you.")

(ROOT / "style.css").write_text(CSS)
OUT = [("index.html", HOME), ("about.html", ABOUT), ("programs.html", PROGRAMS), ("tournaments.html", TOURN),
       ("fields.html", FIELDS), ("photos.html", PHOTOS_PAGE), ("governance.html", GOV), ("contact.html", CONTACT)]
for name, html in OUT:
    (ROOT / name).write_text(html)
print("built", len(OUT), "pages")
