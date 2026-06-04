# Changelog

## v3.0.0 (2026-06-04)

Stable release of the python-getpaid ecosystem umbrella package.

### Breaking Changes

- All gateway backends and framework adapters are now at stable `3.0.0`.
- Optional dependency floors updated from alpha constraints (`>=3.0.0a4`) to stable (`>=3.0.0`).

### Features

- Complete ecosystem umbrella: install all backends and framework adapters with `pip install python-getpaid[all]`.
- Extras for every payment gateway: `payu`, `paynow`, `przelewy24`, `bitpay`.
- Extras for every framework adapter: `django`, `fastapi`, `litestar`.
- Bundle extras: `backends` (all gateways), `frameworks` (all adapters), `all` (everything).
