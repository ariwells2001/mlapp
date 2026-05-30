---
title: qmd
type: entity
created: 2026-05-30
updated: 2026-05-30
tags: [tool, software, search]
sources: [llm-wiki-pattern]
---

# qmd

마크다운 파일을 위한 **로컬 검색 엔진**. 하이브리드 BM25/벡터 검색 + LLM 재랭킹을 모두 **온디바이스**로 수행. CLI(셸로 호출)와 MCP 서버(네이티브 도구로 사용) 둘 다 제공. (출처: [[llm-wiki-pattern]])

## 이 위키에서의 역할
[[llm-wiki]]가 커지면 [[index-and-log|index 파일]]만으로 부족할 수 있다. 소규모에선 index로 충분하지만, 수백 페이지 규모가 되면 제대로 된 검색이 필요 — qmd가 그 후보(선택사항, optional CLI tools). 더 단순하게 직접 검색 스크립트를 vibe-code 해도 됨.
→ 이 vault에 도입하면 [[CLAUDE]] §7에 사용법을 기록할 것.

관련: [[llm-wiki]] · [[index-and-log]] · [[obsidian]]
