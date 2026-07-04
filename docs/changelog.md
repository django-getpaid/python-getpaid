# Changelog

## v3.2.0 (2026-07-04)

### Breaking Changes

- Removed the `bitpay`, `fastapi`, and `litestar` extras: `python-getpaid-bitpay`,
  `fastapi-getpaid`, and `litestar-getpaid` only have prerelease versions on PyPI,
  which pip excludes by default, making those extras (and any bundle including
  them) uninstallable for end users. This also changes the contents of the
  `backends`, `frameworks`, and `all` bundle extras — anyone relying on
  `python-getpaid[all]`, `[backends]`, or `[frameworks]` no longer gets those
  three integrations. The extras will return once stable releases of the
  underlying packages are published; until then install them explicitly with
  `pip install --pre <package>`.
- Raised the core dependency floor to `python-getpaid-core>=3.1.0`.

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
