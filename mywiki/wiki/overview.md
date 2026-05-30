---
title: Overview
type: overview
created: 2026-05-30
updated: 2026-05-30
tags: [meta, overview, synthesis]
sources: [llm-wiki-pattern]
---

# Overview — 진화하는 종합(Synthesis)

이 페이지는 위키 전체를 관통하는 **현재까지의 종합**입니다. 새 소스가 수집될 때마다 갱신됩니다.

## 현재 상태
소스 1개 수집됨 — [[llm-wiki-pattern]]. 이 vault는 그 문서가 설명하는 패턴([[llm-wiki]])을 **자기 자신에게 적용한** 첫 사례다(self-referential first ingest).

## 핵심 주제 (Themes)
- **누적 vs 재발견**: [[llm-wiki]]의 본질은 지식을 영속적·복리적으로 쌓는 것. 질의마다 처음부터 재발견하는 [[retrieval-augmented-generation]]과 대비된다.
- **유지비를 0으로**: 위키가 실패하는 이유는 읽기가 아니라 bookkeeping 부담. LLM이 그 부담을 떠안아 위키를 살아있게 한다. 이것이 [[memex]](1945)가 못 푼 문제의 해답.
- **구조가 규율을 만든다**: [[three-layer-architecture]](raw/wiki/schema) + [[ingest-query-lint]](운영) + [[index-and-log]](항법). 스키마([[CLAUDE]])가 LLM을 일반 챗봇이 아닌 규율 있는 관리자로 만든다.
- **모듈성**: 모든 요소는 선택적. 도메인·취향에 맞춰 인스턴스화한다.

## 열린 질문 (Open questions)
- 이 vault를 어떤 도메인(개인/리서치/업무 등)에 특화할 것인가? → [[CLAUDE]] §8에 기록 예정.
- 규모가 커지면 [[qmd]] 같은 검색을 도입할 것인가, 언제?
- 휴대폰 vault ↔ 저장소 동기화의 최종 방식(현재: 채팅 붙여넣기 + git pull).

## 미해결 모순 (Open contradictions)
- 없음 (소스 1개).

---
관련: [[index]] · [[log]] · [[CLAUDE]]
