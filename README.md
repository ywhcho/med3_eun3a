# med3_eun3a - 의약정보 관리 시스템

Django와 MySQL을 사용한 의약품 정보 관리 웹사이트입니다.

## 📋 주요 기능

### 1. 회원 관리
- 회원가입 및 로그인/로그아웃
- 회원정보 수정 (이메일, 비밀번호)
- Django User 모델 기반 인증 시스템

### 2. 의약정보 보기
- **검색 기능**: 성분명, 회사명, 효능별 검색
- **페이지네이션**: 10개씩 페이지 구분
- **상세 정보**: 약품명, 성분명, 효능, 용량, 주의사항, 회사명

### 3. 게시판
- 게시글 작성, 수정, 삭제 (로그인 필수)
- 게시글 조회 (조회수 자동 증가)
- 작성자만 수정/삭제 가능

### 4. About Us
- 회사 소개 페이지 ("의약품 안전사용 전문회사")

## 🛠 기술 스택

- **Backend**: Django 6.0.1
- **Database**: MySQL (또는 SQLite for development)
- **Frontend**: Bootstrap 5.3.0
- **Language**: Python 3.12+

## 📦 설치 방법

### 1. 저장소 클론

```bash
git clone https://github.com/ywhcho/med3_eun3a.git
cd med3_eun3a
```

### 2. 가상환경 생성 및 활성화

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 데이터베이스 설정

#### SQLite 사용 (개발용 - 기본 설정)
현재 설정으로 바로 사용 가능합니다.

#### MySQL 사용 (프로덕션)

1. MySQL 데이터베이스 생성:
```sql
CREATE DATABASE med3_eun3a CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'your_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON med3_eun3a.* TO 'your_user'@'localhost';
FLUSH PRIVILEGES;
```

2. `config/settings.py` 파일에서 DATABASES 설정 변경:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'med3_eun3a',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
```

### 5. 마이그레이션 실행

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. 관리자 계정 생성

```bash
python manage.py createsuperuser
```

### 7. (선택사항) 샘플 데이터 생성

```bash
python create_sample_data.py
```

이 스크립트는 다음을 생성합니다:
- 관리자 계정: admin / admin123
- 테스트 사용자: testuser / test123
- 12개의 샘플 의약품 정보
- 3개의 샘플 게시글

### 8. 개발 서버 실행

```bash
python manage.py runserver
```

브라우저에서 `http://127.0.0.1:8000/` 접속

## 📁 프로젝트 구조

```
med3_eun3a/
├── manage.py
├── requirements.txt
├── create_sample_data.py       # 샘플 데이터 생성 스크립트
├── config/                     # 프로젝트 설정
│   ├── settings.py            # Django 설정
│   ├── urls.py                # 메인 URL 라우팅
│   └── wsgi.py
├── accounts/                   # 회원 관리 앱
│   ├── models.py              # (Django User 모델 사용)
│   ├── views.py               # 회원가입, 로그인, 프로필
│   └── urls.py
├── board/                      # 게시판 앱
│   ├── models.py              # Post 모델
│   ├── views.py               # 게시글 CRUD
│   ├── admin.py               # 관리자 페이지 설정
│   └── urls.py
├── medicine/                   # 의약정보 앱
│   ├── models.py              # Medicine 모델
│   ├── views.py               # 의약품 목록, 검색, 상세
│   ├── admin.py               # 관리자 페이지 설정
│   └── urls.py
├── pages/                      # 정적 페이지
│   ├── views.py               # About Us, Home
│   └── urls.py
├── templates/                  # 템플릿 파일
│   ├── base.html              # 베이스 템플릿 (네비게이션 포함)
│   ├── home.html              # 홈페이지
│   ├── accounts/              # 회원 관리 템플릿
│   ├── board/                 # 게시판 템플릿
│   ├── medicine/              # 의약정보 템플릿
│   └── pages/                 # 정적 페이지 템플릿
└── static/                     # 정적 파일
    ├── css/
    └── js/
```

## 🎯 주요 URL

- 홈페이지: `/`
- 의약정보 보기: `/medicine/`
- 게시판: `/board/`
- About Us: `/pages/about/`
- 로그인: `/accounts/login/`
- 회원가입: `/accounts/signup/`
- 관리자 페이지: `/admin/`

## 💡 사용 방법

### 의약품 검색
1. 의약정보 보기 메뉴 클릭
2. 검색 유형 선택 (성분명/회사명/효능)
3. 검색어 입력 후 검색 버튼 클릭
4. 의약품 목록에서 원하는 항목 클릭하여 상세 정보 확인

### 게시글 작성
1. 로그인 필요
2. 게시판 메뉴 클릭
3. 글쓰기 버튼 클릭
4. 제목과 내용 입력 후 작성

### 관리자 페이지에서 데이터 관리
1. `/admin/` 접속
2. 슈퍼유저 계정으로 로그인
3. Medicine, Post 모델에서 데이터 추가/수정/삭제

## 🔒 보안 기능

- CSRF 보호 활성화
- 비밀번호 해싱 (Django 기본 설정)
- 로그인 필수 데코레이터 (@login_required)
- 작성자 권한 확인 (게시글 수정/삭제)

## 🌐 반응형 디자인

Bootstrap 5를 사용하여 모바일, 태블릿, 데스크톱 모든 기기에서 최적화된 UI 제공

## 📝 라이선스

이 프로젝트는 교육 목적으로 작성되었습니다.

## 👥 기여

프로젝트에 기여하고 싶으시다면 Pull Request를 보내주세요.

## 📧 문의

프로젝트 관련 문의사항은 GitHub Issues를 통해 남겨주세요.

