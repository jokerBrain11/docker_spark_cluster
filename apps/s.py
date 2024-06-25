from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 设置 Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 打开 Spark UI
driver.get('http://localhost:8080')

# 等待页面加载
time.sleep(5)

# 定位 DAG 图
dag_element = driver.find_element_by_css_selector('svg')  # 具体的 CSS 选择器可能需要根据实际的页面调整

# 截图并保存
dag_element.screenshot('dag.png')

driver.quit()
