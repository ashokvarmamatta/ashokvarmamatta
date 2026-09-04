#!/usr/bin/env python3
"""
Builds README.md from TEMPLATE.md by health-checking each GitHub analytics
service and only including cards that are currently responding (HTTP 200).

Two cards only - stats and languages. The streak, summary cards, trophies,
activity graph, 3D calendar and snake were dropped: hiring managers discount
the contribution graph as gameable, and nine widgets buried the parts of the
profile that say something about the engineering.

The language card hides javascript, typescript and html - those come from
research, interest and vibe-coded repos where none of the code is mine.
"""

import urllib.request
import sys

USERNAME = "ashokvarmamatta"
EXCLUDE_REPOS = "Advance-Hearing-App"  # hidden from stats & language cards

# ── Services to check ──────────────────────────────────────────────
# Each entry: (name, test_url, markdown_block)
SERVICES = [
    (
        "stats",
        f"https://github-readme-stats-gamma-one-20.vercel.app/api?username={USERNAME}",
        None  # handled specially in ROW 1
    ),
    (
        "languages",
        f"https://github-readme-stats-gamma-one-20.vercel.app/api/top-langs/?username={USERNAME}&layout=compact",
        None  # handled specially in ROW 1
    ),
]


def check_url(url: str, timeout: int = 10) -> bool:
    """Returns True if URL responds with HTTP 200."""
    try:
        req = urllib.request.Request(url, method="HEAD")
        req.add_header("User-Agent", "readme-builder/1.0")
        resp = urllib.request.urlopen(req, timeout=timeout)
        ok = resp.status == 200
    except Exception:
        try:
            # Some services don't support HEAD, try GET
            req = urllib.request.Request(url)
            req.add_header("User-Agent", "readme-builder/1.0")
            resp = urllib.request.urlopen(req, timeout=timeout)
            ok = resp.status == 200
        except Exception:
            ok = False
    return ok


def build_analytics(alive: dict) -> str:
    """Build the GitHub Analytics markdown section from alive services."""
    parts = []

    parts.append('''<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,2,5,30&height=1&section=header" width="100%"/>
<br/>

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=22&pause=1000&color=00D4AA&center=true&vCenter=true&width=400&lines=%F0%9F%93%8A+GitHub+Analytics" alt="GitHub Analytics" />
</div>''')

    # ROW 1: Stats + Languages (side by side, or just one, or neither)
    stats_up = alive.get("stats", False)
    langs_up = alive.get("languages", False)

    if stats_up and langs_up:
        parts.append(f'''
<table align="center" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td align="center" valign="top">
      <img src="https://github-readme-stats-gamma-one-20.vercel.app/api?username={USERNAME}&show_icons=true&hide_border=true&bg_color=0d1117&title_color=00D4AA&icon_color=00D4AA&text_color=c9d1d9&ring_color=00D4AA&count_private=true&include_all_commits=true&custom_title=%E2%9A%A1+Stats&exclude_repo={EXCLUDE_REPOS}" alt="Stats" width="400" />
    </td>
    <td align="center" valign="top">
      <img src="https://github-readme-stats-gamma-one-20.vercel.app/api/top-langs/?username={USERNAME}&layout=compact&theme=dark&hide_border=true&bg_color=0d1117&title_color=00D4AA&text_color=c9d1d9&langs_count=4&hide=javascript,typescript,html&custom_title=%F0%9F%92%BB+Languages&exclude_repo={EXCLUDE_REPOS}" alt="Languages" width="350" />
    </td>
  </tr>
</table>''')
    elif stats_up:
        parts.append(f'''
<p align="center">
  <img src="https://github-readme-stats-gamma-one-20.vercel.app/api?username={USERNAME}&show_icons=true&hide_border=true&bg_color=0d1117&title_color=00D4AA&icon_color=00D4AA&text_color=c9d1d9&ring_color=00D4AA&count_private=true&include_all_commits=true&custom_title=%E2%9A%A1+Stats&exclude_repo={EXCLUDE_REPOS}" alt="Stats" width="520" />
</p>''')
    elif langs_up:
        parts.append(f'''
<p align="center">
  <img src="https://github-readme-stats-gamma-one-20.vercel.app/api/top-langs/?username={USERNAME}&layout=compact&theme=dark&hide_border=true&bg_color=0d1117&title_color=00D4AA&text_color=c9d1d9&langs_count=4&hide=javascript,typescript,html&custom_title=%F0%9F%92%BB+Languages&exclude_repo={EXCLUDE_REPOS}" alt="Languages" width="520" />
</p>''')

    # Remaining services — just include their block if alive
    for name, _, block in SERVICES:
        if name in ("stats", "languages"):
            continue
        if block and alive.get(name, False):
            parts.append(f"\n{block}")

    return "\n".join(parts)


def main():
    # Health-check all services
    alive = {}
    for name, url, _ in SERVICES:
        ok = check_url(url)
        alive[name] = ok
        status = "[UP]" if ok else "[DOWN]"
        print(f"  {status}  {name}")

    up_count = sum(1 for v in alive.values() if v)
    total = len(alive)
    print(f"\n  {up_count}/{total} services healthy")

    # Read template
    with open("TEMPLATE.md", "r", encoding="utf-8") as f:
        template = f.read()

    # Build analytics section
    if up_count > 0:
        analytics = build_analytics(alive)
    else:
        analytics = ""

    # Replace placeholder
    readme = template.replace(
        "<!-- GITHUB_ANALYTICS_START -->\n<!-- GITHUB_ANALYTICS_END -->",
        f"<!-- GITHUB_ANALYTICS_START -->\n{analytics}\n<!-- GITHUB_ANALYTICS_END -->"
    )

    # Write README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    print(f"\n  README.md generated ({up_count} analytics cards included)")


if __name__ == "__main__":
    main()
