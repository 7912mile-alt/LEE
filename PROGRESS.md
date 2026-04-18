# Progress log

세션이 끝날 때마다 Claude가 업데이트합니다. 최신 섹션이 위로 오도록 prepend.

---

## Week 1 Day 1 (2026-04-18) — 완료

### 오늘 한 일

- [x] 모노레포 폴더 구조 생성 (`backend/`, `frontend/`)
- [x] `docker-compose.yml` 작성 — PostgreSQL 16 + pgvector, 호스트 포트 5433
- [x] `backend/pyproject.toml` 작성 — uv 기반, 런타임/dev 의존성 버전 하한 지정
- [x] `backend/.env.example` 작성 — 키만, 값은 비움
- [x] `backend/app/core/config.py` — pydantic-settings 로 환경변수 로딩 (모든 필드 기본값 있음)
- [x] `backend/app/core/logging.py` — structlog 설정, dev에선 ConsoleRenderer / 그 외 JSONRenderer
- [x] `backend/app/db/session.py` — SQLAlchemy 2.x 엔진/세션/Base + `get_db()` 제너레이터
- [x] `backend/app/main.py` — FastAPI 앱 + `/health` 엔드포인트 + lifespan 로깅
- [x] 루트 `README.md` — 제품 개요, 로컬 개발법, 부팅 검증 체크리스트, 12주 로드맵
- [x] `.gitignore` — Python/Node/macOS/IDE/Playwright + `.env` 차단 (`.env.example`만 허용)
- [x] 초기 커밋 `feat: initial project scaffold`

### 설계 메모

- `config.py` 의 `DATABASE_URL` 기본값을 docker-compose 와 동일하게 두어, `.env` 없어도 `/health` 부팅이 가능하도록 함. 실제 운영/외부 DB 사용 시 `.env` 로 override.
- HWP 파싱은 Week 4부터. MVP 는 HWPX (XML) 만 지원 → `parsers/` 디렉토리는 예약만.
- 스케줄러: Week 11까지는 로컬 `cron` 또는 수동 실행. 이후 GitHub Actions 로 이관.
- `alembic/` 은 빈 폴더로만 예약. 실제 `alembic init` 은 첫 모델이 생길 때 (Week 1 Day 2~3) 수행.

### 내일(Week 1 Day 2) 할 일

- [ ] `alembic init alembic` 으로 마이그레이션 초기화
- [ ] 공고 도메인 최소 모델 스케치: `Portal`, `Notice`, `Attachment` SQLAlchemy 모델
- [ ] 첫 마이그레이션 생성/적용 → `\d notices` 로 테이블 확인
- [ ] pgvector `CREATE EXTENSION IF NOT EXISTS vector;` 마이그레이션 포함
- [ ] bizinfo 포털 URL 구조 조사 (크롤러 Week 1 Day 3~ 붙일 준비)

### 오픈 이슈 / 결정 대기

- bizinfo 가 robots.txt 로 크롤링 차단하는지 먼저 확인 필요.
- 포털별 중복 공고 식별키 설계 (URL? 공고번호? 해시?) — Day 2~3에 모델 확정 전에 결정.
- 프로덕션 DB 호스팅 (Supabase vs RDS vs Neon) — Week 10~11에 결정해도 늦지 않음.
