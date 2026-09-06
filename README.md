<p align="center"><img src="assets/banner.svg" alt="Privacy Footprint Scan" width="100%"></p>

# Privacy Footprint Scan

> Inventory possible personal data across a folder without printing sensitive values.

[![CI](https://github.com/zchstime/privacy-footprint-scan/actions/workflows/ci.yml/badge.svg)](https://github.com/zchstime/privacy-footprint-scan/actions/workflows/ci.yml) [![Python](https://img.shields.io/badge/python-3.11%2B-3776AB)](pyproject.toml) [![Dependencies](https://img.shields.io/badge/runtime_dependencies-0-16a34a)](pyproject.toml) [![MIT](https://img.shields.io/badge/license-MIT-f59e0b)](LICENSE)

Privacy Footprint Scan is a compact, privacy-friendly command-line utility built around one recurring workflow. It runs without an account or API key, keeps its decisions inspectable, and produces portable output you can use immediately.

## Why it is useful

Inventory possible personal data across a folder without printing sensitive values. Instead of hiding simple analysis behind a hosted service, it keeps data local and shows the evidence behind every recommendation.

## Highlights

- Email, phone, IP, and secret hints
- File-type and risk aggregation
- No raw value disclosure
- Binary and large-file safeguards
- Zero third-party runtime dependencies

## Quick start

```bash
git clone https://github.com/zchstime/privacy-footprint-scan.git
cd privacy-footprint-scan
python -m pip install -e .

privacy-scan examples --output privacy-report.md
```

Use the synthetic [`examples/`](examples/) data for a safe first run. Run `privacy-scan --help` for the complete command reference.

## Design

```text
local input → deterministic analysis → cited findings → portable report
```

The default workflow performs no network requests and does not silently modify source data. The implementation is deliberately small enough to audit, teach from, and extend.

## Test

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

GitHub Actions tests Python 3.11, 3.12, and 3.13.

## Roadmap

- Additional import and export formats
- More community-provided edge-case fixtures
- Stable machine-readable report schemas
- Optional plugin hooks while keeping the core dependency-free

If this tool saves you time, **star the repository** and share the workflow you want next. Contributions are welcome—start with the open `good first issue`.

## Community and security

See [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md). Never put private data or real credentials in an issue.

## License

[MIT](LICENSE) © 2026 zchstime
