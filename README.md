#  "Measure time to load web page"
## Method 01:
   • urllib: urllib package is the URL handling module for python. It is used to fetch
     URLs. It uses the urlopen function and is able to fetch URLs using a variety of
     different protocols.  
     
   • import urlib.request: The urllib.request module defines functions and classes
     which help in opening URLs (mostly HTTP) in a complex world — basic and
     digest authentication, redirections, cookies and more. 
     
   • urlib.request.urlopen(url): Open the URL url, which can be either a string or
     a Request object.
     
   • time.time(): The time() function returns the number of seconds passed since
    epoch. For Unix system, January 1, 1970, 00:00:00 at UTC is epoch (the point
    where time begins).
    
   • time.ctime(): Convert a time in seconds since the Epoch to a string in local
    time. This is equivalent to asctime(localtime(seconds)). When the time tuple is
    not present, current time as returned by localtime() is used.

## Method 02 :
   • install selenium library: Run this command on terminal “pip install selenium”. 
     Selenium is a powerful tool for controlling web browsers through programs and 
     performing browser automation. It is functional for all browsers,
     works on all major OS and its scripts are written in various languages i.e Python,
     Java, C#, etc, we will be working with Python.
     
   • From selenium import webdriver: Selenium WebDriver is a web framework that permits 
     you to execute cross-browser tests. This tool is used for automating
     web-based application testing to verify that it performs expectedly.
     
   • from webdriver_manager.chrome import ChromeDriverManager: It is used to install the 
     webdriver at runtime.
     
   • driver.get(link): It get url link and open the url on chrome window.
   
   • driver.execute_script(“”): Use the browser Navigation Timing API to get some numbers.

## Method 03 :
   • import requests: requests will allow you to send HTTP/1.1 requests using Python. With it, 
   you can add content like headers, form data, multipart files, and parameters via simple Python 
   libraries. It also allows you to access the response data of Python in the same way.
   
   • requests.get(url): It get the url link and load the data of url web response.
   
   • response.elapsed: response.elapsed returns a timedelta object with the time elapsed from sending 
   the request to the arrival of the response. It is often used to stop the connection after a certain 
   point of time is “elapsed”.
   
• Input:
    Enter the string url and choose one library for running the program to measure the load time of web. 
    
• Expected output:
    Program prints the load time of web in minutes.

#  "Make progress bar using ‘tqdm’" 
     • install tqdm library: Run this command on terminal “pip install tqdm”. “tqdm” is a Python 
       library that allows you to output a smart progress bar by wrapping around any iterable. A 
       tqdm progress bar not only shows you how much time has elapsed, but also shows the estimated 
       time remaining for the iterable.
       
     • import time: This module provides various time-related functions. For related functionality, 
       see also the sleep, datetime and calendar modules.
     • tqdm syntax: tqdm(iterable)
## Parameters in tqdm:
        ◦ Iterable: It can be a range, a list whose progress we have to check.
        ◦ ncols: (int, optional)
             The width of the entire output message. If specified, dynamically resizes the progressbar to 
             stay within this bound. If unspecified, attempts to use environment width. The fallback is a 
             meter width of 10 and no limit for the counter and statistics. If 0, will not print any meter (only stats).
        ◦ desc: (str, optional)
             Prefix or text message for the progressbar.
        ◦ initial: (int or float, optional)
             The initial counter value. Useful when restarting a progress bar [default: 0]. If using float, 
             consider specifying {n:.3f} or similar in bar_format, or specifying unit_scale.
        ◦ miniters: (int or float, optional)
             Minimum progress display update interval, in iterations. If 0 and dynamic_miniters, will automatically 
             adjust to equal min interval. If > 0, will skip display of specified number of iterations.
        ◦ colour: (str, optional)
             Bar colour (e.g: 'yellow', 'ffff00').
