# Changelog

All notable changes to Stack Saver Android are documented here.

## [1.0.0] - 2025-05-21

### Added
- Initial release
- WebView wrapper loading `https://money.spookymallard.cfd`
- Immersive fullscreen mode — status bar and navigation bar hidden
- Edge-to-edge layout with transparent system bars
- System bar inset padding so web content never hides behind bars
- IME (keyboard) inset listener on `decorView` — system bars re-hidden after keyboard dismissal via back gesture or tap-outside
- Offline detection screen with retry button
- Back navigation routes through WebView history before exiting
- WebView state save/restore across configuration changes
- External URLs open in system browser instead of WebView
- Mixed content blocked (`MIXED_CONTENT_NEVER_ALLOW`)
- Dark background (`#0c0f17`) to prevent white flash before first paint
- Launcher icons generated from `logo.svg`
- Network security config
