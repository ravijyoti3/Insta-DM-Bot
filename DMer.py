from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
import re

# import schedule

x = 0
failedDm = 0

def dmer():
    global x
    usrnames = ['monikonw']  # username whom you will send the message

    chrome_options = Options()
    chrome_options.add_argument(
        '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    mobile_emulation = { "deviceName": "iPhone 5/SE" }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.binary_location = r"/bin/google-chrome"

    browser = webdriver.Chrome("./chromedriver_linux", options=chrome_options)

    browser.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    usrname_bar = browser.find_element_by_name('username')
    passwrd_bar = browser.find_element_by_name('password')

    username = 'sadbrotech'  # Enter your username here
    password = '123456qwerty'  # Enter your password here

    usrname_bar.send_keys(username)
    passwrd_bar.send_keys(password + Keys.ENTER)

    time.sleep(11)

    def grabFollowers(username):
        browser.get('https://www.instagram.com/{}'.format(username))
        time.sleep(1)
        followers = browser.find_elements_by_xpath("//span[@class='g47SY lOXF2']")
        print(followers[1].text)
        # browser.get('https://www.instagram.com/{}/followers'.format(username))
        # flwrs = int(followers[1].text)
        nxt_btn = browser.find_elements_by_xpath("//a[@href='/"+username+"/followers/']")
        print(nxt_btn)
        nxt_btn[0].click()

        # box = browser.find_element_by_css_selector('.jSC57._6xe7A')
        actions = ActionChains(browser)
        nfl = []
        for i in range(9999999):
            actions.send_keys(Keys.DOWN).perform()
            time.sleep(1)
            nf = browser.find_elements_by_xpath("//li[@class='wo9IH']")
            print(len(nf))
            nfl.append(len(nf))
            if i>10 and nfl[i]==nfl[i-10]:
                break
            # if nf:
            #     print(len(nf[0]))
                # if len(nf[0])==flwrs:
                #     return 0
        time.sleep(1)
        print('stats')
        id_lst = []
        flw_id = browser.find_elements_by_xpath("//li[@class='wo9IH']/div")
        print(flw_id)
        for f in flw_id:
            str1 = f.text
            fin_txt = str1.replace('\n'," ").split()[0]
            # fin_txt = re.split('\W',f.text)
            id_lst.append(fin_txt)
            print(id_lst)
        count = 0
        try:
            for usrnamee in id_lst:
                send_msg(usrnamee)
                count += 1

        except TypeError:
            print('Failed!')
            count-=1

        browser.quit()

        print(f'''
        Successfully Sent {count} Massages
        ''')
        time.sleep(3)

    def send_msg(usrnames):
        try:
            browser.get('https://www.instagram.com/direct/new/')

            time.sleep(5)

            to_btn = browser.find_elements_by_css_selector('.j_2Hd.uMkC7.M5V28')
            to_btn[0].send_keys(usrnames)
            time.sleep(8)
            chk_mrk = browser.find_elements_by_class_name('-qQT3')
            for c in chk_mrk:
                if c.text.replace('\n'," ").split()[0] == usrnames:
                    c.click()
                    break

            time.sleep(3)

            nxt_btn = browser.find_elements_by_css_selector('.sqdOP.yWX7d.y3zKF.cB_4K')
            nxt_btn[0].click()

            time.sleep(6)

            txt_box = browser.find_element_by_tag_name('textarea')
            txt_box.send_keys(f"Hi @{usrnames} ! What's up ?")  # Customize your message

            time.sleep(2)

            snd_btn = browser.find_elements_by_css_selector('.sqdOP.yWX7d.y3zKF')
            snd_btnn = snd_btn[len(snd_btn)-1]
            snd_btnn.click()

            time.sleep(4)
        
        except IndexError:
            print('failed')
    
    count = 0
    try:
        for usrnamee in usrnames:
            grabFollowers(usrnamee)
            count += 1

    except TypeError:
        print('Failed!')

    browser.quit()

    print(f'''
    Successfully grabbed {count} user's follower
    ''')

    x += 1
    
    # count = 0
    # try:
    #     for usrnamee in usrnames:
    #         send_msg(usrnamee)
    #         count += 1

    # except TypeError:
    #     print('Failed!')

    # browser.quit()

    # print(f'''
    # Successfully Sent {count} Massages
    # ''')

    # x += 1


# timee = "08:51"  # Specific Time When The message will be send

# try:
#     schedule.every().day.at(timee).do(dmer)
# except TypeError:
#     pass

# try:
#     while True and x != 1:
#         schedule.run_pending()
#         time.sleep(1)
# except UnboundLocalError:
#     pass

dmer()
