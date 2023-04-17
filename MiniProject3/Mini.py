#################################################
# Mini.py                                       # 
# 유튜브에서 영상 검색 후 음성소스/ 동영상         #
# 선택 다운로드 크롤링                            #
#                                               #
# *중요*                                        #
# Chrome driver를 설치된 Chrome 버전에 맞게       #
# 설치 후 소스코드 위치에 옮겨 주어야 함           #
# 유튜브 검색결과 조회 및 다운로드에               #
# 동적 크롤링을 사용하여 필수                     #
#                                               #
# Download_Folder의 값을 변경하여                #
# 다운로드 위치 변경가능                         #
################################################

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep
from pytube import YouTube
import os


# 파일을 저장할 폴더의 위치입니다.
Download_Folder = 'C:/Users/Ku/Downloads/'

# q로 종료할떄 까지 반복해서 동작
while True:
  query = input("검색어를 입력해 주세요. q입력시 종료 : ")

  if(query == 'q'):
    break
  
  options = webdriver.ChromeOptions()

  options.add_argument("headless")

  # 크롬 드라이버 화면을 표기할 필요가 없음으로
  # 숨김 옵션 활성화
  dr = webdriver.Chrome(chrome_options=options)
  
  # 검색어를 입력받아 해당하는 검색창으로 이동
  url = 'https://www.youtube.com/results?search_query=%s'%query

  dr.get(url)

  sleep(1)

	# 크롬 드라이버의 사이트 소스를 얻어와 보기좋게 정리
  html = bs(dr.page_source, 'html.parser')

	# 얻어온 정보에서 a 태그를 가지고 vodeos-title 클래스를 가지는
	# 속성들을 추출
  videos = html.select('a#video-title')

  videoUrls = []

  count = 1

  for video in videos:
    try:
      # 얻어온 정보에서 href 즉 해당 영상의 유튜브 링크를 획득
      youtubeUrl = "https://youtube.com" + video['href']

      # aria-label 부분에는 영상 제목/ 영상 길이/ 영상 업로드로 부터의 기간등
      # 다양한 정보들이 한줄로 연결되어 있음으로 영상 길이 부분만 인덱싱하여 추출
      youtubeTime = " ".join(video['aria-label'].split()[-4: -2]) if (video['aria-label'].split()[-4: -3] != "전") else video['aria-label'].split()[-3: -2]
      print("%d.\nYoutube Title: %s %s"%(count, video['title'], youtubeTime))
      print("Youtube Link: %s\n"%youtubeUrl)
      count += 1
      videoUrls.append(youtubeUrl)

    except:
      print(f'video setting Error from {video}')
      continue
  
  # 숫자를 입력받아 저장된 url로 부터 어느 영상/ 음원을
  # 다운받을 것인지 확인
  dlSet = list(map(int, input("어느 파일을 다운하시겠습니까? 숫자들만 입력해 주세요. (종료: -1)\n :").split()))
  if (dlSet[0] == -1):
    continue

  while True:   
    mod = input("어느 형식으로 저장하시겠습니까? (mp3음원, mp4영상) 음원/ 영상으로 입력해 주십시오.\n(취소 = q)\n")

    if (mod == "음원"):
      for i in dlSet:
        yt = YouTube(videoUrls[i - 1])

        # 음원만 다운함으로 only_audio 옵션을 활성화
        # download 내부는 다운로드 위치 임으로 원하는 곳으로 재설정 가능
        yt.streams.filter(only_audio=True).first().download(Download_Folder)
        try:
          # 다운로드 한 파일의 형식을 mp4에서 mp3로 변경해 줍니다.
          print(f'yt.title: {yt.title}')
          os.rename(Download_Folder + yt.title + '.mp4', Download_Folder + yt.title + '.mp3')
        except:
          # 파일명에 \ | / : ? * < >과 같은 특수문자가 포함될 경우등ㅂ
          # 변환이 불가능할 경우에 에러처리를 진행합니다.
          print("%s의 파일명 변환중 에러가 발생하였습니다."%yt.title)
          print("유튜브 영상 제목에 사용할 수 없는 특수문자가 포함되어 있습니다.")
          print(".mp4 형식으로 저장되었습니다.")
      break

    elif (mod == "영상"):
      for i in dlSet:
        yt = YouTube(videoUrls[i - 1])

        # 영상화 함께 다운함으로 고화질로 다운로드 설정
        yt.streams.filter().get_highest_resolution().download(Download_Folder)
      break

    elif (mod == "q"):
      break

    else:
      print("잘못된 입력입니다.")
      continue
    
	# 크롬 드라이버 종료
  dr.close()