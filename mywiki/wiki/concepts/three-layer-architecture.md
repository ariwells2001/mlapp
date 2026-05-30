---
title: 3-Layer Architecture (raw / wiki / schema)
type: concept
created: 2026-05-30
updated: 2026-05-30
tags: [architecture, structure]
sources: [llm-wiki-pattern]
---

# 3-Layer Architecture

[[llm-wiki]]를 이루는 세 개의 레이어. (출처: [[llm-wiki-pattern]])

## 1. Raw sources (`raw/`)
큐레이션한 원본 문서 — 기사, 논문, 이미지, 데이터. **불변(immutable)**: LLM은 읽기만 하고 절대 수정하지 않는다. **진실의 원천(source of truth)**.

## 2. The wiki (`wiki/`)
LLM이 생성하는 마크다운 — 소스 요약, [[entities|개체 페이지]], 개념 페이지, 비교, overview, 종합. **LLM이 전적으로 소유**: 페이지를 만들고, 새 소스가 오면 갱신하고, 교차참조를 유지하며 일관성을 지킨다. 사람은 읽고, LLM은 쓴다.

## 3. The schema (`CLAUDE.md` / `AGENTS.md`)
위키 구조·관례·워크플로(수집·질의·유지)를 LLM에게 알려주는 **핵심 설정 파일**. LLM을 일반 챗봇이 아니라 **규율 있는 위키 관리자**로 만든다. 사람과 LLM이 도메인에 맞게 함께 진화시킨다. → 이 vault의 스키마: [[CLAUDE]]

## 데이터 흐름
```
raw/ (불변, 사람이 투입)  ──읽기──▶  LLM ──쓰기──▶  wiki/ (LLM 소유)
                                   ▲
                              CLAUDE.md (규칙)
```

관련: [[llm-wiki]] · [[ingest-query-lint]] · [[index-and-log]]
