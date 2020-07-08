
import os
import pytest
from selenium import webdriver
from basicdata_pages.login_page import LoginPage
from datas.login_data import login_data
from selenium.webdriver import ChromeOptions
from alarm_manage_pages.equiplink_page import EquipLinkPage


@pytest.fixture(scope='class')
def set_up_login():
    """初始化浏览器并登录"""
    for a, b, c in os.walk(r"C:\Users"):
        for file in c:
            if file == "chrome.exe":
                chrome_path = os.path.join(a,file)
                path = a.split('\\')
                download_path = path[0] + '\\' + path[1] + '\\' + path[2] + '\\' + 'Downloads'
    options = ChromeOptions()
    prefs = {'download.prompt_for_download':False,'download.default_directory':f'{download_path}'}
    options.add_experimental_option("prefs",prefs)
    options.binary_location = chrome_path
    driver = webdriver.Chrome(chrome_options=options)
    driver.command_executor._commands["send_command"] = ("POST",'/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior','params':{'behavior':'allow','downloadPath':f'{download_path}'}}
    driver.execute("send_command",params)
    driver.implicitly_wait(5)
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.login(login_data[0]['username'],login_data[0]['pwd'])
    yield driver
    driver.quit()
    # driver.refresh()

@pytest.fixture(scope='class',name='master')
def set_up_login_master():
    """初始化浏览器并登录"""
    for a, b, c in os.walk(r"C:\Users"):
        for file in c:
            if file == "chrome.exe":
                chrome_path = os.path.join(a,file)
                path = a.split('\\')
                download_path = path[0] + '\\' + path[1] + '\\' + path[2] + '\\' + 'Downloads'
    options = ChromeOptions()
    prefs = {'download.prompt_for_download':False,'download.default_directory':f'{download_path}'}
    options.add_experimental_option("prefs",prefs)
    options.binary_location = chrome_path
    driver = webdriver.Chrome(chrome_options=options)
    driver.command_executor._commands["send_command"] = ("POST",'/session/$sessionId/chromium/send_command')
    params = {'cmd':'Page.setDownloadBehavior','params':{'behavior':'allow','downloadPath':f'{download_path}'}}
    driver.execute("send_command",params)
    driver.implicitly_wait(5)
    driver.maximize_window()
    login_page = LoginPage(driver)
    login_page.login_master(login_data[0]['username'],login_data[0]['pwd'])
    yield driver
    driver.quit()


