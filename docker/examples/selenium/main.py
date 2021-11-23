# pip install selenium
# %%
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=DesiredCapabilities.FIREFOX)

# %%


driver.get("https://yandex.ru/")
