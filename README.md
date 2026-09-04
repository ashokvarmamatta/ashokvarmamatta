<h1 align="center">Matta Ashok Varma</h1>
<p align="center">
  <b>Android Developer · Kotlin · Jetpack Compose · On-Device AI</b><br/>
  Hyderabad, India · 4 years shipping native Android
</p>
<p align="center">
  <a href="https://ashokvarma.dev/"><img src="https://img.shields.io/badge/Portfolio-00D4AA?style=flat-square&logo=googlechrome&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/ashokvarmamatta"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white" /></a>
  <a href="mailto:mashokvarma1997@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" /></a>
  <img src="https://img.shields.io/badge/Open_to_Senior_Android_roles-3DDC84?style=flat-square&logo=android&logoColor=white" />
</p>

I build native Android at **Ramson Softech**, Hyderabad. I work on consumer apps past **10M and
5M installs**, ship my own to Google Play, and most of my current work is **AI running on the
device rather than a server** — ML Kit GenAI and Gemma 4 through LiteRT, in production.

| | |
|---|---|
| **92%** fewer crashes | found a `WallpaperService` ↔ `Camera2` ownership conflict across lifecycle transitions · app has **10M+ installs** |
| **ANR −38%**, cold start **−45%** | GPS callbacks arriving faster than they were consumed, plus lazy DI · **5M+ installs** |
| crash-free 96.1% → **99.4%**, APK **−22%** | lifecycle-aware coroutines, removed unused ML model binaries |
| **ML Kit GenAI** on-device summarization | shipped in a production app |

**Open to Senior Android roles** — Hyderabad or remote. Kotlin, Compose, Media3, on-device AI.

---

## 🟢 On Google Play — designed, built and released solo

<table>
<tr>
<td width="50%" valign="top">

**[ANTAR — Device Analytics](https://play.google.com/store/apps/details?id=com.ashes.dev.works.system.core.internals.antar)**
· [source](https://github.com/ashokvarmamatta/ANTAR)

44+ hardware sensors surfaced as real-time `StateFlow` streams, dual-SIM detection, GPS
satellite tracking, custom Compose Canvas charts. Released through a tag-triggered GitHub
Actions pipeline.

`Kotlin` `Compose` `Canvas` `SensorManager` `Clean Architecture` `GitHub Actions`

</td>
<td width="50%" valign="top">

**[Chitra — AI Wallpapers](https://play.google.com/store/apps/details?id=com.ashes.dev.works.chitra.cosmos)**
· [KMP engine](https://github.com/ashokvarmamatta/Chitra)

Curated collections delivered over a Cloudflare R2 CDN with an offline-first Room cache. The
open-source engine runs the same Kotlin codebase on Android, Desktop (JVM) and Web (Wasm/JS).

`Kotlin` `Compose Multiplatform` `Cloudflare R2` `Room` `Ktor` `Voyager`

</td>
</tr>
</table>

*Two more built and waiting to upload.*

## Open source

**[MEDHA — On-Device AI Chat](https://github.com/ashokvarmamatta/MEDHA)**
LLM inference on the phone with no network at all — **Gemma 4 (E2B) via Google LiteRT LM**,
GPU-accelerated, handling text, vision and audio. Optional Gemini path with multi-key failover.
`Kotlin` `LiteRT LM` `Gemma 4` `Compose` `Koin` `Room`

**[ZeroClawAndroid — Always-On Agent Daemon](https://github.com/ashokvarmamatta/ZeroClawAndroid)**
An Android foreground service that stays alive, bridging Telegram and WhatsApp to multiple model
providers with automatic waterfall failover, reachable over a Cloudflare Tunnel.
`Kotlin` `Foreground Services` `Ktor` `Cloudflare Tunnel` `Multi-LLM`

---

<details>
<summary><h2 style="display:inline">🔍 Engineering log — things that broke, and why</h2></summary>

<br/>

> A running list. I add to it as I hit things worth writing down.

**Casting a file the receiver cannot see**
A Chromecast has no access to the phone's filesystem, so "cast this local video" is not a
playback problem — it is a networking one. The app runs an embedded **NanoHTTPD** server and
hands the receiver a URL on the phone's own LAN address. Media3 covers HLS, DASH and RTSP for
the streams it can reach directly. *(Video AI Player)*

**A camera that was never free**
A live wallpaper kept dying with Camera Busy. The cause was `WallpaperService` and `Camera2`
disagreeing about who owned the camera across lifecycle transitions — not a camera bug. Binding
acquisition to the surface lifecycle and releasing on every teardown path took crashes down
**92%** on an app with 10M+ installs.

**ANRs that were not in the UI thread's own work**
A maps app was blocking on GPS callbacks arriving faster than they were consumed. Restructuring
the callback path and moving DI to lazy initialization cut **ANR 38%** and **cold start 45%**.

**Sign-in that failed as "cancelled by user"**
Google Sign-In through Credential Manager bounced with no picker, and Firestore threw
`Unknown calling package name`. Neither message points at the cause: the build machine's debug
**SHA-1 was not registered** in the Firebase project. Two more that cost time on the same flow —
Credential Manager needs an **Activity** context to draw the picker, not the application context;
and Firebase requires a **recent login** before it will delete an account, so deletion has to
re-authenticate and retry.

**A model format that stopped loading on Android 15**
Android 15's 16 KB memory page size broke the existing TFLite path. Migrating to **LiteRT** and
re-checking GPU delegation restored on-device super-resolution.

**Paging that returned zero rows without erroring**
A Firestore query succeeded and came back empty. Adding an `orderBy` on a field outside the
equality filters had quietly pushed it off the automatic single-field indexes. Filter-only
queries, ordered by document id, need no composite index.

</details>

## 🛠️ Core Technologies

<table>
  <tr>
    <td align="center" width="25%">
      <b>📱 Mobile</b><br/><br/>
      <img src="https://skillicons.dev/icons?i=kotlin,java,androidstudio&perline=3" /><br/>
      <sub>Kotlin • Java • Android Studio</sub>
    </td>
    <td align="center" width="25%">
      <b>🎨 UI & Frameworks</b><br/><br/>
      <img src="https://skillicons.dev/icons?i=materialui,firebase,gradle&perline=3" /><br/>
      <sub>Material 3 • Firebase • Gradle</sub>
    </td>
    <td align="center" width="25%">
      <b>🌐 Web & Cross-Platform</b><br/><br/>
      <img src="https://skillicons.dev/icons?i=kotlin,wasm,js&perline=3" /><br/>
      <sub>KMP Wasm/JS • Compose Web</sub>
    </td>
    <td align="center" width="25%">
      <b>🔧 Tools & Design</b><br/><br/>
      <img src="https://skillicons.dev/icons?i=git,github,figma&perline=3" /><br/>
      <sub>Git • GitHub • Figma</sub>
    </td>
  </tr>
</table>

<p align="center">
  <img src="https://img.shields.io/badge/Jetpack_Compose-4285F4?style=flat-square&logo=jetpackcompose&logoColor=white" />
  <img src="https://img.shields.io/badge/KMP-7F52FF?style=flat-square&logo=kotlin&logoColor=white" />
  <img src="https://img.shields.io/badge/Kotlin%2FWasm-7F52FF?style=flat-square&logo=webassembly&logoColor=white" />
  <img src="https://img.shields.io/badge/Compose_Web-4285F4?style=flat-square&logo=jetpackcompose&logoColor=white" />
  <img src="https://img.shields.io/badge/Hilt_%26_Koin-F88909?style=flat-square&logo=android&logoColor=white" />
  <img src="https://img.shields.io/badge/Room_DB-003B57?style=flat-square&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Coroutines_%26_Flow-7F52FF?style=flat-square&logo=kotlin&logoColor=white" />
  <img src="https://img.shields.io/badge/Media3_%2F_ExoPlayer-FF0000?style=flat-square&logo=youtube&logoColor=white" />
  <img src="https://img.shields.io/badge/Google_Cast-4285F4?style=flat-square&logo=googlecast&logoColor=white" />
  <img src="https://img.shields.io/badge/Ktor-087CFA?style=flat-square&logo=ktor&logoColor=white" />
  <img src="https://img.shields.io/badge/Retrofit_%2F_OkHttp-48B983?style=flat-square&logo=square&logoColor=white" />
  <img src="https://img.shields.io/badge/Coil_3-000000?style=flat-square&logo=android&logoColor=white" />
  <img src="https://img.shields.io/badge/CameraX-34A853?style=flat-square&logo=android&logoColor=white" />
  <img src="https://img.shields.io/badge/ML_Kit-4285F4?style=flat-square&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/ML_Kit_GenAI-4285F4?style=flat-square&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/LiteRT-FF6F00?style=flat-square&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/Biometric_%2F_OAuth-D14836?style=flat-square&logo=android&logoColor=white" />
  <img src="https://img.shields.io/badge/MVVM_%2F_MVI-00897B?style=flat-square&logo=android&logoColor=white" />
  <img src="https://img.shields.io/badge/Clean_Architecture-6DB33F?style=flat-square&logo=spring&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/SQL-4479A1?style=flat-square&logo=postgresql&logoColor=white" />
</p>

<sub align="center">AI-assisted for code review, test scaffolding, refactoring and research. Architecture, on-device debugging and production fixes are hands-on — I reproduce crashes on real devices and fix them myself.</sub>

---

## At Ramson Softech — apps I work on with the team

> Company apps, not my repos. The improvements and the numbers are mine; the products are theirs.

| App | Scale | What I did |
|---|---|---|
| [Transparent Live Wallpaper](https://play.google.com/store/apps/details?id=com.ram.transparentlivewallpaper) · [Camera Screen](https://play.google.com/store/apps/details?id=com.raisingapps.transparentlauncher.screenlivewallpaper) | **10M+ each** | Camera Busy crashes traced to a WallpaperService/Camera2 ownership conflict — **92%** crash reduction |
| [GPS Village Maps](https://play.google.com/store/apps/details?id=com.gpsmaps.villagemaps.directions.whereami.navigation.gpsarea.location.tracker) | **5M+** | ANR **−38%**, cold start **−45%**, 60% of XML migrated to Compose, dual Maps + HERE SDK |
| [Video AI Player](https://play.google.com/store/apps/details?id=com.rms.videoplayerai.allformat.playvideo) | new | Media3 HLS/DASH/RTSP, Google Cast over an embedded HTTP server, PiP, Transformer editing |
| [QR & Barcode Scanner](https://play.google.com/store/apps/details?id=com.rstech.qrcodescanner.barcode.qrgenarator.qrreader.createqr.barcodereader) | — | 100% of scanner leaks removed, crash-free 96.1% → **99.4%**, APK **−22%** |

## 📚 Learning right now

**Agentic Android** — apps that expose their own functions so an on-device model can call them:
`androidx.appfunctions`, ML Kit GenAI, and where the OS is heading with on-device tool calling.
The interesting part is that the app stops being a UI you tap and becomes something an assistant
can operate on your behalf.

**Neural networks from the ground up** — working through Karpathy's *Zero to Hero*, building the
autograd engine and the models by hand rather than importing them, so the on-device inference
work rests on something I actually understand.

**Quantization and measurement on real hardware** — running models on the phone, quantizing them,
and recording tokens/sec, RAM and battery instead of guessing.

**Testing discipline** — JUnit, MockK, Turbine and Robolectric, and getting a suite running in CI
on apps that do not have one yet.

## Writing

[Gemma 4 on Android via LiteRT LM](https://gist.github.com/ashokvarmamatta) ·
[Multi-provider AI integration for Android](https://gist.github.com/ashokvarmamatta) ·
[MCP knowledge vault for Android](https://gist.github.com/ashokvarmamatta) ·
[Android over Cloudflare tunnels](https://gist.github.com/ashokvarmamatta)

<details>
<summary><b>More projects</b></summary>
<br/>

| Project | What it is | Tech |
|---|---|---|
| [ProPlayer](https://github.com/ashokvarmamatta/videoplayer2) | Video player — PiP, gestures, subtitles, playlists | Compose, ExoPlayer, Koin, Room |
| [WeatherShow KMP](https://github.com/ashokvarmamatta/WeatherShow-KMP) | Cross-platform weather — [live demo](https://weather-show-kmp.vercel.app) | KMP, Compose Multiplatform, Ktor |
| [MedicineReminder](https://github.com/ashokvarmamatta/MedicineReminder) | Scheduled notifications and tracking | Kotlin, AlarmManager, Room |

</details>

<!-- GITHUB_ANALYTICS_START -->
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,2,5,30&height=1&section=header" width="100%"/>
<br/>

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=22&pause=1000&color=00D4AA&center=true&vCenter=true&width=400&lines=%F0%9F%93%8A+GitHub+Analytics" alt="GitHub Analytics" />
</div>

<table align="center" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <td align="center" valign="top">
      <img src="https://github-readme-stats-gamma-one-20.vercel.app/api?username=ashokvarmamatta&show_icons=true&hide_border=true&bg_color=0d1117&title_color=00D4AA&icon_color=00D4AA&text_color=c9d1d9&ring_color=00D4AA&count_private=true&include_all_commits=true&custom_title=%E2%9A%A1+Stats&exclude_repo=Advance-Hearing-App" alt="Stats" width="400" />
    </td>
    <td align="center" valign="top">
      <img src="https://github-readme-stats-gamma-one-20.vercel.app/api/top-langs/?username=ashokvarmamatta&layout=compact&theme=dark&hide_border=true&bg_color=0d1117&title_color=00D4AA&text_color=c9d1d9&langs_count=4&hide=javascript,typescript,html&custom_title=%F0%9F%92%BB+Languages&exclude_repo=Advance-Hearing-App" alt="Languages" width="350" />
    </td>
  </tr>
</table>
<!-- GITHUB_ANALYTICS_END -->
