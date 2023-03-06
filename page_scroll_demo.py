import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class ScrollingThePage():
    def test(self):
        driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
        driver.get("https://www.microsoft.com/sr-latn-rs/")
        driver.maximize_window()
        driver.fullscreen_window()


        # Scroll Down
        driver.execute_script("window.scrollBy(0, 180);")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, 380);")
        time.sleep(4)
        driver.execute_script("window.scrollBy(0, 1100);")
        time.sleep(3)
        # Scroll Up
        driver.execute_script("window.scrollBy(0, -380);")
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -1100);")
        time.sleep(4)
        driver.close()


page_scroll = ScrollingThePage()
page_scroll.test()








