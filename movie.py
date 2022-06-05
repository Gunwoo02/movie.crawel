#이태균-역대박스오피스 영화 제목 크롤링 후 100위까지 출력
!pip install selenium
!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin

import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=options)

URL = 'https://www.kobis.or.kr/kobis/business/stat/offc/findFormerBoxOfficeList.do'
driver.get(url=URL)

movie_title = driver.find_elements_by_class_name('boxMNm')
#영화 제목 크롤링

title=[]
ranking=[]
rank=1
for i in movie_title :
  title.append(i.text)
  ranking.append(rank)
  rank+=1
title=title[:100]
ranking=ranking[:100]
#print(title)-영화 제목
#print(ranking)-영화 순위

for i in range(len(title)) :
  print(f'{ranking[i]}등 : {title[i]}')
#역대 100위까지의 영화 출력

#김건우-원하는 순위의 영화 정보 출력
movie_information = driver.find_elements_by_class_name("rowGroup")
 
information=[]
for i in movie_information :
  information.append(i.text)
information=information[:100]
#print(information)-박스오피스 순위의 영화 정보 크롤링(순위 영화명 개봉일 매출액 관객수 스크린수)

movie_want=list(map(int,input('순위를 입력하시오(순위 영화명 개봉일 매출액 관객수 스크린수) : ').split()))
for i in movie_want :
  print(information[i-1])
  print('')
#원하는 순위의 영화 정보 출력
