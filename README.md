# Blinker-AI
for LikeLion-13 boogi-thon

## 🛠️ 가상환경 관리 가이드 (Windows & macOS)

이 프로젝트는 Python 가상환경 기반으로 구성되어 있으며, 누구나 동일한 환경에서 실행할 수 있도록 다음 절차에 따라 설정해주세요.

--- 
## ✅ 1. 가상환경 생성 (최초 1회만)

Python 3.10 기준으로 가상환경을 생성합니다:

```bash
python3.10 -m venv venv
```

---

## ✅ 2. 가상환경 실행

| 운영체제     | 명령어                       |
|--------------|------------------------------|
| **Windows**  | `venv\Scripts\activate`      |
| **macOS/Linux** | `source venv/bin/activate` |

---

## ✅ 3. 가상환경 종료

가상환경을 종료하려면 운영체제와 관계없이 아래 명령어를 입력하세요:

```bash
deactivate
```

---

## ✅ 4. 새로운 라이브러리 설치 후 `requirements.txt`에 저장

필요한 라이브러리를 설치한 후 다음 명령어로 `requirements.txt`를 갱신합니다:

```bash
pip freeze > requirements.txt
```

---