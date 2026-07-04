# python-getpaid

Umbrella package for the **python-getpaid** payment processing ecosystem.

## Installation

Install the core library:

```bash
pip install python-getpaid
```

### Payment gateway backends

```bash
pip install python-getpaid[payu]
pip install python-getpaid[paynow]
pip install python-getpaid[przelewy24]
pip install python-getpaid[backends]       # all backends
```

### Framework adapters

```bash
pip install python-getpaid[django]
pip install python-getpaid[frameworks]     # all framework adapters
```

### Everything

```bash
pip install python-getpaid[all]
```

## Extras reference

| Extra | Installs |
|---|---|
| `payu` | `python-getpaid-payu` |
| `paynow` | `python-getpaid-paynow` |
| `przelewy24` | `python-getpaid-przelewy24` |
| `django` | `django-getpaid` |
| `backends` | All payment gateway backends |
| `frameworks` | All framework adapters |
| `all` | Everything above |

> **Note:** The `bitpay`, `fastapi`, and `litestar` integrations
> (`python-getpaid-bitpay`, `fastapi-getpaid`, `litestar-getpaid`) currently
> only have prerelease versions on PyPI, which pip does not install by
> default. Their extras have been removed for now and will return once
> stable releases of those packages are published. In the meantime you can
> install them explicitly, e.g. `pip install --pre python-getpaid-bitpay`.
