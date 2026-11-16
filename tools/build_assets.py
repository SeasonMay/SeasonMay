"""Generate original, self-contained SVG artwork for the profile."""
from pathlib import Path
from html import escape

assets = Path(__file__).resolve().parents[1] / "assets"
FONT = 'font-family="Segoe UI,Arial,sans-serif"'
MONO = 'font-family="Consolas,monospace"'

def save(name, width, height, body):
    (assets / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">{body}</svg>', encoding="utf-8")

save("header.svg", 1000, 460, f'''
<title>SeasonMay — AI, Systems, Open Source</title>
<defs>
 <linearGradient id="edge"><stop stop-color="#22d3ee"/><stop offset=".5" stop-color="#a78bfa"/><stop offset="1" stop-color="#fb7185"/></linearGradient>
 <radialGradient id="halo"><stop stop-color="#6d28d9" stop-opacity=".5"/><stop offset="1" stop-color="#090e20" stop-opacity="0"/></radialGradient>
 <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#94a3b8" stroke-opacity=".06"/></pattern>
</defs>
<style>
 @keyframes orbit{{to{{transform:rotate(360deg)}}}}
 @keyframes blink{{50%{{opacity:0}}}}
 @keyframes breathe{{50%{{opacity:.35}}}}
 .orbit{{transform-origin:790px 172px;animation:orbit 24s linear infinite}}
 .cursor{{animation:blink 1.2s steps(1) infinite}}
 .pulse{{animation:breathe 4s ease-in-out infinite}}
 @media(prefers-reduced-motion:reduce){{.orbit,.cursor,.pulse{{animation:none}}}}
</style>
<rect x="1" y="1" width="998" height="458" rx="24" fill="#090e20" stroke="#293250"/>
<rect x="1" y="1" width="998" height="458" rx="24" fill="url(#grid)"/>
<ellipse cx="800" cy="170" rx="290" ry="240" fill="url(#halo)"/>
<path d="M26 1H974" stroke="url(#edge)" stroke-width="3"/>
<text x="48" y="48" fill="#22d3ee" {MONO} font-size="12" letter-spacing="3">SEASONMAY / PERSONAL SPACE</text>
<circle cx="932" cy="44" r="4" fill="#34d399" class="pulse"/>
<text x="48" y="142" fill="#f8fafc" {FONT} font-size="76" font-weight="800" letter-spacing="-4">SeasonMay<tspan fill="#22d3ee">.</tspan></text>
<text x="51" y="183" fill="#b5bfd5" {FONT} font-size="20">Curiosity into code. Ideas into experiments.</text>
<g {MONO} font-size="11" letter-spacing="1">
 <rect x="50" y="209" width="112" height="28" rx="14" fill="#103341"/><text x="68" y="227" fill="#67e8f9">AI SYSTEMS</text>
 <rect x="173" y="209" width="130" height="28" rx="14" fill="#282046"/><text x="188" y="227" fill="#c4b5fd">OPEN SOURCE</text>
 <rect x="314" y="209" width="136" height="28" rx="14" fill="#332136"/><text x="333" y="227" fill="#fda4af">BUILD &amp; LEARN</text>
</g>
<circle cx="790" cy="172" r="107" fill="none" stroke="#4c3f7e" stroke-width="1"/>
<circle cx="790" cy="172" r="82" fill="none" stroke="#22d3ee" stroke-opacity=".28" stroke-dasharray="3 8"/>
<g class="orbit"><ellipse cx="790" cy="172" rx="133" ry="48" fill="none" stroke="url(#edge)" stroke-width="2"/><circle cx="923" cy="172" r="6" fill="#22d3ee"/></g>
<g class="orbit" style="animation-direction:reverse;animation-duration:35s"><circle cx="790" cy="65" r="5" fill="#c4b5fd"/></g>
<rect x="741" y="123" width="98" height="98" rx="27" fill="#131a32" stroke="#a78bfa" stroke-opacity=".65"/>
<text x="790" y="185" text-anchor="middle" fill="#e9e5ff" {MONO} font-size="35" font-weight="700">S/M</text>
<rect x="48" y="272" width="904" height="148" rx="12" fill="#0c1428" stroke="#293250"/>
<path d="M48 306H952" stroke="#293250"/>
<g><circle cx="67" cy="289" r="4" fill="#fb7185"/><circle cx="82" cy="289" r="4" fill="#fbbf24"/><circle cx="97" cy="289" r="4" fill="#34d399"/></g>
<text x="500" y="293" text-anchor="middle" {MONO} font-size="11" fill="#7686a8">seasonmay@github: ~</text>
<g {MONO} font-size="15"><text x="69" y="336" fill="#67e8f9">$ whoami</text><text x="69" y="364" fill="#c9d4ea">Exploring AI applications, reliable systems &amp; open source.</text><text x="69" y="393" fill="#a78bfa">$ reproduce → understand → improve</text></g>
<rect class="cursor" x="403" y="380" width="9" height="17" fill="#a78bfa"/>
''')

save("toolkit.svg", 1000, 112, '<title>Tools used in my experiments</title>' + ''.join(
    f'<g transform="translate({10+i*166},8)"><rect width="150" height="96" rx="14" fill="#10172b" stroke="#283452"/><rect x="14" y="16" width="36" height="36" rx="10" fill="{color}" fill-opacity=".14"/><text x="32" y="41" text-anchor="middle" {MONO} font-size="16" font-weight="700" fill="{color}">{icon}</text><text x="14" y="77" {FONT} font-size="15" fill="#dce5f5">{label}</text><circle cx="129" cy="27" r="3" fill="{color}"/></g>'
    for i,(label,icon,color) in enumerate([('Python','Py','#facc15'),('Docker','Dk','#38bdf8'),('Git','&gt;_','#fb923c'),('Linux','~$','#a78bfa'),('SQLite','DB','#22d3ee'),('pytest','✓','#4ade80')])
))

for name, number, tag, title, subtitle, color, path in [
 ('sse.svg','117','EVENT DELIVERY','Recover from overflow','Slow consumers · bounded queues','#22d3ee','M38 72h24l12-16 16 31 14-15h25'),
 ('boundary.svg','118','PATH CONTAINMENT','Respect the boundary','Resolved paths · symlink checks','#a78bfa','M45 55l24-9 24 9v21q-24 28-48 0z'),
 ('filters.svg','119','DOCUMENT DISCOVERY','Keep filters consistent','Corpus paths · stable document IDs','#fb7185','M44 50h54L79 73v19H64V73z')]:
 save(name, 460, 192, f'''<title>PR #{number}: {escape(title)}</title><rect x="1" y="1" width="458" height="190" rx="17" fill="#10172b" stroke="#303c58"/><rect x="1" y="24" width="3" height="46" fill="{color}"/><path d="{path}" transform="translate(-18,-15) scale(.7)" stroke="{color}" stroke-width="2" fill="none"/><text x="85" y="38" {MONO} fill="{color}" font-size="11" letter-spacing="1">{tag}</text><text x="420" y="39" text-anchor="end" {MONO} fill="#8b9cb9" font-size="13">#{number}</text><text x="25" y="91" {FONT} font-size="24" font-weight="700" fill="#edf2fc">{title}</text><text x="25" y="123" {FONT} font-size="15" fill="#96a9c8">{subtitle}</text><path d="M25 144H435" stroke="#293650"/><text x="25" y="171" {MONO} font-size="11" fill="#a1b2cc">HUGEGRAPH AI / ONTOGENY</text><text x="430" y="172" text-anchor="end" {FONT} font-size="18" fill="{color}">↗</text>''')

save("footer.svg",1000,100,f'''<title>Keep building, keep learning</title><defs><linearGradient id="g"><stop stop-color="#22d3ee"/><stop offset=".5" stop-color="#a78bfa"/><stop offset="1" stop-color="#fb7185"/></linearGradient></defs><path d="M0 30Q250 0 500 30T1000 30" fill="none" stroke="url(#g)" stroke-opacity=".55"/><text x="500" y="72" text-anchor="middle" {MONO} font-size="13" fill="#8795b1" letter-spacing="4">ALWAYS CURIOUS. ALWAYS BUILDING.</text>''')

if __name__ == '__main__':
    import xml.etree.ElementTree as ET
    for file in assets.glob('*.svg'):
        ET.parse(file)
    print('Generated and validated SVG assets.')
