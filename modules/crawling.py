from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches",['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=chrome_options)

username = "J1W0N-1209"

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5) # 웹페이지가 로딩 될 때까지 5초는 기다림
driver.maximize_window() # 화면 최대화
driver.get("https://github.com/" + username)

# 스크롤 전 높이
before_h = driver.execute_script("return window.scrollY")
# 무한 스크롤
while True:
    # 맨 아래로 스크롤을 내린다.
    driver.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)

    # 스크롤 사이 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = driver.execute_script("return window.scrollY")

    if after_h == before_h:
        break
    before_h = after_h

commits = driver.find_elements(By.CSS_SELECTOR,".ContributionCalendar-day")

for commit in commits:
    if commit.get_attribute("aria-describedby") == "contribution-graph-legend-level-0":
        print(commit.get_attribute("data-date"))