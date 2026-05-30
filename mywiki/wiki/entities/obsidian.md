---
title: Obsidian
type: entity
created: 2026-05-30
updated: 2026-05-30
tags: [tool, software, obsidian]
sources: [llm-wiki-pattern]
---

# Obsidian

마크다운 기반 노트 앱. [[llm-wiki]] 패턴에서 사람이 위키를 **읽고 탐색하는 인터페이스**로 쓰인다. "Obsidian은 IDE, LLM은 프로그래머, 위키는 코드베이스." (출처: [[llm-wiki-pattern]])

## 이 위키에서의 역할
LLM이 대화에 따라 위키를 편집하면, 사람은 Obsidian에서 링크를 따라가고 graph view를 보며 갱신된 페이지를 실시간으로 읽는다. 이 vault(`mywiki`)는 Obsidian vault로 직접 열도록 구성됨. → [[README]]

## 언급된 기능·플러그인
- **Web Clipper**: 웹 글 → 마크다운 변환 브라우저 확장. `raw/`로 소스 빠르게 수집.
- **이미지 로컬 저장**: Settings → Files and links의 Attachment folder path를 고정 폴더(예: `raw/assets/`)로, Hotkeys에서 "Download attachments for current file"를 단축키 바인딩.
- **Graph view**: 위키의 구조(허브/고아 페이지)를 시각화. [[memex]]의 연상 경로의 디지털 구현.
- **Marp**: 마크다운 슬라이드 덱 플러그인. 위키 내용으로 발표자료 생성.
- **Dataview**: frontmatter(태그·날짜·소스 수) 기반 동적 테이블/리스트.

## 메모
- LLM은 인라인 이미지가 박힌 마크다운을 한 번에 못 읽음 → 텍스트를 먼저 읽고 이미지를 따로 보는 우회가 필요(원본 문서의 팁).

관련: [[llm-wiki]] · [[qmd]]
