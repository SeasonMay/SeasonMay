"""Render profile cards from public GitHub data; no third-party statistics API."""
import json
import os
from collections import Counter
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1] / 'profile'
ROOT.mkdir(exist_ok=True)
USER = 'SeasonMay'

def get(path):
    headers = {'User-Agent': 'SeasonMay-profile', 'Accept': 'application/vnd.github+json'}
    if os.getenv('GH_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GH_TOKEN']
    with urlopen(Request('https://api.github.com/' + path, headers=headers), timeout=30) as response:
        return json.load(response)

def card(name, width, height, body):
    (ROOT / name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><rect x="1" y="1" width="{width-2}" height="{height-2}" rx="12" fill="#1a1b27" stroke="#30344b"/><g font-family="Segoe UI,Arial,sans-serif">{body}</g></svg>', encoding='utf-8')

def text(x, y, value, color='#a9b1d6', size=14, weight=400):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}">{escape(str(value))}</text>'

repos = []
for page in range(1, 100):
    batch = get(f'users/{USER}/repos?type=owner&per_page=100&page={page}')
    repos.extend(r for r in batch if not r['private'])
    if len(batch) < 100:
        break
owned = [r for r in repos if not r['fork']]
prs = get(f'search/issues?q=author%3A{USER}+is%3Apr+is%3Apublic&per_page=1')['total_count']
issues = get(f'search/issues?q=author%3A{USER}+is%3Aissue+is%3Apublic&per_page=1')['total_count']
rows = [('Public repositories', len(repos)), ('Stars on owned repos', sum(r['stargazers_count'] for r in owned)), ('Public pull requests', prs), ('Public issues', issues)]
body = text(24, 36, 'SeasonMay · GitHub Stats', '#70a5fd', 18, 600)
for i, (label, value) in enumerate(rows):
    body += text(26, 75 + i * 29, label) + text(345, 75 + i * 29, value, '#38bdae', 17, 600)
body += text(24, 200, 'PUBLIC DATA / ' + datetime.now(timezone.utc).strftime('%Y-%m-%d UTC'), '#737aa2', 10)
card('stats.svg', 405, 220, body)
languages = Counter()
for repo in owned:
    languages.update(get(f"repos/{repo['full_name']}/languages"))
total = sum(languages.values())
top = languages.most_common(5)
if len(languages) > 5:
    top.append(('Other', total - sum(n for _, n in top)))
colors = ['#70a5fd', '#38bdae', '#bb9af7', '#ff9e64', '#e0af68', '#737aa2']
body = text(24, 36, 'Most Used Languages', '#70a5fd', 18, 600)
x = 24
for i, (lang, value) in enumerate(top):
    width = 357 * value / total
    body += f'<rect x="{x:.2f}" y="57" width="{width:.2f}" height="12" fill="{colors[i]}"/>'
    x += width
    col, row = i % 2, i // 2
    body += text(24 + col * 184, 103 + row * 28, f'{lang} {value / total:.1%}', colors[i], 12)
body += text(24, 200, 'OWNED PUBLIC REPOS / BY CODE BYTES', '#737aa2', 10)
card('languages.svg', 405, 220, body)
body = text(30, 36, 'FEATURED CONTRIBUTION   /   TENCENT CLOUD', '#70a5fd', 12, 600)
body += text(30, 82, 'Agent Memory', '#c0caf5', 36, 700)
body += text(30, 116, 'Source feedback. Better context.', '#a9b1d6', 18)
for i, label in enumerate(['EVALUATE', 'LEARN', 'RETRIEVE']):
    x = 30 + i * 185
    body += f'<rect x="{x}" y="147" width="163" height="38" rx="8" fill="#24283b"/>'
    body += text(x + 20, 172, label, ['#70a5fd', '#bb9af7', '#38bdae'][i], 13, 600)
    if i < 2:
        body += text(x + 168, 172, '›', '#737aa2', 18)
body += '<circle cx="705" cy="108" r="62" fill="none" stroke="#30344b"/><circle cx="705" cy="108" r="42" fill="none" stroke="#70a5fd" stroke-dasharray="4 7"/><path d="M665 80L731 76L745 125L685 143Z M665 80L745 125 M731 76L685 143" fill="none" stroke="#bb9af7" stroke-opacity=".7"/>'
for x, y in [(665, 80), (731, 76), (745, 125), (685, 143)]:
    body += f'<circle cx="{x}" cy="{y}" r="6" fill="#38bdae"/>'
card('memory.svg', 840, 216, body)
print('Generated public-data statistics and featured card.')
