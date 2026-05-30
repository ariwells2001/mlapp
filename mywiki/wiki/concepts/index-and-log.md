---
title: Indexing & Logging (index.md / log.md)
type: concept
created: 2026-05-30
updated: 2026-05-30
tags: [navigation, meta, structure]
sources: [llm-wiki-pattern]
---

# Indexing & Logging

[[llm-wiki]]가 커져도 항법(navigation)을 돕는 두 개의 특수 파일. 목적이 다르다. (출처: [[llm-wiki-pattern]])

## index.md — 내용 지향(content-oriented)
위키의 모든 것을 담은 **카탈로그**. 각 페이지를 링크 + 한 줄 요약 + (선택) 날짜·소스 수와 함께 나열. 카테고리(개체/개념/소스)별로 정리. **매 [[ingest-query-lint|ingest]]마다 갱신**. 질의 시 LLM이 **가장 먼저** 읽어 관련 페이지를 찾고 드릴다운.
→ 임베딩 기반 RAG 인프라 없이도 중간 규모(~100 소스, 수백 페이지)에서 잘 작동.
→ 이 vault의 색인: [[index]]

## log.md — 시간 지향(chronological)
무엇이 언제 일어났는지의 **append-only** 기록 — 수집·질의·점검.
팁: 각 항목을 일관된 prefix로 시작하면 unix 도구로 파싱 가능.
```
## [2026-04-02] ingest | Article Title
```
```
grep "^## \[" log.md | tail -5   # 최근 5개 활동
```
위키 진화의 타임라인을 주고, LLM이 최근 작업 맥락을 파악하게 돕는다.
→ 이 vault의 로그: [[log]]

## 대비
| | index.md | log.md |
|---|---|---|
| 관점 | 내용(무엇이 있나) | 시간(무엇을 했나) |
| 갱신 | 매 ingest 시 재구성 | append-only |
| 용도 | 질의의 진입점 | 진화 추적·맥락 |

관련: [[llm-wiki]] · [[ingest-query-lint]] · [[retrieval-augmented-generation]]
