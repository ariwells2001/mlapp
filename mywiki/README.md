# mywiki — LLM Wiki

LLM이 직접 쓰고 유지·관리하는 **개인 지식 베이스**입니다. RAG처럼 질문할 때마다 원문을 다시 뒤지는 대신, LLM이 소스를 읽어 **지속적으로 누적되는 위키**(서로 연결된 마크다운 파일들)를 점진적으로 구축하고 최신 상태로 유지합니다.

> Obsidian이 IDE, LLM이 프로그래머, 위키가 코드베이스입니다.
> 당신은 소스를 큐레이션하고 좋은 질문을 던집니다. 나머지(요약·교차참조·정리·기록)는 LLM이 합니다.

## 폴더 구조

```
mywiki/
├── CLAUDE.md          ← 스키마(설정). LLM에게 위키 운영 규칙을 알려줌
├── README.md          ← 이 문서
├── raw/               ← 원본 소스 (불변, LLM은 읽기만 함)
│   └── assets/        ← 이미지 등 첨부파일 (Obsidian 다운로드 대상 폴더)
└── wiki/              ← LLM이 생성·유지하는 마크다운 (당신은 읽고, LLM이 씀)
    ├── index.md       ← 내용 카탈로그 (모든 페이지 목록 + 한 줄 요약)
    ├── log.md         ← 시간순 기록 (ingest/query/lint 로그, append-only)
    ├── overview.md    ← 전체 개요 / 진화하는 종합(synthesis)
    ├── entities/      ← 개체 페이지 (사람·제품·조직·장소 등)
    ├── concepts/      ← 개념 페이지 (주제·아이디어·이론 등)
    └── sources/       ← 소스별 요약 페이지 (raw/ 의 각 소스에 대응)
```

## 세 개의 레이어

1. **Raw sources** (`raw/`) — 큐레이션한 원본. 불변(immutable). 진실의 원천(source of truth).
2. **The wiki** (`wiki/`) — LLM이 전적으로 소유. 요약·개체·개념·비교·종합 페이지.
3. **The schema** (`CLAUDE.md`) — LLM을 "규율 있는 위키 관리자"로 만드는 핵심 설정 파일. 도메인에 맞게 당신과 LLM이 함께 진화시킴.

## 세 가지 운영(Operations)

- **Ingest(수집)** — `raw/`에 소스를 넣고 LLM에게 처리를 지시. LLM이 읽고 → 핵심을 논의 → 소스 요약 페이지 작성 → index 갱신 → 관련 개체·개념 페이지 갱신 → log에 기록. 소스 하나가 10~15개 페이지를 건드릴 수 있음.
- **Query(질의)** — 위키에 질문. LLM이 index를 먼저 읽고 → 관련 페이지를 찾아 → 인용과 함께 답변 종합. 좋은 답변은 새 페이지로 위키에 다시 보관(compounding).
- **Lint(점검)** — 주기적으로 위키 건강검진. 모순·낡은 주장·고아 페이지(inbound link 없음)·누락된 교차참조·빠진 페이지·데이터 공백을 점검.

## 시작하는 법

1. `raw/`에 첫 소스를 넣습니다 (Obsidian Web Clipper로 웹 글을 마크다운으로 저장하면 편리).
2. LLM 에이전트에게: *"raw/에 있는 새 소스를 ingest 해줘"* 라고 지시.
3. Obsidian을 열어 graph view로 위키가 자라는 모습을 실시간으로 확인.

자세한 운영 규칙은 [[CLAUDE]] 를 참고하세요. 전체 페이지 목록은 [[wiki/index|index]], 변경 이력은 [[wiki/log|log]] 에 있습니다.

## Obsidian 팁

- **Web Clipper**: 웹 글 → 마크다운 변환 브라우저 확장. `raw/`로 빠르게 소스 수집.
- **이미지 로컬 저장**: Settings → Files and links → "Attachment folder path"를 `mywiki/raw/assets/`로 지정. Hotkeys에서 "Download attachments for current file"를 단축키(예: Ctrl+Shift+D)로 바인딩.
- **Graph view**: 위키의 구조(허브/고아 페이지)를 한눈에.
- **Dataview / Marp 플러그인**: frontmatter 기반 동적 테이블, 마크다운 슬라이드 생성.
- 위키는 결국 마크다운 git 저장소 — 버전 관리·브랜치·협업이 공짜.
