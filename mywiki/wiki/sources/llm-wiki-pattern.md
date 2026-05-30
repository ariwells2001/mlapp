---
title: "Source — LLM Wiki (a pattern for LLM-built knowledge bases)"
type: source
created: 2026-05-30
updated: 2026-05-30
tags: [knowledge-management, llm, obsidian, pkm]
sources: [llm-wiki-pattern]
source_path: raw/llm-wiki-pattern.md
source_type: article
source_date: 2026
ingested: 2026-05-30
---

# Source — LLM Wiki

LLM이 직접 쓰고 유지하는 **개인 지식 베이스** 구축 패턴을 설명하는 아이디어 문서. 이 위키(`mywiki`) 자체가 이 문서를 본떠 만들어졌다.

## 핵심 주장 (3줄)
1. RAG는 질문할 때마다 원문에서 지식을 **매번 재발견**한다 — 누적이 없다. 대신 LLM이 **지속적으로 누적되는 위키**를 점진적으로 구축·유지하면, 지식을 한 번 컴파일해 두고 최신 상태로 유지한다. (→ [[retrieval-augmented-generation]] vs [[llm-wiki]])
2. 위키 유지의 진짜 비용은 읽기·사고가 아니라 **bookkeeping**(교차참조 갱신, 요약 최신화, 모순 표시, 일관성 유지)이다. 인간은 이 부담 때문에 위키를 버린다. LLM은 지치지 않고 한 번에 15개 파일을 건드릴 수 있어 유지비가 0에 가깝다.
3. 역할 분담: **사람**은 소스 큐레이션·탐색·좋은 질문·의미 해석, **LLM**은 나머지 전부.

## 핵심 포인트
- **3개 레이어**: 불변 원본(raw) / LLM 소유 위키(wiki) / 스키마 설정(CLAUDE.md). 자세히 → [[three-layer-architecture]]
- **3가지 운영**: Ingest · Query · Lint. 자세히 → [[ingest-query-lint]]
- **2개 특수 파일**: 내용 카탈로그 `index.md`(질의 시 먼저 읽음) + 시간순 `log.md`(append-only, 일관된 prefix로 unix 파싱). 자세히 → [[index-and-log]]
- **누적성(compounding)**: 질의에 대한 좋은 답도 새 페이지로 위키에 보관 → 탐색이 소스처럼 쌓인다.
- **도구**: [[obsidian]]을 IDE처럼 사용(graph view·Web Clipper·Marp·Dataview). 검색이 필요해지면 [[qmd]] 같은 로컬 검색엔진 도입.
- **지적 계보**: [[vannevar-bush]]의 [[memex]](1945)와 같은 정신 — 사적이고 능동적으로 큐레이션되는 지식 저장소. Bush가 못 푼 "누가 유지하나" 문제를 LLM이 해결.
- 문서는 의도적으로 **추상적**: 디렉터리 구조·페이지 형식·도구는 도메인과 취향에 따라 LLM과 함께 인스턴스화하라는 입장.

## 적용 맥락 (예시)
개인(목표·건강·자기계발), 리서치(수개월 심층 탐구), 책 읽기(팬 위키처럼 인물·테마·플롯 페이지 — 예: Tolkien Gateway), 비즈니스/팀(Slack·회의록·고객 콜로 유지되는 내부 위키), 경쟁 분석·실사·여행 계획·강의 노트·취미 등.

## 인용할 만한 구절
> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."
> "LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass."
> "The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else."

## 비판적 메모
- **검증되지 않은 규모 주장**: "~100 소스, 수백 페이지 규모에서 index만으로 잘 작동"은 저자의 경험적 주장이며, 도메인·페이지 밀도에 따라 다를 수 있음.
- **부록의 [[swarmvault]] 댓글**은 핵심 아이디어가 아니라 특정 상용 CLI 도구 홍보 — 같은 패턴의 상용 구현 사례로만 참고.

## 출처
- 원본: `raw/llm-wiki-pattern.md` (아이디어 공유 문서, 2026, 작성자 미상)
- 관련 개념: [[llm-wiki]] · [[three-layer-architecture]] · [[ingest-query-lint]] · [[index-and-log]] · [[retrieval-augmented-generation]] · [[memex]]
- 관련 개체: [[obsidian]] · [[qmd]] · [[vannevar-bush]] · [[swarmvault]]
