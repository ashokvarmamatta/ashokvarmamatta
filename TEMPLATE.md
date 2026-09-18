## Matta Ashok Varma

**Android Developer · 4.5 years · Hyderabad** — apps I've worked on have **25M+ installs** on Google Play.
Open to **Senior Android** roles, Hyderabad or remote.

[![Portfolio](https://img.shields.io/badge/Portfolio-ashokvarma.dev-00D4AA?style=flat-square)](https://ashokvarma.dev/) [![Résumé](https://img.shields.io/badge/Résumé-PDF-3DDC84?style=flat-square)](https://ashokvarma.dev/Ashok_Varma_Resume.pdf) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ashokvarmamatta) [![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:mashokvarma1997@gmail.com)

At **Ramson Softech** I build consumer apps in Kotlin and Compose from an empty project to Google Play, and modernize legacy Java and XML codebases — migrating them to Kotlin and Compose while fixing the ANRs, crashes and memory leaks they carry.

### At Ramson — company apps

**Took over and fixed**
- [Transparent Live Wallpaper](https://play.google.com/store/apps/details?id=com.ram.transparentlivewallpaper) and [Camera Screen](https://play.google.com/store/apps/details?id=com.raisingapps.transparentlauncher.screenlivewallpaper) — **10M+ installs each** — 92% fewer crashes after fixing a camera lifecycle conflict
- [All Village Maps](https://play.google.com/store/apps/details?id=com.gpsmaps.villagemaps.directions.whereami.navigation.gpsarea.location.tracker) — **5M+ installs** — ANR −38%, cold start −45%

**Built from scratch**
- [Video AI Player](https://play.google.com/store/apps/details?id=com.rms.videoplayerai.allformat.playvideo) — streaming (HLS, DASH, RTSP) and Chromecast casting
- [QR & Barcode Scanner](https://play.google.com/store/apps/details?id=com.rstech.qrcodescanner.barcode.qrgenarator.qrreader.createqr.barcodereader) — crash-free 99.4%, APK −22%

Also shipped: **ML Kit GenAI** on-device summarization in a production app. Company code is private — the numbers are mine, the products are Ramson's.

### My own apps
| | App | |
|---|---|---|
| <img src="https://play-lh.googleusercontent.com/k1GL7ov3Md2Ufl3Rz26WOp2uhy-qfgKvebLfpB_Osxqfhh6rkHcPlV7Fq2k6Z9d-E7R6LsbP6gvZtrUTcegTbg=s64" width="40"> | **ANTAR** · [Play](https://play.google.com/store/apps/details?id=com.ashes.dev.works.system.core.internals.antar) · [website](https://antar.ashokvarma.dev) · [source](https://github.com/ashokvarmamatta/ANTAR) | device analytics — 44+ sensors as real-time `StateFlow` streams, custom Compose Canvas charts |
| <img src="https://play-lh.googleusercontent.com/Iv03utZCQVH3RHz2Hh9A9xqKq6aUU-eiskPmhIe3fsfQfXmWfCwY-gIkuAXmvdnbI25rRW02th65Qtk9lbw8=s64" width="40"> | **Chitra** · [Play](https://play.google.com/store/apps/details?id=com.ashes.dev.works.chitra.cosmos) · [website](https://chitra.ashokvarma.dev) · [source](https://github.com/ashokvarmamatta/Chitra) | wallpapers — one Compose Multiplatform codebase for Android, Desktop and Web |
| <img src="https://erosion-rider.ashokvarma.dev/apple-touch-icon.png" width="40"> | **Erosion Rider** · [website](https://erosion-rider.ashokvarma.dev) | sand-surfing game on a custom momentum-physics engine — the terrain erodes where you ride and stays carved. In development |
| 🧠 | **MEDHA** · [source](https://github.com/ashokvarmamatta/MEDHA) | LLM chat that runs fully offline on the phone — Gemma 4 through Google LiteRT LM |

### What I'm digging into
- **On-device AI** — running and quantizing models on real phones, measuring tokens/sec, RAM and battery instead of guessing; and **AppFunctions**, where an app exposes functions an on-device model can call.
- **Adaptive layout as a build gate** — from targetSdk 37, Android 17 ignores orientation and resizability locks on screens 600dp and up, with no opt-out. Three apps I work on already target 37, so I'm moving them to layouts keyed on window size class.
- **Foldables** — trifolds and landscape foldables open landscape-first, so "portrait is natural" breaks exactly where layout matters most. `FoldingFeature` keeps controls off the hinge.

**Writing:** [Gemma 4 on an Android phone with LiteRT LM](https://gist.github.com/ashokvarmamatta/2305e6d9a2c7b5ac7da8fc5c1c95e489) · [Downloading on-device models on demand](https://gist.github.com/ashokvarmamatta/919390ed6c69caa42911df880324bd04) · [AppFunctions: making an app callable by on-device AI](https://gist.github.com/ashokvarmamatta/1f81c79e5a02cbfa50689fb8e4907619) · [Cloudflare Tunnels on Android](https://gist.github.com/ashokvarmamatta/1bba0d91a839039428bd942b8fdcc968)

**Stack:** Kotlin · Java · Jetpack Compose · XML Views · Coroutines & Flow · Hilt / Koin · Room · Media3 · CameraX · ML Kit · LiteRT · Compose Multiplatform · GitHub Actions

<details>
<summary><b>Engineering log — things that broke, and why</b></summary>

**Sign-in that failed as "cancelled by user".** Credential Manager bounced with no picker and Firestore threw `Unknown calling package name`. The cause: the build machine's debug SHA-1 was not registered in Firebase.

**A model that stopped loading on Android 15.** The 16 KB page size broke the TFLite path; migrating to LiteRT and re-checking GPU delegation fixed it.

**Paging that returned zero rows without erroring.** An `orderBy` outside the equality filters pushed the Firestore query off the automatic indexes.

</details>

<sub>Public repos here are my own apps and experiments; company code is private.</sub>

<!-- GITHUB_ANALYTICS_START -->
<!-- GITHUB_ANALYTICS_END -->
