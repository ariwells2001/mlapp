---
title: LLM Wiki (패턴)
type: concept
created: 2026-05-30
updated: 2026-05-30
tags: [knowledge-management, llm, pkm, core]
sources: [llm-wiki-pattern]
---

# LLM Wiki

LLM이 직접 쓰고 유지·관리하는 **지속적·누적적 개인 지식 베이스 패턴**. 서로 연결된 마크다운 파일들의 집합이 당신과 원본 소스 사이에 놓이며, 새 소스가 들어올 때마다 LLM이 읽고 통합하여 위키를 점점 풍부하게 만든다. (출처: [[llm-wiki-pattern]])

## RAG와의 핵심 차이
[[retrieval-augmented-generation]]은 질의 시점에 원문 청크를 검색해 답을 생성 — 매 질문마다 지식을 처음부터 재발견하고 **누적이 없다**. LLM Wiki는 소스를 **한 번 컴파일**해 위키에 통합해 두고 최신 상태로 유지한다. 교차참조·모순 표시·종합이 이미 위키 안에 존재한다.

## 구성
- 구조: [[three-layer-architecture]] (raw / wiki / schema)
- 운영: [[ingest-query-lint]] (수집 / 질의 / 점검)
- 항법(navigation): [[index-and-log]] (내용 카탈로그 / 시간순 로그)

## 왜 작동하나
위키 유지의 진짜 비용은 읽기·사고가 아니라 **bookkeeping**이다. 인간은 유지 부담이 가치보다 빨리 커져 위키를 버린다. LLM은 지치지 않고 교차참조를 빠뜨리지 않으며 한 번에 15개 파일을 갱신 → **유지비 ≈ 0**. (cf. [[memex]]가 못 푼 "누가 유지하나" 문제의 해답)

## 역할 분담
- 사람: 소스 큐레이션, 탐색 방향, 좋은 질문, 의미 해석.
- LLM: 요약·교차참조·정리·기록 등 나머지 전부.

## 실천
[[obsidian]]을 IDE처럼 한쪽에 띄우고 LLM을 다른 쪽에 띄워, 대화에 따라 LLM이 편집하고 사람은 graph view·링크를 실시간으로 따라가며 본다. 규모가 커지면 [[qmd]] 같은 검색 도구를 더한다. 상용 구현 예: [[swarmvault]].

관련: [[llm-wiki-pattern]] · [[memex]]
