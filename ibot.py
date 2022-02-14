
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
import re
import sys
import instaloader as ig

class CSVH:

## TODO: convert IO to binary

    def __init__(self, fp, mode = 'r'):

        self.handle = open(fp, mode)
        self.mode = mode
        self.file_path = fp

        self.raw_data = []

    def load(self):

        if self.handle.closed:

            print("<--! File is closed !-->")
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

            self.data[count] = count
            count += 1


        print("<--! {} Items Loaded !-->".format(count))

    def add(self, val):

        if self.handle.closed or 'a' not in self.mode:

            print("<--! File is closed or/and Wrong Mode !-->")
            sys.exit(1)

        raw_val = ",".join(val) +"\n"

        self.handle.write(raw_val)

L = ig.Instaloader()

username = "sadbrotech"
password = "123456qwerty"

L.login(username, password)  # (login)

profile = ig.Profile.from_username(L.context, 'monikonw')

chrome_options = Options()
chrome_options.add_argument(
   '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')

chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
mobile_emulation = { "deviceName": "iPhone 5/SE" }
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.binary_location = r"/bin/google-chrome"

browser = webdriver.Chrome("./chromedriver_linux", options=chrome_options)

try:

    browser.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    usrname_bar = browser.find_element_by_name('username')
    passwrd_bar = browser.find_element_by_name('password')

    username = 'sadbrotech'  # Enter your username here
    password = '123456qwerty'  # Enter your password here

    usrname_bar.send_keys(username)
    passwrd_bar.send_keys(password + Keys.ENTER)

    print("Successfully Logged in !")

    time.sleep(11)

except:

    print("Unsuccessful Login !")

follow_list = []

for follower in profile.get_followers():
    follow_list.append(follower.username)

def send_msg(usrname):

    try:
        browser.get('https://www.instagram.com/direct/new/')

        time.sleep(5)

        to_btn = browser.find_elements_by_css_selector('.j_2Hd.uMkC7.M5V28')
        to_btn[0].send_keys(usrname)
        time.sleep(8)
        chk_mrk = browser.find_elements_by_class_name('-qQT3')
        for c in chk_mrk:
            if c.text.replace('\n'," ").split()[0] == usrname:
                c.click()
                break

        time.sleep(3)

        nxt_btn = browser.find_elements_by_css_selector('.sqdOP.yWX7d.y3zKF.cB_4K')
        nxt_btn[0].click()

        time.sleep(6)

        txt_box = browser.find_element_by_tag_name('textarea')
        txt_box.send_keys(f"Hi @{usrname} ! What's up ?")  # Customize your message

        time.sleep(2)

        snd_btn = browser.find_elements_by_css_selector('.sqdOP.yWX7d.y3zKF')
        snd_btnn = snd_btn[len(snd_btn)-1]
        snd_btnn.click()

        print("Sent Msg to {}".format(usrname))  # LOG TO CONSOLE

        time.sleep(4)

    except IndexError:
        print('failed')

print(follow_list)  #--> To get the list

print("\nNo of followers: {}".format(len(follow_list)))

for un in follow_list:

    send_msg(un)

browser.quit()
