from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

import random
import time
import math

def StartBrowser(browserName: str):

    match browserName.lower():

        case "firefox":
            return webdriver.Firefox()
        case "edge":
            return webdriver.Edge()
        case "chrome":
            return webdriver.Chrome()
        case "safari":
            return webdriver.Safari()


def GoToUrl(browser: webdriver.Remote, url: str):
    browser.get(url)

def FindElementsByClass(browser: webdriver.Remote, className: str):
    return browser.find_elements(By.CLASS_NAME, className)


def FindElementsById(browser: webdriver.Remote, id: str):
    return browser.find_elements(By.ID, id)

def ClickElement(element: WebElement):
    element.click()

def SendTextToElement(element: WebElement, text: str):
    element.send_keys(text)


def HumanLikeScroll(browser: webdriver.Remote, scrollTo, pauseRange=(0.3, 1), scrollAmount=(100,500), chanceToPause = 0.2, chanceToGoUp = 0.1):

    currentPosition = 0

    endPosition = scrollTo

    scroll_speed = random.randint(*scrollAmount)

    while currentPosition <= endPosition:

        scrollBy = random.randint(*scrollAmount)

        if currentPosition < scrollTo / 3:
            scroll_speed = int(scroll_speed * 1.25)  # Accelerate
        elif currentPosition > 2 * scrollTo / 3:
            scroll_speed = int(scroll_speed * 0.55)  # Decelerate

        scroll_speed = min(scroll_speed, 70)

        scrollBy = min(scroll_speed, endPosition - currentPosition)

        browser.execute_script(f'''
            window.scrollBy({{ 
                top: {scrollBy}, 
                behavior: 'smooth' 
            }});''')

        if(random.uniform(0,1) <= chanceToGoUp):
            currentPosition -= scrollBy
        else:
            currentPosition += scrollBy

        if(random.uniform(0,1) <= chanceToPause):
            sleepTime = random.uniform(*pauseRange)

            time.sleep(sleepTime)