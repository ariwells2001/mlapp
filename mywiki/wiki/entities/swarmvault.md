---
title: SwarmVault
type: entity
created: 2026-05-30
updated: 2026-05-30
tags: [tool, software, commercial, third-party]
sources: [llm-wiki-pattern]
---

# SwarmVault

[[llm-wiki]] 패턴을 패키징한 **상용 CLI 도구**(`@swarmvaultai/cli`). 원본 문서 본문이 아니라 GitHub **댓글(@waydelyle)**에서 홍보된 third-party 도구. (출처: [[llm-wiki-pattern]] 부록 댓글)

## 주장하는 워크플로
1. `npx @swarmvaultai/cli init` → `raw/`, `wiki/`, 스키마 파일 생성 (API 키 불필요).
2. `swarmvault source add` / `ingest` → 50+ 포맷(코드 AST 분석, PDF·트랜스크립트·YouTube·오디오) 추출·구조화.
3. `swarmvault compile` → 위키 페이지 + 지식 그래프 + 검색 인덱스 + **모순 탐지** + 공유 카드 생성. 출력은 `wiki/`의 순수 마크다운.
4. `swarmvault context build/query/graph` → 에이전트에 **bounded context** 제공, 태스크 ledger로 세션 간 작업 기억.
5. `swarmvault watch` → git 커밋 시 자동 갱신. `doctor`/`graph serve`/`install --agent` 등.
- 모두 로컬, 임의 LLM 제공자 또는 오프라인. Repo: github.com/swarmclawai/swarmvault

## 위치 / 주의
- [[llm-wiki]] 패턴의 **상용 자동화 구현 사례**로만 참고. 핵심 아이디어와는 별개이며, 본 vault는 이 도구에 의존하지 않는다.
- ⚠️ 출처가 홍보성 댓글이라 기능 주장은 **미검증**. 실제 도입 전 직접 확인 필요.

관련: [[llm-wiki]] · [[ingest-query-lint]]
