#!/usr/bin/python
# -*- coding: utf-8 -*-
# by: pantuts
# ASUS RTAC1200g+

from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select

import sys
import time

MAC_TO_FILTER = '00:11:22:33:44:55'

URL = 'https://192.168.1.1:8443'
INPUT_USER = 'login_username'
INPUT_PASSWD = 'login_passwd'

WIRELESS_ID = 'Advanced_Wireless_Content_menu'
WL_MAC_FILTER_TAB_ID = 'Advanced_ACL_Content_tab'
WL_MAC_TABLE_ID = 'MainTable1'
MAC_RADIO_ENABLE = 'enable_mac'
MAC_SELECT = 'wl_macmode_show'
LIST_0 = 'wl_maclist_x_0'

REMOVE_BTN = 'remove_btn'
ADD_BTN = 'add_btn'
SUBMIT_BTN = 'submitBtn'
LOADING_ID = 'Loading'

if len(sys.argv) < 2:
    print('mac_filter.py 0|1')
    print('REMOVE FILTER (0) | ADD FILTER (1)')
    sys.exit()

cmd = int(sys.argv[1])

user = input('Eman Lodi: ')
passwd = getpass('Drowssap Lodi: ')

driver = webdriver.Chrome()
driver.get(URL)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, INPUT_USER)))

user_input = driver.find_element_by_id(INPUT_USER)
passwd_input = driver.find_element_by_name(INPUT_PASSWD)
user_input.send_keys(user)
passwd_input.send_keys(passwd)
time.sleep(1)
passwd_input.send_keys(Keys.RETURN)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'NM_table')))

wltab = driver.find_element_by_id(WIRELESS_ID).find_element_by_class_name('menu_Desc')
wltab.click()
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, WL_MAC_FILTER_TAB_ID)))
time.sleep(1)
wl_mac_tab = driver.find_element_by_id(WL_MAC_FILTER_TAB_ID)
wl_mac_tab.click()
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, WL_MAC_TABLE_ID)))

mac_enable = driver.find_element_by_name(MAC_RADIO_ENABLE)
mac_enable.click()
time.sleep(1)
mac_select = Select(driver.find_element_by_name(MAC_SELECT))
mac_select.select_by_value('deny')
time.sleep(1)

if cmd == 0:
    mac_remove = driver.find_element_by_class_name(REMOVE_BTN)
    mac_remove.click()
    time.sleep(1)
elif cmd == 1:
    mac_list0 = driver.find_element_by_name(LIST_0)
    mac_list0.send_keys(MAC_TO_FILTER)
    time.sleep(1)
    mac_add = driver.find_element_by_class_name(ADD_BTN)
    mac_add.click()
    time.sleep(1)

submit = driver.find_element_by_id(SUBMIT_BTN).find_element_by_tag_name('input')
submit.click()
WebDriverWait(driver, 15).until(EC.invisibility_of_element_located((By.ID, LOADING_ID)))

driver.quit()
