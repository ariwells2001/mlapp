# raw/ — 원본 소스 (immutable)

여기에 **원본 소스**를 넣습니다. 기사, 논문, PDF, 트랜스크립트, 이미지, 데이터 파일 등.

규칙:
- 이 폴더는 **진실의 원천(source of truth)**입니다.
- LLM은 여기서 **읽기만** 하고 **절대 수정하지 않습니다**.
- 위키 가공물은 `../wiki/`에 생성됩니다.

수집 방법:
- **Obsidian Web Clipper**로 웹 글을 마크다운으로 저장해 이 폴더에 넣으면 편리합니다.
- 이미지는 `assets/`에 저장됩니다 (Obsidian Attachment folder path를 `mywiki/raw/assets/`로 지정).

소스를 넣은 뒤 LLM에게: **"raw/에 있는 새 소스를 ingest 해줘"**
