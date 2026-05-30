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

## 이 vault 사용법 (현재 설정)

이 폴더(`mywiki`)는 **그 자체로 하나의 Obsidian vault**입니다.
휴대폰 Obsidian에서 **`Documents` 안의 이 `mywiki` 폴더를 vault로 열면**, Obsidian 입장에서 루트가 곧 위키가 됩니다.

소스 투입 방식은 **"채팅에 붙여넣기"**로 합니다:

1. 읽은 글·메모·파일 내용을 **LLM 채팅창에 붙여넣고** "이거 ingest 해줘"라고 말합니다.
2. LLM이 그 내용을 `raw/`에 소스 파일로 저장하고, `wiki/`에 요약·개체·개념 페이지를 만들고, `index`·`log`·`overview`를 갱신한 뒤 git에 push 합니다.
3. 휴대폰에서 저장소를 pull(또는 동기화)하면 새 위키 페이지가 Obsidian에 나타납니다. graph view로 자라는 모습을 확인하세요.

> 질문도 같은 방식입니다: 채팅에 질문하면 LLM이 위키를 읽고 인용과 함께 답하며, 좋은 답은 새 페이지로 위키에 보관합니다.

## 시작하는 법

1. 첫 소스(글/메모/데이터)의 내용을 채팅에 붙여넣고 "ingest 해줘"라고 말합니다.
2. LLM이 위키를 생성·갱신하고 push 합니다.
3. 휴대폰 Obsidian에서 pull/동기화하여 결과를 확인합니다.

자세한 운영 규칙은 [[CLAUDE]] 를 참고하세요. 전체 페이지 목록은 [[index]], 변경 이력은 [[log]] 에 있습니다.

## Obsidian 팁

- **Web Clipper**: 웹 글 → 마크다운 변환 브라우저 확장. `raw/`로 빠르게 소스 수집.
- **이미지 로컬 저장**: Settings → Files and links → "Attachment folder path"를 `mywiki/raw/assets/`로 지정. Hotkeys에서 "Download attachments for current file"를 단축키(예: Ctrl+Shift+D)로 바인딩.
- **Graph view**: 위키의 구조(허브/고아 페이지)를 한눈에.
- **Dataview / Marp 플러그인**: frontmatter 기반 동적 테이블, 마크다운 슬라이드 생성.
- 위키는 결국 마크다운 git 저장소 — 버전 관리·브랜치·협업이 공짜.
