# So you wanna be a programmar?
![안선생님](https://raw.github.com/heejongahn/So-you-wanna-be-a-programmer/master/app/static/ahn_teacher.png)
허허허 이리 오거라.


## 목적
두 개의 목적을 가지고 이 프로젝트를 진행합니다.

1. 프로그래밍에 관심이 있는 사람들에게 단편적 기술 정보들이 아닌 큰 그림에 대한 지식 제공
2. 맨땅에서부터의 **실질적인** 웹 서비스 개발 프로세스를 경험

이 README 파일은 본 프로젝트의 스펙으로서 기능하며, 따라서 개발이 진행됨에 따라
그에 맞춰 지속적으로 업데이트됩니다.


## 콘텐츠 (추가 예정)
1. 파이썬 기초 : 자료형, 연산자, 함수, 조건문, 반복문, 파일 입출력, 예외처리 (아마 두 부분으로 나누어서)
2. 객체지향 프로그래밍, 클래스
3. 모듈화, 라이브러리 임포트
(추가 예정)

부록: Developer’s toolbox (Git, Github, Vim, zsh 등등.. 레퍼런스 주소만? 아니면
디테일한 설명까지?)


## 뷰 & 기능
1. 메인 페이지: 개요 및 시작하기 버튼(#1로 리다이렉트), 목차
2. 포스트: 이전 포스트, 다음 포스트로 넘어가는 버튼. 신택스 하이라이팅, 이미지, 외부 embedded 링크
3. 제안 및 콘택트 : 나의 정보

네비게이션 바: 홈 버튼, 포스트 탭(마우스 올리면 펼쳐짐), 제안 및 연락처 버튼


## DB 구조
Post 테이블 : id, 타이틀, 본문, 타임스탬프

그 외에 특별한 디비가 필요할까? 스태틱 파일들은 어떻게..


## 기술 스택
- Flask + SQLAlchemy
- Twitter Bootstrap + Font Awesome


## Someday...
- Heroku, Redis
- Smarter static files store
- Alter HTMl, CSS, JS with slim, sass, ls and preprocessors
- Manager page : To write/edit/delete posts via web. We don't need general user login, though...
- English support *(needed?)*
