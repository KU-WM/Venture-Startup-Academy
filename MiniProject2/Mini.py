################################################
# Mini.py                                      #
# 뉴스 제목출력/ 검색 이미지, 동영상              #
# 다운로드 크롤링 코드                           #
#                                              #
# *중요*                                        #
# Chrome driver를 설치된 Chrome 버전에 맞게      #
# 설치 후 소스코드 위치에 옮겨 주어야 함          #
# 네이버 이미지검색, 구글 동영상 다운로드에       #
# 동적 크롤링을 사용하여 필수                    #
################################################

import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pytube import YouTube

# q로 종료할떄 까지 반복해서 동작
while True:
  query = input("검색할 단어를 입력하세요. q입력시 종료 : ")

  if(query == 'q'):
    break

  searchType = input("검색할 부분을 입력해 주세요. 뉴스/ 이미지/ 동영상 : ")

  if(searchType == '뉴스'):

    # 파싱할 url 생성 (네이버 뉴스탭의 url)
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=' + '%s'%query

    # 해당 url의 response를 확인
    response = requests.get(url)

    # 해당 url의 response를 text형식만 뽑아냄
    html_text = response.text

    # text형식의 response를 보기 현하게 바꿈
    html = bs(html_text, 'html.parser')

    # a(링크)태그의 news_tit라는 클래스 명을 가진것을 10개만 뽑아냄 (뉴스기사의 제목)
    titles = html.select('a.news_tit' , limit=10)

    # 뽑아낸 태그들 중에 text만 출력함
    for i in titles:
      title = i.get_text()
      print("Result : ", title, "\n\n")
  
  elif(searchType == '이미지'):
    # 크롬 웹 브라우저를 기동함
    # 크롬 드라이버의 위치가 다른경우 ()내부에 주소 적어야함
    dr = webdriver.Chrome()

        # 파싱할 url 생성 (네이버 이미지탭의 url)
    url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' + '%s'%query

    # 크롬 드라이버로 해당 사이트에 접속
    dr.get(url)

    # 크롬 드라이버 작동을 위하여 코드 1초간 대기
    sleep(1)

    # 크롬 드라이버의 사이트 소스를 얻어와 보기좋게 정리
    html = bs(dr.page_source, 'html.parser')
    
    # 얻어온 정보에서 img 태그를 가지고 _image와 _listImage 클래스를 가지는
    # 속성들을 추출
    images = html.select('img._image._listImage')

    # 이미지 저장을 위한 숫자
    count = 1
    for image in images:

      # 일부 데이터가 src가 아닌 data: AAAAAVVSDFSDF이런 형식으로 같이 추출되는 것을 확인
      # 검색 결과에서의 원하는 값이 아님으로 해당 값을 예외처리함
      if(image['src'][0:4] == 'data'):
        continue

      else:
        # 예외처리 이후 각 img 태그 들에서 src 속성만 추출
        req = requests.get(image["src"]).content

        # 검색어 + 이미지 숫자 + .png 형식의 이름으로 설정
        savename = query + str(count) + ".png"
        
        # 사진은 해당 이름으로 웹에서 읽어서 저장후 종료
        photo = open(savename, "wb")
        photo.write(req)
        photo.close()

        # 숫자 증가 및 10개 넘어가면 종료
        count += 1
        if(count > 10):
          break
    
    # 크롬 드라이버 종료
    dr.close()
    
  elif (searchType == '동영상'):

    dr = webdriver.Chrome()

    url = 'https://www.google.com/search?q=%s&oq=$%s&aqs=chrome.0.69i59j69i60.1311j0j9&sourceid=chrome&ie=UTF-8'%(query, query)

    dr.get(url)

    sleep(1)

    # 동영상 태그의 위치가 검색어 마다 다름으로 
    # xpath가 배열형식임을 이용하여 2번부터 검색 (1번은 전체검색으로 설정이 되어있지 않음)
    for i in range(2, 9):
      VD = dr.find_element(By.XPATH ,'//*[@id="hdtb-msb"]/div[1]/div/div[%d]/a'%i)
      if(VD.text == '동영상'):
        VD.click()
        break;

    sleep(3)

    # 크롬 드라이버의 사이트 소스를 얻어와 보기좋게 정리
    html = bs(dr.page_source, 'html.parser')
    
    # 얻어온 정보에서 div 태그를 가지고 VYkpsb 클래스를 가지는
    # 속성들을 추출
    videos = html.select('div.MjjYud a')

    print("Videos : ", videos, end='\n\n\n')

    # 동영상 저장을 위한 숫자
    count = 1
    for video in videos:

      # data-url태그가 없는 경우(썸네일이 5초의 영상이 아닌 이미지인 경우)를 위한 예외처리
      try:
        if("youtube" in video['href']):
          print("Youtube : ", video['href'], end='\n\n\n')
        # req = requests.get(video["data-url"]).content
      
        # # 검색어 + 동영상 숫자 + .mp4 형식의 이름으로 설정
        # savename = query + str(count) + ".mp4"
        
        # # 동영상을 해당 이름으로 웹에서 읽어서 저장후 종료
        # photo = open(savename, "wb")
        # photo.write(req)
        # photo.close()

        # count += 1

        # elif(video['href']):
        #   print("Links : ", video, end='\n\n\n')

        # else:
        #   print("Others : ", video, end='\n\n\n')

      except:
        continue

    # 크롬 드라이버 종료
    dr.close()
  
  # 뉴스 & 이미지 & 동영상 이외의 검색조건을 입력할 경우 프로그램 종료
  else:
    print("잘못된 입력입니다.\n")
    break