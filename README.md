# gov-signal

정부 지원사업 공고를 자동 집계하고 서울 소재 AI/IT 개발사 대표·사업개발 담당자에게 맞춤 추천해주는 SaaS.

## Monorepo layout

```
LEE/
├── backend/          # FastAPI + crawlers + parsers (Python 3.12, uv)
├── frontend/         # Next.js 15 (Week 5 이후)
├── docker-compose.yml
├── README.md
├── PROGRESS.md       # 세션별 진척도
└── TODO.md           # 당일 체크리스트
```

## Prerequisites

- Docker Desktop (또는 docker + docker-compose)
- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- (Week 5+) Node.js 20+, pnpm

## Local development

```bash
# 1. PostgreSQL 16 + pgvector 컨테이너 기동 (호스트 5433 포트)
docker-compose up -d

# 2. 백엔드 의존성 설치
cd backend
uv sync

# 3. 환경변수 준비 (최소 ANTHROPIC_API_KEY만 채우면 됨)
cp .env.example .env
# 에디터로 .env 열고 ANTHROPIC_API_KEY 등 작성

# 4. FastAPI 실행
uv run uvicorn app.main:app --reload

# 5. 다른 터미널에서 헬스체크
curl http://localhost:8000/health
# => {"status":"ok","env":"development"}
```

## Week 1 Day 1 부팅 검증 체크리스트

형님이 로컬에서 아래 순서대로 돌려보시고 모두 통과하면 Day 1 완료입니다.

- [ ] `docker-compose up -d` → `gov-signal-db` 컨테이너 `Up (healthy)` 상태
- [ ] `docker ps` 로 5433 포트 LISTEN 확인
- [ ] `cd backend && uv sync` → 에러 없이 `.venv/` 생성
- [ ] `cp .env.example .env` 로 `.env` 생성 (값은 비어도 됨 — config.py에 기본값 있음)
- [ ] `uv run uvicorn app.main:app --reload` → `Uvicorn running on http://127.0.0.1:8000` 로그
- [ ] `curl http://localhost:8000/health` → `{"status":"ok","env":"development"}` 응답
- [ ] 브라우저에서 `http://localhost:8000/docs` 접속 → Swagger UI 표시

## Roadmap (12주)

- **Week 1**: 프로젝트 스캐폴드, DB/설정/로깅, bizinfo 크롤러 프로토타입
- **Week 2**: IRIS·NIPA 크롤러, 공고 원본 스냅샷 저장
- **Week 3**: KIAT·KIRIA 크롤러, 중복 제거 및 포털 간 병합
- **Week 4**: HWPX 파서, 첨부파일 다운로드/파싱 파이프라인
- **Week 5**: Next.js 프론트엔드 초기화, 공고 리스트/상세 페이지
- **Week 6**: 사용자 프로필 스키마, 키워드 기반 기본 추천
- **Week 7**: Claude API 연동, 공고 LLM 구조화(요약·조건 추출)
- **Week 8**: pgvector 임베딩 기반 유사도 추천
- **Week 9**: 맞춤 알림 (이메일 or 슬랙 웹훅) MVP
- **Week 10**: 인증(로그인/세션), 대시보드 개인화
- **Week 11**: 관측성(로그/메트릭), GitHub Actions 스케줄러 이관
- **Week 12**: 베타 유저 온보딩, 피드백 수집, 버그픽스

## License

TBD
