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
pip install python-getpaid[fastapi]
pip install python-getpaid[litestar]
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
| `fastapi` | `fastapi-getpaid` |
| `litestar` | `litestar-getpaid` |
| `backends` | All payment gateway backends |
| `frameworks` | All framework adapters |
| `all` | Everything above |
