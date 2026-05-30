---
title: Retrieval-Augmented Generation (RAG)
type: concept
created: 2026-05-30
updated: 2026-05-30
tags: [llm, retrieval, rag, contrast]
sources: [llm-wiki-pattern]
---

# Retrieval-Augmented Generation (RAG)

질의 시점에 문서 컬렉션에서 관련 청크를 **검색(retrieve)**해 LLM이 답을 **생성**하는 방식. 파일을 업로드해 두면 질문마다 관련 조각을 찾아 답한다. NotebookLM, ChatGPT 파일 업로드, 대부분의 RAG 시스템이 이 방식. (출처: [[llm-wiki-pattern]])

## [[llm-wiki]]가 지적하는 한계
- LLM이 **매 질문마다 지식을 처음부터 재발견** — 누적이 없다.
- 5개 문서를 종합해야 하는 미묘한 질문이면, 매번 관련 조각을 찾아 짜맞춰야 한다.
- 쌓이는 것이 없다: 교차참조도, 모순 표시도, 종합도 매번 휘발.

## 대비
| | RAG | [[llm-wiki]] |
|---|---|---|
| 지식 처리 시점 | 질의 시 매번 | 수집 시 1회 컴파일 |
| 누적 | 없음 | 영속·복리(compounding) |
| 교차참조/모순 | 매번 재구성 | 위키에 이미 존재 |
| 인프라 | 임베딩/벡터DB | 마크다운 + index 파일(중간 규모) |

> ⚠️ 균형: LLM Wiki는 RAG를 완전히 부정하지 않는다. 규모가 커지면 위키 위에 검색([[qmd]], BM25/벡터)을 얹어 보완할 수 있다 — 즉 둘은 배타적이지 않다.

관련: [[llm-wiki]] · [[index-and-log]]
