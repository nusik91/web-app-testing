import yaml
import requests
from selenium import webdriver
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(name)

from model import Site
with open('./config.yaml') as f:
    requests.post(url=url)
    config = yaml.safe_load(f)
    btn1_selector = """//*[@id="login"]/div[3]/button"""
Site.find_element('css', btn1_selector).click()
def test_step1():
    try:
        x_selector1 = """//*[@id="login"]/div[1]/label/input"""
        input1 = Site.find_element('xpath', x_selector1)
        input1.send_keys(config['test'])
    except Exception as e:
        logger.error("Error occurred in teststep1: " + str(e))
def test_step2():
    try:
        x_selector2 = """//*[@id="login"]/div[2]/label/input"""
        input2 = Site.find_element('xpath', x_selector2)
        input2.send_keys(config['test'])
        btn_selector = "button"
        button = Site.find_element('css', btn_selector)
        button.click()
        x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
        err_label = Site.find_element('xpath', x_selector3)
        assert err_label.text == "Неверный логин или пароль"
        logger.info("Performed test_step2")
    except Exception as e:
        logger.error("Error occurred in test_step2: " + str(e))

def test_step3():
    try:
        createbutton = Site.findelement('css', 'button#create-btn')
        createbutton.click()
        time.sleep(1)
        posttitleinput = Site.findelement('css', 'input.mdc-text-field__input')
        posttitleinput.sendkeys(config['test_post_title'])
        postcontentinput = Site.findelement('css', 'textarea.mdc-text-field__input')
        postcontentinput.sendkeys(config['test_post_content'])
        x_selector4 = """//*[@id="app"]/main/div/div/form/div/div/div[7]/div/button/div"""
        createpostbutton = Site.findelement('css', x_selector4)
        createpostbutton.click()


        time.sleep(1)

        posttitleselector = "h2.post-title"
        posttitle = Site.findelement('css', posttitleselector).text
        assert posttitle == config['test_post_title']
        logger.info("Performed teststep3")
    except Exception as e:
        logger.error("Error occurred in teststep3: " + str(e))

def test_step4():
    try:
        x_selector5 = """//*[@id="contact"]/div[4]/button/div"""
        contactusbutton = Site.findelement('css', x_selector5)
        contactusbutton.click()
        time.sleep(1)

        nameinput = Site.findelement('css', 'input.mdc-text-field__input')
        nameinput.sendkeys(config['test_name'])

        emailinput = Site.findelement('css', 'email-input')
        emailinput.sendkeys(config['test_email'])

        messageinput = Site.findelement('message-input')
        messageinput.sendkeys(config['test_message'])

        submitbutton = Site.findelement('submit-button')
        submitbutton.click()

        time.sleep(1)

        alert = Site.switchto.alert
        alerttext = alert.text

        alert.accept()

        assert alerttext == config['test_alert_message']

        Site.quit()
        logger.info("Performed teststep4")
    except Exception as e:
        logger.error("Error occurred in teststep4: " + str(e))