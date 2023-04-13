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
import subprocess

# q로 종료할떄 까지 반복해서 동작
while True:
  query = input("검색어를 입력해 주세요. q입력시 종료 : ")

  if(query == 'q'):
    break
  
  options = webdriver.ChromeOptions()

  options.add_argument("headless")
# chrome_options=options
  dr = webdriver.Chrome()
        
  url = 'https://www.youtube.com/results?search_query=%s'%query

  dr.get(url)

  sleep(1)

	# 크롬 드라이버의 사이트 소스를 얻어와 보기좋게 정리
  html = bs(dr.page_source, 'html.parser')

	# 얻어온 정보에서 div 태그를 가지고 VYkpsb 클래스를 가지는
	# 속성들을 추출
  videos = html.select('a#video-title')

  videoUrls = []

  count = 1

  for video in videos:
    try:
      youtubeUrl = "https://youtube.com" + video['href']

      youtubeTime = " ".join(video['aria-label'].split()[-4: -2]) if (video['aria-label'].split()[-4: -3] != "전") else video['aria-label'].split()[-3: -2]
      print("%d.\nYoutube Title: %s %s"%(count, video['title'], youtubeTime))
      print("Youtube Link: %s\n"%youtubeUrl)
      count += 1
      videoUrls.append(youtubeUrl)

    except:
      continue
  
  dlSet = list(map(int, input("어느 파일을 다운하시겠습니까? 숫자들만 입력해 주세요. (종료: q)\n :").split()))
  if (dlSet == "q"):
    continue

  while True:   
    mod = input("어느 형식으로 저장하시겠습니까? (mp4음원, mp4영상) 음원/ 영상으로 입력해 주십시오.\n(취소 = q)\n")

    if(mod == "음원"):
      for i in dlSet:
        yt = YouTube(videoUrls[i - 1])
        yt.streams.filter(only_audio=True).first().download('C:/Users/Ku/Downloads')
      break

    elif(mod == "영상"):
      for i in dlSet:
        yt = YouTube(videoUrls[i - 1])
        yt.streams.filter().get_highest_resolution().download('C:/Users/Ku/Downloads')
      break

    elif (mod == "q"):
      break

    else:
      print("잘못된 입력입니다.")
      continue
    
	# 크롬 드라이버 종료
  dr.close()