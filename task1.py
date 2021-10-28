import requests
import urllib.request as ur
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

try:
    link = input("Enter web url ->")
    # open the url link
    web = ur.urlopen(link)
except:
    print("Error in your web url, default link is opening now......")
    link = "https://www.arhamsoft.com/"
    # open the url link
    web = ur.urlopen(link)

# calculate the time to load the page
start_time = time.time()
print("Start time: ", start_time,"sec", "-------> ", time.ctime(start_time))
web.read()     # read the web page to check all contents load correctly
end_time = time.time()
print("End time:  ", end_time, "sec", "-------> ", time.ctime(end_time))
load_time = end_time - start_time
print("Web page load time: ", load_time, "sec")


#      ********* Second method using selenium library  *********

print("********* Second method using selenium library  *********")
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome()
    driver.get(link)

    navigation_start = driver.execute_script(
        "return window.performance.timing.navigationStart")
    dom_complete = driver.execute_script(
        "return window.performance.timing.domComplete")
    total_time = dom_complete - navigation_start

    print(f"Time {total_time}ms")

    driver.quit()
except Exception as e:
    print("Error: ", e)


#      ********* third method using request library  *********

print("********* third method using request library  *********")
# Making a get request
response = requests.get(link)
#  print response time and elapsed time
print("Page response: ", response, "  Web response time:", response.elapsed)
# print elapsed time seconds
print("Web response time in seconds:", response.elapsed.seconds, "sec")
