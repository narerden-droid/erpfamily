# Family ERP

Семейная учетно-аналитическая система: члены семьи, финансы, покупки, бюджет, отчёты.

**Стек:** React + TypeScript + Vite + Tailwind · FastAPI (Python 3.12) · PostgreSQL 16 · SQLAlchemy 2 · Alembic · Docker Compose · Caddy (HTTPS).

## Быстрый старт (локально, через Docker)

```bash
cp .env.example .env
# в .env: APP_ENV=development, SESSION_COOKIE_SECURE=false, задайте POSTGRES_PASSWORD и SECRET_KEY
docker compose up --build
```
Откройте https://localhost (локальный сертификат Caddy) · документация API: /api/docs

## Разработка без Docker

```bash
# backend
cd backend && python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload            # :8000
# frontend
cd frontend && npm install && npm run dev   # :5173, /api проксируется на :8000
# тесты (из корня)
pytest tests -q
```

## Безопасность
- `.env` в `.gitignore`; в репозитории только `.env.example`.
- PostgreSQL не публикуется наружу, доступен только во внутренней сети Compose.
- Наружу открыты лишь порты 80/443 (Caddy).

## Статус
- [x] Шаг 1 — структура проекта и конфигурация
- [ ] Шаг 2 — схема PostgreSQL и миграции
- [ ] Шаги 3–10 — см. промпт
