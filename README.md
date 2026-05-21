# Stack Saver

Android wrapper for [Stack Saver](https://money.spookymallard.cfd) — a personal finance tracker built for Uganda.

## Features

- **Dashboard** — net worth, period income/expense/investment totals, trend line chart, category pie chart
- **Transactions** — log income, expenses, and investments with item name, amount, quantity, and category
- **Ledger** — filterable transaction history with edit/delete and CSV export
- **Accounts** — multiple account support (cash, mobile money, bank) with per-account balances
- **Transfers** — move money between accounts with automatic MTN/Airtel mobile money fee calculation
- **Investments** — track invested capital separately from liquid cash
- **Offline screen** — graceful fallback when no internet connection is detected

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Android wrapper | Kotlin + WebView (`minSdk 29`, `targetSdk 33`) |
| Web app | React + TypeScript + Vite |
| Styling | Tailwind CSS + shadcn/ui |
| Backend | Supabase (auth + Postgres) |
| Currency | UGX (Ugandan Shilling) |

## Requirements

- Android 10+ (API 29)
- Internet connection (web app loads from `https://money.spookymallard.cfd`)

## Installation

Download the latest APK from [Releases](https://github.com/Spooky-Mallard/Stack-Saver-mobile/releases) and install it.

> Enable **Install unknown apps** in Android settings if prompted.

## Building from Source

```bash
git clone https://github.com/Spooky-Mallard/Stack-Saver-mobile.git
cd Stack-Saver-mobile
./gradlew assembleRelease
```

Output APK: `app/build/outputs/apk/release/app-release.apk`

## License

MIT — see [LICENSE](LICENSE)
