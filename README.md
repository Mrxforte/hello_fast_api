# Eshop API

Clean Architecture backend starter for a marketplace platform with authentication, role-based access, vendor operations, product catalog management, and order flow.

---

## Project Snapshot

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-009688?logo=fastapi&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-Clean-0A0A0A)
![Auth](https://img.shields.io/badge/Auth-JWT-8A2BE2)

## Why This Template

- Clear separation of domain, application, infrastructure, and presentation layers
- Ready-to-run auth with JWT and role checks
- Marketplace-focused modules for vendors, products, and orders
- Easy to swap storage implementation from in-memory to SQL/NoSQL
- Great starting point for scaling into a production backend

## Feature Set

- JWT authentication
- Role-based authorization: `admin`, `vendor`, `customer`
- Vendor profile creation and retrieval
- Product CRUD for vendor-owned products
- Customer order creation with stock validation
- Vendor order confirmation flow
- Health check endpoint

---

## Architecture Layout

```text
app/
  domain/
    entities/
    repositories/
    services/
  application/
    schemas/
    use_cases/
  infrastructure/
    repositories/
    security/
    container.py
  presentation/
    api/v1/
      routers/
main.py
requirements.txt
```

## Layer Responsibilities

| Layer | Responsibility |
|---|---|
| Domain | Business entities, repository contracts, core rules |
| Application | Use-cases and request/response schemas |
| Infrastructure | Security, dependency wiring, repository implementations |
| Presentation | FastAPI routers and HTTP transport layer |

---

## Quick Start

### 1) Create environment

```bash
python -m venv .venv
```

### 2) Activate environment

```bash
.venv\Scripts\activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Run server

```bash
uvicorn main:app --reload
```

### 5) Open API docs

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

## Default Admin User

The app seeds one admin account on startup.

- Email: `admin@example.com`
- Password: `Admin123!`

---

## Authorization Matrix

| Endpoint Group | Admin | Vendor | Customer |
|---|---|---|---|
| Auth | Yes | Yes | Yes |
| Vendors `/me` | No | Yes | No |
| Products write | No | Yes | No |
| Products read | Yes | Yes | Yes |
| Orders create | No | No | Yes |
| Orders confirm | No | Yes | No |
| Orders `/me` | Yes | Yes | Yes |

---

## API Endpoints

### Health

| Method | Path |
|---|---|
| GET | `/api/v1/health` |

### Auth

| Method | Path |
|---|---|
| POST | `/api/v1/auth/register` |
| POST | `/api/v1/auth/login` |

### Vendors

| Method | Path | Access |
|---|---|---|
| POST | `/api/v1/vendors/me` | Vendor |
| GET | `/api/v1/vendors/me` | Vendor |
| GET | `/api/v1/vendors` | Public/Auth |

### Products

| Method | Path | Access |
|---|---|---|
| POST | `/api/v1/products` | Vendor |
| PATCH | `/api/v1/products/{product_id}` | Vendor |
| DELETE | `/api/v1/products/{product_id}` | Vendor |
| GET | `/api/v1/products` | Public/Auth |
| GET | `/api/v1/products/vendor/{vendor_id}` | Public/Auth |

### Orders

| Method | Path | Access |
|---|---|---|
| POST | `/api/v1/orders` | Customer |
| PATCH | `/api/v1/orders/{order_id}/confirm` | Vendor |
| GET | `/api/v1/orders/me` | Customer, Vendor, Admin |

---

## Auth Usage Example

1. Register a user with role `vendor` or `customer`
2. Login and receive `access_token`
3. Pass token in request header

```text
Authorization: Bearer <access_token>
```

---

## Current Storage Mode

This template currently uses in-memory repositories for fast local development.

To move to production:

1. Add database-backed repositories under `app/infrastructure/repositories`
2. Replace container bindings in `app/infrastructure/container.py`
3. Add migrations and persistent configuration

---

## Next Improvements

- Add refresh tokens and token revocation
- Add pagination, filtering, and search for products
- Add integration tests and CI pipeline
- Add observability (structured logs, tracing, metrics)