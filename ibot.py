
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import instaloader as ig

import datetime as dt
import time
import sys
import random

class CSVH:

## TODO: convert IO to binary

    def __init__(self, fp, mode = 'r'):

        try:
            self.handle = open(fp, mode)

        except:
            print("[SYS] Vooh, Couldn't open the file.")

        self.mode = mode
        self.file_path = fp

        self.raw_data = []

    def load(self):

        if self.handle.closed:

            print("[SYS] File is closed.")
            sys.exit(1)

        self.raw_data = self.handle.readlines()
        self.fields = self.raw_data[0].strip("\n").split(",")
        self.data = []

        count = 0

        for raw in self.raw_data[1:]:

            tmp_dict = {}
            values = raw.strip("\n").split(",")

            for key, val in zip(self.fields, values):

                tmp_dict[key] = val

            self.data[count] = tmp_dict
            count += 1

        print("[INFO] {} Items Loaded".format(count))

    def add(self, val):

        raw_val = ",".join([str(i) for i in val]) +"\n"
        self.handle.write(raw_val)

    def get_last(self):

        if self.data:
            pass

        else:
            self.load()

        return self.data[-1]

    def __del__(self):

        self.handle.close()

    def close(self):

        self.__del__()
        print("[SYS] File Handler for FILE({}) with MODE({}) successfully closed".format(self.file_path, self.mode))

L = ig.Instaloader()

uname = "rgntech"
pword = "thisismyroot"

L.login(uname, pword)  # (login)

profile = ig.Profile.from_username(L.context, 'monikonw')

chrome_options = Options()
chrome_options.add_argument(
   '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')

chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
mobile_emulation = { "deviceName": "iPhone 5/SE" }
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.binary_location = r"/bin/google-chrome"

browser = webdriver.Chrome("drivers/chromedriver", options=chrome_options)

try:

    browser.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    usrname_bar = browser.find_element_by_name('username')
    passwrd_bar = browser.find_element_by_name('password')

    username = uname  # Enter your username here
    password = pword  # Enter your password here

    usrname_bar.send_keys(username)
    passwrd_bar.send_keys(password + Keys.ENTER)

    print("[INFO] Successfully Logged in !")

    time.sleep(11)

except:

    print("[INFO] Unsuccessful Login !")

follow_list = []

def send_msg(usrname):

    try:
        browser.get('https://www.instagram.com/direct/new/')

        time.sleep(random.randint(1, 6)) # og 5

        to_btn = browser.find_elements_by_css_selector('.j_2Hd.uMkC7.M5V28')
        to_btn[0].send_keys(usrname)
        time.sleep(8)
        chk_mrk = browser.find_elements_by_class_name('-qQT3')
        for c in chk_mrk:
            if c.text.replace('\n'," ").split()[0] == usrname:
                c.click()
                break

        time.sleep(random.randint(1, 4)) # og 3

        nxt_btn = browser.find_elements_by_css_selector('.sqdOP.yWX7d.y3zKF.cB_4K')
        nxt_btn[0].click()

        time.sleep(random.randint(1, 7)) # og 7

        txt_box = browser.find_element_by_tag_name('textarea')
        txt_box.send_keys(f"Hi @{usrname} ! What's up ?")  # Customize your message

        time.sleep(random.randint(1, 3)) # og 2

        snd_btn = browser.find_elements_by_css_selector('.sqdOP.yWX7d.y3zKF')
        snd_btnn = snd_btn[len(snd_btn)-1]
        snd_btnn.click()

        print("[INFO] Sent Msg to {}".format(usrname))  # LOG TO CONSOLE

        time.sleep(random.randint(1, 5)) # og 4

    except IndexError:
        print('[SYS] DM failed')

print(follow_list)  #--> To get the list

print("\n[INFO] No of followers: {}\n".format(len(follow_list)))

fio = CSVH("follower.csv", "w")

try:

    fio.load()

    start_index = len(fio.data)

    for i in range(start_index, len(follow_list)):

        send_msg(follow_list[i])
        fio.add([i, follow_list[i], dt.datetime.now(), True])

except:

    fio.add(["id", "ig_handle", "time", "sent"])

    for i, un in enumerate(follow_list):

        send_msg(un)
        fio.add([i, un, dt.datetime.now(), True])

fio.close()

#browser.quit()
