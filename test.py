from bs4 import BeautifulSoup
import urllib.request

keyword = '휴학'
url = 'https://www.jbnu.ac.kr/web/news/notice/sub01.do?menu=2377'
response = urllib.request.urlopen(url)
html_content = response.read()

soup = BeautifulSoup(html_content, 'html.parser')

filtered_a_tags = [tag for tag in soup.find_all('a', class_='title') if keyword.lower() in tag.get_text().lower()]

for a_tag in filtered_a_tags:
    # 고유 번호
    no_index = int(a_tag.get('onclick', '').split('(')[-1].split(')')[0].strip("'"))
    # 공지 제목
    notice_title = a_tag.get_text(strip=True)
    # 공지 세부내용 url
    detail_url = f'https://www.jbnu.ac.kr/web/Board/{no_index}/detailView.do?pageIndex=1&menu=2377'

    print((no_index, notice_title, detail_url))
