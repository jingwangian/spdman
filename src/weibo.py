#!/usr/bin/env python3
import pickle
from selenium import webdriver


def test():
    browser = webdriver.Firefox()

    try:
        login_url = 'https://www.weibo.com/login.php'

        print("request {}".format(login_url))
        browser.get(login_url)

        pickle.dump(browser.get_cookies(), open("cookies.pkl", "wb"))

        url = 'https://www.weibo.com/1764145893/Gnuo0f5k0?type=comment'

        print("request {}".format(url))
        browser.get(url)
        # assert 'Yahoo' in browser.title

        # print(browser.page_source)

        print("Start to save into file")
        with open("../data/weibo_1764145893.html", 'w') as f:
            f.write(browser.page_source)

        print("Finished to save into file")
        # elem = browser.find_element_by_name('p')  # Find the search box
        # elem.send_keys('seleniumhq' + Keys.RETURN)

    except Exception as e:
        print("Error : {}".format(str(e)))

    finally:
        print("Close browser")
        browser.quit()


test()
