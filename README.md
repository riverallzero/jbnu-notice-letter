# JBNU-NoticeLetter
| MONITORING | 오전 10시부터 오후 6시까지, 2시간 간격으로 받아보는 원하는 키워드에 관한 공지사항 뉴스레터

## Setting
⚠️ 본 저장소 클론하고 개별 설정한 이후 사용할 수 있습니다.

### GMail
- 메일 발신자에 한해 보안설정에 관해 2차 인증이 필요합니다.
  
1. 구글 계정관리에 들어가 왼쪽에 보안 메뉴를 클릭합니다.   
2. 2단계 인증 부분을 완료해줍니다.
   
   ![](https://github.com/riverallzero/riverallzero/assets/93754504/9df5d2a1-6923-413b-9a2c-f91748af9164)
   
3. "메일", "window컴퓨터"를 선택 앱 비밀번호를 설정합니다.
   
   ![](https://github.com/riverallzero/riverallzero/assets/93754504/1f242ae5-5eb3-4907-af13-850b0574a41b)

4. 생성된 비밀번호를 복사합니다
   
  ![](https://github.com/riverallzero/riverallzero/assets/93754504/1518e42a-202b-4e35-9b6c-649baa355b73)

### EMail Information
- ⚙︎ Settings - (Security) Secrets and variables - Actions - New repository secret
- Name이 'MAIL_SENDER', 'MAIL_PASSWORD', 'MAIL_RECEIVER'인 변수에 알맞은 값을 넣어 만들기
  - MAIL_SENDER: 메일 발신자
  - MAIL_PASSWORD: 발신자의 메일 비밀번호
  - MAIL_RECEIVER: 메일 수신자
     
  ![](https://github.com/riverallzero/riverallzero/assets/93754504/afb1d803-9dca-47c9-8a72-e1c1b5ff78ca)
  ![](https://github.com/riverallzero/riverallzero/assets/93754504/313f798d-f87a-41f8-85d7-25c6d4c6695d)

### Keyword 
- [crawler.py](https://github.com/riverallzero/JBNU-NoticeLetter/blob/main/crawler.py): line 11에 원하는 키워드 입력하기

  ```python
  # ================================================
  # KEYWORD ========================================
  # ================================================
  
  keyword = '안내'
  ```

### Reset last_no.txt
- [last_no.txt](https://github.com/riverallzero/JBNU-NoticeLetter/blob/main/last_no.txt): 최신 공지 번호 0으로 설정하기

## Result
![](https://github.com/riverallzero/riverallzero/assets/93754504/b0d4ca71-22a0-4d3a-9575-d52cd2d8050f)
