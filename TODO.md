# TODO

## Week 1 Day 1 (2026-04-18) — 완료

- [x] 1. 모노레포 폴더 구조 생성 (`backend/`, `frontend/`, 기본 파일들)
- [x] 2. `docker-compose.yml` 작성 (PostgreSQL 16 + pgvector, 호스트 5433 포트)
- [x] 3. `backend/pyproject.toml` + `.env.example` 작성 (uv 기반, 의존성 명시)
- [x] 4. FastAPI 최소 앱 스캐폴딩 (`config.py`, `logging.py`, `main.py`, `db/session.py`, `/health`)
- [x] 5. 루트 `README.md` + `.gitignore` 작성 후 로컬 부팅 검증 → 초기 커밋

## 형님이 로컬에서 실행할 검증 체크리스트

- [ ] `docker-compose up -d`
- [ ] `cd backend && uv sync`
- [ ] `cp .env.example .env` (선택: `ANTHROPIC_API_KEY` 채우기)
- [ ] `uv run uvicorn app.main:app --reload`
- [ ] `curl http://localhost:8000/health` → `{"status":"ok","env":"development"}`

## Week 1 Day 2 예정

- [ ] `alembic init alembic`
- [ ] `Portal`, `Notice`, `Attachment` 모델 스케치
- [ ] 첫 마이그레이션 + pgvector extension 활성화
- [ ] bizinfo 포털 URL/robots.txt 조사
