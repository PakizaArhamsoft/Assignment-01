import warnings
warnings.filterwarnings("ignore")
import requests
import urllib.request as ur
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

"""
    measure the load time of a web page in minutes
"""
class time_load_web:
    def __init__(self) -> None:
        self.link = "https://www.google.com/"
        self.load_time = 0.0

    #      ********* First method using Urllib library  *********
    def using_urllib(self, link):
        try:
            self.link = link
            # open the url link
            web = ur.urlopen(self.link)
            # calculate the time to load the page
            start_time = time.time()
            print("Start time: ", start_time, "sec", "-------> ", time.ctime(start_time))
            web.read()  # read the web page to check all contents load correctly
            end_time = time.time()
            print("End time:  ", end_time, "sec", "-------> ", time.ctime(end_time))
            self.load_time = end_time - start_time
            print("Web page load time: ", self.load_time, "sec")
            print("Web page load time: ", round(self.load_time / 60, 2), "min")
        except Exception as e:
            print("Error: ", e)

    #      ********* Second method using selenium library  *********
    def using_selenium(self, link, driver):
        try:
            self.link = link
            driver.get(self.link)

            navigation_start = driver.execute_script(
                "return window.performance.timing.navigationStart")
            dom_complete = driver.execute_script(
                "return window.performance.timing.domComplete")
            self.load_time = dom_complete - navigation_start

            print(f"Time {self.load_time}ms")
            print("Web page load time: ", round(self.load_time / 60000, 2), "min")

            driver.quit()
        except Exception as e:
            print("Error: ", e)

    #      ********* third method using request library  *********
    def using_request(self, link):
        # Making a get request
        self.link = link
        response = requests.get(self.link)
        #  print response time and elapsed time

        print("Page response: ", response, "  Web response time:", response.elapsed)
        # print elapsed time seconds
        self.load_time = response.elapsed.seconds
        print("Web response time in seconds:", self.load_time, "sec")
        print("Web page load time: ", round(self.load_time / 60, 2), "min")


if __name__ == '__main__':
    obj = time_load_web()
    link = input("Enter web url ->")
    print("""
    Which library want to use for measuring time to load web???
    Please Choose right one option:
    1. By using urllib
    2. By using selenium
    3. By using request
    4. Exit
    """)
    option = int(input("->"))
    if option == 1:
        obj.using_urllib(link)
    elif option == 2:
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        obj.using_selenium(link, driver)
    elif option == 3:
        obj.using_request(link)
    elif option == 4:
        pass
    else:
        print("Invalid Choice......")
