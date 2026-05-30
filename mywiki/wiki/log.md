---
title: Log
type: overview
created: 2026-05-30
updated: 2026-05-30
tags: [meta, log]
---

# Log — 시간순 활동 기록

Append-only. 각 항목은 일관된 prefix로 시작합니다 → `grep "^## \[" log.md | tail -5` 로 최근 활동 확인.

형식:
```
## [YYYY-MM-DD] ingest | <소스 제목>
## [YYYY-MM-DD] query  | <질문 요약>
## [YYYY-MM-DD] lint   | <점검 결과 요약>
```

---

## [2026-05-30] init | mywiki 위키 초기 구조 생성 (raw/, wiki/, CLAUDE.md, index, log, overview)
## [2026-05-30] ingest | LLM Wiki (a pattern for LLM-built knowledge bases) — 소스 1개. 생성: sources/llm-wiki-pattern, concepts(llm-wiki, retrieval-augmented-generation, three-layer-architecture, ingest-query-lint, index-and-log, memex), entities(vannevar-bush, obsidian, qmd, swarmvault). overview·index 갱신. 11개 페이지 생성/갱신.
