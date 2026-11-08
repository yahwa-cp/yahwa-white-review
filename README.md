# 야화 · 그림 없는 흰 배경 비교

GPT Site의 원본 HTML/CSS/JavaScript 및 이미지·폰트 전체 소스입니다.

- 원본 커밋: `e7f75b1aa7dcfcb5c45b7a0a135e732c582bdd8b`
- 실행 사이트: https://yahwa-white-review-nov06.yahwacompany-8958.chatgpt.site
- GitHub 웹 업로드의 파일 크기 제한 때문에 원본 파일을 여러 ZIP에 나눠 담았습니다. 각 ZIP은 독립 압축 파일이며, **모두 같은 폴더에 압축 해제**하면 원본 디렉터리 구조가 복원됩니다.
- 인증정보·Git 이력·Sites 호스팅 식별 설정은 포함하지 않았습니다.

## 다운로드 및 실행

1. Code → Download ZIP으로 내려받고 압축을 풉니다.
2. `yahwa-source-*.zip`을 모두 같은 폴더에 압축 해제합니다. 또는 아래 명령을 실행합니다.

```sh
python extract-source.py
python -m http.server 8000 --directory app
```

3. 브라우저에서 http://localhost:8000 을 엽니다.

`app/index.html`이 메인 화면이고 `app/` 안에 스타일·스크립트·이미지·폰트가 들어 있습니다. 별도의 npm 빌드 없이 실행하는 정적 시안입니다. 외부 서비스나 실제 운영 서버 기능까지 복제한 것은 아닙니다.
