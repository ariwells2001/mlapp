---
title: Operations — Ingest / Query / Lint
type: concept
created: 2026-05-30
updated: 2026-05-30
tags: [operations, workflow]
sources: [llm-wiki-pattern]
---

# Operations — Ingest · Query · Lint

[[llm-wiki]]를 운영하는 세 가지 핵심 동작. (출처: [[llm-wiki-pattern]])

## Ingest (수집)
새 소스를 [[three-layer-architecture|raw 컬렉션]]에 넣고 LLM에게 처리를 지시.
예시 흐름: 소스 읽기 → 핵심 takeaway 논의 → 위키에 요약 페이지 작성 → [[index-and-log|index]] 갱신 → 관련 개체·개념 페이지 갱신 → [[index-and-log|log]]에 기록.
한 소스가 보통 **10~15개 페이지**를 건드린다. 한 번에 하나씩 검토하며 진행하거나(권장), 배치로 대량 수집도 가능.

## Query (질의)
위키에 질문 → LLM이 [[index-and-log|index]]를 먼저 읽어 관련 페이지를 찾고, 읽은 뒤 **인용과 함께** 답을 종합.
답변 형태는 다양: 마크다운, 비교 표, 슬라이드([[obsidian|Marp]]), 차트(matplotlib), 캔버스.
**핵심 통찰**: 좋은 답은 채팅에 묻히지 말고 **새 페이지로 위키에 보관** → 탐색이 소스처럼 누적(compounding).

## Lint (점검)
주기적 건강검진. 점검 항목:
- 페이지 간 **모순**
- 새 소스가 뒤집은 **낡은 주장**
- inbound 링크 없는 **고아 페이지**
- 자주 언급되나 자기 페이지가 없는 **누락 개념**
- **누락된 교차참조**
- 웹 검색으로 메울 **데이터 공백** → 새 질문·소스 제안

위키가 커져도 건강을 유지하게 한다.

관련: [[llm-wiki]] · [[index-and-log]] · [[three-layer-architecture]]
