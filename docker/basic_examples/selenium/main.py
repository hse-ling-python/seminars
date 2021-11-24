# %% 
# !pip install selenium
# docker run -d -p 4444:4444 -p 5432:7900 --shm-size="2g" selenium/standalone-firefox:4.1.0-20211123
# %%
import time 
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# %%

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.FIREFOX)

# %%


driver.get("https://yandex.ru/")
time.sleep(5)
time.sleep(5)

# %%
driver.get("https://yandex.ru/pogoda/")
# подождем, когда страница загрузится
time.sleep(5)
# получим xpath через инспектор браузера и найдем элемент с погодой в html
temperature = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[1]/div[6]/a/div[1]/span[2]").text
print(f'temperature={temperature}')
# %%
