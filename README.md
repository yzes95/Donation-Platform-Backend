# Ataa (عطاء) Donation Platform: Backend

FastAPI backend for the [Ataa frontend](https://github.com/yzes95/Donation-Platform).

## Status: skeleton (not production-ready)

| Part | State |
|---|---|
| `main.py` (app, CORS, `/health`) | ✅ Working |
| `routes/admin.py` (admin test router at `/api/v1/admin`) | ✅ Present |
| `routes/auth.py`, `families.py`, `services.py`, `donations.py`, `payments.py` | 🚧 Files exist but are **not included** in `main.py` (commented out `TODO`) |
| `models/` (user, family, service, donation, audit), `schemas/`, `database/` | 🚧 Defined, not yet wired to live routes |
| `services/payment_service.py` | ❌ Empty stub (no gateway integration) |
| Tests | ❌ None |
| Deployment | ❌ Not documented. The frontend's AWS Lab shows a *target* architecture only. |

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload --port 8000
```

Open `http://localhost:8000/docs` for the interactive API docs.

## Structure
`config/` settings · `database/` connection & base · `middleware/` auth · `models/` · `routes/` · `schemas/` · `services/` · `utils/`

## Roadmap
- [ ] Enable the auth, families, services, donations and payments routers
- [ ] Real payment gateway integration (InstaPay / Fawry / cards)
- [ ] Tests (pytest) and CI
- [ ] Containerize and deploy (the AWS design is documented in the frontend's AWS Lab)
