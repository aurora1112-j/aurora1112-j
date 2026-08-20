#!/usr/bin/env python3
"""Generate the light and dark profile cards."""

from __future__ import annotations

from html import escape
from pathlib import Path


USERNAME = "aurora1112-j"
ROOT = Path(__file__).resolve().parent

# Edit these lines to make the card more personal. Keep values concise so they fit.
PROFILE = {
    "name": "CHENXI HUANG",
    "role": "AI Product Manager & Designer",
    "study": "Nanjing University",
    "explore": "AI agents · memory · knowledge management",
    "build": "Astro · TypeScript · React · MDX",
    "email": "hcx0579@qq.com",
    "x_handle": "Aurora736951",
    "website": "aurora1112-j.github.io",
    "projects": [
        ("vesti", "Vesti", "Local-first AI memory & knowledge hub"),
        ("aurora1112-j.github.io", "Botanical Systems", "Ideas, systems & photography"),
    ],
}


ASCII_ART = """\
░▒▒▒░▒▓▓▓▒▒▓████▓▓▓▓▓▓▓▒▒▒░░░░░░▒▒▒▓▒▓▓▓▓▓
░░░▒▒▓▓▒▓▒▒▓███▓▓▓▒▒▒▒░░░░░░░░░░░░░▒▒▒▒▒▓█
░░░░▒▓▒▒▓▓▓▓███▓▒░▒░░░░░░░░░░░░░░░░░▒▒▒▒▒▓
░░░░▒▒▒▒▓▒▒▒▓▓▓▒░░░░░░░░░░░░░░░░░░░░░▒░▒▒▒
░░░▒▒▒▒▒▓▓▒▒▓▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒░▒
▒░▒▒▒▒░▒▓▒▒▓▓▒▒▒░▒░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒▒▒▓▓▒▒▓▓▒▓▓▓▓▒▒▓▒░░░░░░░░░░░░░░░░░░░░
▓▒▒▒▒▒▒▓▒▒▓▒▓▓▓▒▒▒▒▓▓▓▓▒░░░░░░░░░░░░░░░░░░
▒▒▒▒▒▒▒▒▓█▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░
▒▒▒▒▒▒▓▓█▓▓▓██▓██▓▓▓▓▓▒▒▒░░░░░░░░▒▒▒▒▒▒▒░░
▒▒▓▓▓████▓▓▒▓▓▒▓▓▓▒▒▒▓░░▒▒░░░▒░░▒▒▒▓▓▓▓██▓
▓████████▓▒▒▒▓▒▒▒░░▒▓▓░░▒░░░░▒▒░░▒▒▒▒▒░░▒▒
▓▓▓▓██▓█▓▓▒▒▒▒▓▓▒▒░░░░░░░░░░░▒▒░░▒▒▓█▓▒▒░░
▓▓▓██▓▓█▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░▒▓▓▓▓▓▓▒▓▓
▓▓█▓▓▓▓▓▒▒▓▒▒▒▒▒▒░░░░░░░░░░░▒░░░░▒░▒▓▒░░▒▓
▒▓█▓▓██▓▒▒▓▒▒▒▒▒▒░░░░▒▒▒░░▒▒▒▒░░░░░▒▒░▒▒▒▒
▓▓██▓▓██▒▒▒▒▒▒▒░░░░░▒▓▒▒░░▒▒▒▒░░░░░░▒▒▒▒▓▒
█▓██████▓▒▒▒▒▒▒░░░░░▓▒▓▓▒▒▓▓▓▓░░░░░░░░▒▒░░
▓▓▓█████▓▒▒▒░░░░░░░░▒▒▒▒▒▓█▒▒▓▒░░░░░▒▒▒▒▒▒
▓█▓██████▒▒░░░░░░░░░░░░░░░▒▒▒▒░░░░░▒▒▒▒▒▒▒
▓▓▓██████▒░░░░░░░░▒▒▓▓▒▒▒░░░░░░░░░▒▒▒▒▒▒▒▒
▓▓▓▓██████▒░░░░░▒▓▓▓▓▓▓▓▓▒▒░░░░░░░▒░░▒▒░▒▒
▒▓▓▒▓▓█████▒░░░░░▒▒▒▒▓▓▓▓▓▓▒░░░░░░░░▒▒░░▒▒
▓▓▓▒▓▓▓▓▓▓▓▒░▒░░░░▒▒▒▒▒▓▒▒▓▓▒░░░░░░░░░░░▒▒
▓▒▓▓▒▒▒▓▓▒▒▓▓▒▒▒▒░░░▒▓▒▒▒▒▒░░░░░░░░░░░░░▒▒
▓▓▓▓▓▒▒▒▒▓▒▒▓█▓▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▓█"""


THEMES = {
    "light": {
        "bg": "#f6f8fa",
        "panel": "#fbfcfd",
        "text": "#3d4857",
        "muted": "#8a95a5",
        "line": "#dde2e8",
        "key": "#68788c",
        "accent": "#69769a",
        "art1": "#668f96",
        "art2": "#9bafb5",
        "art3": "#9891ad",
    },
    "dark": {
        "bg": "#151a22",
        "panel": "#1b222d",
        "text": "#d9e0e8",
        "muted": "#7f8b9d",
        "line": "#303947",
        "key": "#a1afc0",
        "accent": "#a2a9c5",
        "art1": "#5f838a",
        "art2": "#899da3",
        "art3": "#8d879f",
    },
}


def art() -> str:
    lines = []
    for index, line in enumerate(ASCII_ART.splitlines()):
        lines.append(
            f'<tspan x="38" y="{102 + index * 14.6:.1f}">{escape(line)}</tspan>'
        )
    return "\n".join(lines)


def row(y: int, label: str, value: str) -> str:
    return (
        f'<text x="468" y="{y}" class="row">'
        f'<tspan class="key">{escape(label):<11}</tspan>'
        f'<tspan class="value">{escape(value)}</tspan></text>'
    )


def detail_row(y: int, namespace: str, kind: str, value: str) -> str:
    label = f"{namespace}.{kind}"
    line_start = 468 + len(label) * 8.5 + 14
    return f'''<g>
      <text x="468" y="{y}" class="row"><tspan class="key">{escape(namespace)}</tspan>.<tspan class="key">{escape(kind)}</tspan>:</text>
      <line x1="{line_start:.1f}" y1="{y - 5}" x2="704" y2="{y - 5}" class="leader"/>
      <text x="716" y="{y}" class="value detail">{escape(value)}</text>
    </g>'''


def project(y: int, index: int, slug: str, name: str, description: str) -> str:
    url = f"https://github.com/{USERNAME}/{slug}"
    return f'''<a href="{escape(url)}">
      <text x="468" y="{y}" class="project">
        <tspan class="index">{index:02d}</tspan>
        <tspan dx="14" class="accent">{escape(name)}</tspan>
        <tspan dx="12" class="muted">— {escape(description)}</tspan>
      </text>
    </a>'''


def render(theme_name: str) -> str:
    c = THEMES[theme_name]
    projects = "\n".join(
        project(451 + index * 28, index, slug, name, description)
        for index, (slug, name, description) in enumerate(PROFILE["projects"], start=1)
    )
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1120" height="620" viewBox="0 0 1120 620" role="img" aria-labelledby="title desc">
  <title id="title">{escape(PROFILE["name"])} — GitHub profile</title>
  <desc id="desc">Terminal-style profile card with an ASCII portrait, interests, selected work and contact links.</desc>
  <defs>
    <linearGradient id="portrait" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c['art1']}"/>
      <stop offset="0.55" stop-color="{c['art2']}"/>
      <stop offset="1" stop-color="{c['art3']}"/>
    </linearGradient>
  </defs>
  <style>
    text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace; fill: {c['text']}; }}
    .ascii {{ white-space: pre; font-size: 15px; font-weight: 700; fill: url(#portrait); }}
    .eyebrow {{ font-size: 14px; letter-spacing: 1.8px; fill: {c['muted']}; }}
    .title {{ font-size: 27px; font-weight: 700; fill: {c['text']}; }}
    .subtitle {{ font-size: 15px; fill: {c['accent']}; }}
    .section {{ font-size: 14px; letter-spacing: 1.4px; fill: {c['muted']}; }}
    .row {{ font-size: 15px; }}
    .key {{ fill: {c['key']}; font-weight: 700; }}
    .value {{ fill: {c['text']}; }}
    .project {{ font-size: 14px; }}
    .index {{ fill: {c['key']}; font-weight: 700; }}
    .accent {{ fill: {c['accent']}; font-weight: 700; }}
    .muted {{ fill: {c['muted']}; }}
    .link {{ fill: {c['accent']}; font-size: 14px; }}
    .detail {{ font-size: 14px; }}
    .leader {{ stroke: {c['line']}; stroke-width: 3; stroke-dasharray: 2 7; }}
  </style>
  <rect width="1120" height="620" rx="22" fill="{c['bg']}"/>
  <rect x="24" y="24" width="400" height="572" rx="18" fill="{c['panel']}" stroke="{c['line']}"/>
  <text class="ascii">{art()}</text>
  <text x="468" y="48" class="eyebrow">{USERNAME.upper()} / PROFILE</text>
  <text x="468" y="82" class="title">{escape(PROFILE['name'])}</text>
  <text x="468" y="108" class="subtitle">{escape(PROFILE['role'])}</text>
  <line x1="468" y1="131" x2="1068" y2="131" stroke="{c['line']}"/>
  {row(160, 'Study', PROFILE['study'])}
  {row(188, 'Explore', PROFILE['explore'])}
  {row(216, 'Build', PROFILE['build'])}
  <text x="468" y="248" class="section">LANGUAGES ─────────────────────────────────</text>
  {detail_row(276, 'Languages', 'Programming', 'TypeScript · JavaScript · Python')}
  {detail_row(304, 'Languages', 'Web', 'Astro · React · HTML · CSS')}
  {detail_row(332, 'Languages', 'Real', 'Chinese · English')}
  <text x="468" y="365" class="section">HOBBIES ───────────────────────────────────</text>
  {detail_row(393, 'Hobbies', 'Outdoor', 'Rock climbing')}
  {detail_row(421, 'Hobbies', 'Creative', 'Photography')}
  <text x="468" y="449" class="section">SELECTED WORK ─────────────────────────────</text>
  {projects}
  <text x="468" y="532" class="section">CONTACT ───────────────────────────────────</text>
  <a href="mailto:{escape(PROFILE['email'])}"><text x="468" y="554" class="row"><tspan class="key">Email</tspan>: <tspan class="link">{escape(PROFILE['email'])}</tspan></text></a>
  <a href="https://x.com/{escape(PROFILE['x_handle'])}"><text x="468" y="576" class="row"><tspan class="key">X</tspan>: <tspan class="link">@{escape(PROFILE['x_handle'])}</tspan></text></a>
  <a href="https://{escape(PROFILE['website'])}"><text x="468" y="598" class="row"><tspan class="key">Web</tspan>: <tspan class="link">{escape(PROFILE['website'])}</tspan></text></a>
  <text x="38" y="570" class="eyebrow">PORTRAIT / TERMINAL EDITION</text>
</svg>
'''


def main() -> None:
    for name in THEMES:
        (ROOT / f"{name}_mode.svg").write_text(render(name), encoding="utf-8")
    print("Generated light_mode.svg and dark_mode.svg")


if __name__ == "__main__":
    main()
