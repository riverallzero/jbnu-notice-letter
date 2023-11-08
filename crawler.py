from bs4 import BeautifulSoup
import urllib.request
import smtplib
from email.mime.text import MIMEText
import os

# KEYWORD ========================================
# ================================================

keywords = ['해외', '해커톤', '연수']

# EMAIL ==========================================
# ================================================

email_address = os.environ.get('MAIL_ADDRESS')
email_password = os.environ.get('MAIL_PASSWORD')

# CODE ===========================================
# ================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, 'last_no.txt')

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        last_no_file = file.read().split(',')
        
        if len(keywords) == len(last_no_file):
            last_no_list = last_no_file
        else:
            last_no_list = [0 for i in range(len(keywords))]
else:
    last_no_list = [0 for i in range(len(keywords))]

url = 'https://www.jbnu.ac.kr/kor/?menuID=139'
response = urllib.request.urlopen(url)
html_content = response.read()

soup = BeautifulSoup(html_content, 'html.parser')

last_nums = []
for idx, keyword in enumerate(keywords):
    new_notices = []

    last_no = int(list(last_no_list)[idx])
    for a_tag in soup.find_all(
            'a',
            href=lambda href: href and href.startswith('?menuID=139'),
            title=lambda title: title and keyword.lower() in title.lower(),
    ):
        if a_tag.find('span'):
            # 고유 번호
            no_index = int(a_tag['href'].split('=')[-1])
            # 공지 제목
            notice_title = a_tag['title'][:-5]
            # 공지 세부내용 url
            detail_url = f'https://www.jbnu.ac.kr/kor/?menuID=139&mode=view&no={no_index}'

            if last_no is None or no_index > last_no:
                new_notices.append((no_index, notice_title, detail_url))

    last_no = max(new_notices, key=lambda x: x[0])[0] if new_notices else last_no
    last_nums.append(str(last_no))

    if new_notices:
        contents = '<ul>'
        for notice in new_notices:
            contents += f'<li>{notice[1]}<a href="{notice[2]}">(바로가기)</a></li>'
        contents += '</ul>'

        msg = MIMEText(f'키워드 "{keyword}"에 대한 새로운 공지사항이 업데이트되었습니다. 아래에서 상세 내용을 확인해주세요. \n \n{contents}', 'html')
        msg['Subject'] = f'[{keyword}] 전북대학교 공지사항 새알림'
        msg['From'] = email_address
        msg['To'] = email_address

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(email_address, email_password)
        smtp.sendmail(email_address, email_address, msg.as_string())

        smtp.quit()

    new_notices.clear()

with open(file_path, 'w') as file:
    file.write(str(','.join(last_nums)))
