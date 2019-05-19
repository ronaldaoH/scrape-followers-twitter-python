from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


def scroll_down(driver):
    """Un metodo para hacer scroll a una página web."""
    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to the bottom.
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page.
        time.sleep(2)
        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def get_followers(user_followers):
    MY_SCREEN_NAME = 'USERNAME'
    MY_PASSWORD = open("mypassword.txt").read().strip()
    driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
    driver.get("https://twitter.com/login")
    el = driver.find_element_by_css_selector("#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) > input")
    el.send_keys(MY_SCREEN_NAME)
    driver.find_element_by_css_selector("#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input").send_keys(MY_PASSWORD, Keys.ENTER)
    link_seguidores = 'https://twitter.com/{}/followers?lang=es'.format(user_followers)
    driver.get(link_seguidores)
    time.sleep(1)
    scroll_down(driver)
    user = driver.find_elements_by_css_selector('div.ProfileCard-userFields > span > a > span > b')
    for a in user:
        print(str(a.text))
    print("el numero de usuarios es : ", len(user))

get_followers('rorolas_')