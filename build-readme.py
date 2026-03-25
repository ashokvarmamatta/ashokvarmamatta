#!/usr/bin/env python3
"""
Builds README.md from TEMPLATE.md by health-checking each GitHub analytics
service and only including cards that are currently responding (HTTP 200).
"""

import urllib.request
import sys

USERNAME = "ashokvarmamatta"

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
    (
        "streak",
        f"https://streak-stats.demolab.com?user={USERNAME}",
        f'''<p align="center">
  <img src="https://streak-stats.demolab.com?user={USERNAME}&hide_border=true&background=0d1117&ring=00D4AA&fire=FF6B6B&currStreakLabel=00D4AA&sideLabels=c9d1d9&dates=555555&currStreakNum=00D4AA&sideNums=00D4AA" alt="Streak" width="520" />
</p>'''
    ),
    (
        "summary_cards",
        f"https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username={USERNAME}&theme=github_dark",
        f'''<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username={USERNAME}&theme=github_dark" alt="Repos/Lang" width="260" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username={USERNAME}&theme=github_dark" alt="Commits/Lang" width="260" />
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username={USERNAME}&theme=github_dark&utcOffset=5.5" alt="Productive Hours" width="260" />
</p>

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username={USERNAME}&theme=github_dark" alt="Contribution Map" width="95%" />
</p>'''
    ),
    (
        "activity_graph",
        f"https://github-readme-activity-graph.vercel.app/graph?username={USERNAME}",
        f'''<details>
<summary><b>📈 Contribution Activity Graph</b></summary>
<br/>
<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username={USERNAME}&bg_color=0d1117&color=00D4AA&line=00D4AA&point=FF6B6B&area=true&area_color=00D4AA&hide_border=true&custom_title=Contribution%20Activity" alt="Activity Graph" width="95%" />
</p>
</details>'''
    ),
    (
        "trophies",
        f"https://github-trophies.vercel.app/?username={USERNAME}&theme=algolia",
        f'''<details>
<summary><b>🏆 GitHub Trophies</b></summary>
<br/>
<p align="center">
  <img src="https://github-trophies.vercel.app/?username={USERNAME}&theme=algolia&no-frame=true&no-bg=true&column=7&margin-w=6" alt="Trophies" width="95%" />
</p>
</details>'''
    ),
    (
        "contrib_3d",
        f"https://ssr-contributions-svg.vercel.app/_/{USERNAME}?chart=3dbar&format=svg&weeks=50&dark=true",
        f'''<details>
<summary><b>🧊 3D Contribution Calendar</b></summary>
<br/>
<p align="center">
  <img src="https://ssr-contributions-svg.vercel.app/_/{USERNAME}?chart=3dbar&gap=0.6&scale=2&flatten=2&animation=wave&animation_duration=4&animation_delay=0.06&animation_amplitude=24&animation_frequency=0.1&animation_wave_center=0_3&format=svg&weeks=50&dark=true&widget_size=large" alt="3D Contributions" width="95%" />
</p>
</details>'''
    ),
    (
        "snake",
        f"https://raw.githubusercontent.com/{USERNAME}/{USERNAME}/output/ocean.gif",
        f'''<details>
<summary><b>🐍 Contribution Snake</b></summary>
<br/>
<p align="center">
  <img src="https://raw.githubusercontent.com/{USERNAME}/{USERNAME}/output/ocean.gif" alt="Snake Animation" width="100%" />
</p>
</details>'''
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
      <img src="https://github-readme-stats-gamma-one-20.vercel.app/api?username={USERNAME}&show_icons=true&hide_border=true&bg_color=0d1117&title_color=00D4AA&icon_color=00D4AA&text_color=c9d1d9&ring_color=00D4AA&count_private=true&include_all_commits=true&custom_title=%E2%9A%A1+Stats" alt="Stats" width="400" />
    </td>
    <td align="center" valign="top">
      <img src="https://github-readme-stats-gamma-one-20.vercel.app/api/top-langs/?username={USERNAME}&layout=compact&theme=dark&hide_border=true&bg_color=0d1117&title_color=00D4AA&text_color=c9d1d9&langs_count=6&custom_title=%F0%9F%92%BB+Languages" alt="Languages" width="350" />
    </td>
  </tr>
</table>''')
    elif stats_up:
        parts.append(f'''
<p align="center">
  <img src="https://github-readme-stats-gamma-one-20.vercel.app/api?username={USERNAME}&show_icons=true&hide_border=true&bg_color=0d1117&title_color=00D4AA&icon_color=00D4AA&text_color=c9d1d9&ring_color=00D4AA&count_private=true&include_all_commits=true&custom_title=%E2%9A%A1+Stats" alt="Stats" width="520" />
</p>''')
    elif langs_up:
        parts.append(f'''
<p align="center">
  <img src="https://github-readme-stats-gamma-one-20.vercel.app/api/top-langs/?username={USERNAME}&layout=compact&theme=dark&hide_border=true&bg_color=0d1117&title_color=00D4AA&text_color=c9d1d9&langs_count=6&custom_title=%F0%9F%92%BB+Languages" alt="Languages" width="520" />
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
