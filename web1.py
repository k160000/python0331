# web1.py
from bs4 import BeautifulSoup

#문서를 로딩(문서 전체를 읽어서 문자열로 리턴): 메서드 체인 호출
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#전체 문서를 보기 
#print(soup.prettify())

#문서에 있는 <p>태그를 전부 가져오기
print(soup.find_all("p"))

