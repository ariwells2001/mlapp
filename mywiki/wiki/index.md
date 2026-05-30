---
title: Index
type: overview
created: 2026-05-30
updated: 2026-05-30
tags: [meta, index]
---

# Index — mywiki 카탈로그

위키의 모든 페이지 목록입니다. 질의 시 LLM이 가장 먼저 읽는 파일이며, 매 ingest마다 갱신됩니다.
각 줄: `[[링크]] — 한 줄 요약`.

> 시작 안내: [[overview]] 부터 읽으세요. 운영 규칙은 [[CLAUDE]], 변경 이력은 [[log]] 에 있습니다.

## Overview
- [[overview]] — 위키 전체를 관통하는 진화하는 종합. (소스 1개 반영)

## Sources
- [[llm-wiki-pattern]] — LLM이 직접 쓰고 유지하는 개인 지식 베이스 구축 패턴(아이디어 문서). 이 vault의 모태. (2026, article)

## Entities
- [[obsidian]] — 위키를 읽고 탐색하는 마크다운 노트 앱. "IDE" 역할. (tool)
- [[qmd]] — 마크다운용 로컬 검색 엔진(BM25/벡터+재랭킹, CLI/MCP). 규모 확장 시 선택지. (tool)
- [[swarmvault]] — LLM Wiki 패턴의 상용 CLI 구현(third-party, 홍보성·미검증). (tool)
- [[vannevar-bush]] — [[memex]](1945)를 구상한 엔지니어. 패턴의 지적 계보. (person)

## Concepts
- [[llm-wiki]] — LLM이 유지하는 영속·누적 지식 베이스 패턴. (core)
- [[retrieval-augmented-generation]] — 질의 시점에 원문을 검색해 답을 생성하는 대비 개념(RAG).
- [[three-layer-architecture]] — raw(불변) / wiki(LLM 소유) / schema(설정)의 3개 레이어.
- [[ingest-query-lint]] — 위키 운영 3동작: 수집 / 질의 / 점검.
- [[index-and-log]] — 항법용 두 특수 파일: 내용 카탈로그(index) / 시간순 로그(log).
- [[memex]] — Vannevar Bush의 1945년 개인 지식 저장 구상. 패턴의 선조.
