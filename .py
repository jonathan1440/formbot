import webbrowser
import pyautogui
import random
import math
import time
from datetime import datetime

#king and queen
#url = "https://docs.google.com/forms/d/e/1FAIpQLSenKUkczIp3jhx_sy_SFaoVHi06RKRJQrUSXhbvU-PUZCSikA/viewform?c=0&w=1"

#prince and princess
url = "https://docs.google.com/a/ziesmer.us/forms/d/e/1FAIpQLSc-fTsjkPPm-IH6jshrGZXSVI19VNXs2_2S3BbJCYJD9Nz7UQ/viewform?c=0&w=1"

#female name spelling options
fnames = [""]

#male name spelling options
mnames = ["vincent rooyakkers","vincent royakkers","vincent rooyakers","vincent royakers"]

#captialize random words
def words(string):
    wrds = string.split(" ")
    for i in range(len(wrds)):
        if(math.floor(random.randint(0,2)) == 0):
            wrds[i] = wrds[i].capitalize()

    return wrds

#number of iterations
numi = int(2)

#open page
webbrowser.open_new(url)
time.sleep(3)

dt = datetime.now()

while numi > 0:

    #print("")
    #print("iteration "+str(numi))
    
    if dt.hour > 8 and dt.hour < 22:

        #select next on pg 1
        pyautogui.press('tab')
        #print("select next on pg 1")
        time.sleep(3)   

        #click next on pg 1
        pyautogui.press('enter')
        #print("click next on pg 1")
        time.sleep(1)

        #select pg 2 text field
        pyautogui.press('tab')
        #print("select pg 2 text field")
        time.sleep(1)

        #enter text from fnames
        pyautogui.typewrite(words(fnames[math.floor(random.randint(0,len(fnames)-1))]))
        #print("enter text from fnames")
        time.sleep(1)

        #selet pg 2 back
        pyautogui.press('tab')
        #print("selet pg 2 back")
        time.sleep(1)

        #select pg 2 next
        pyautogui.press('tab')
        #print("select pg 2 next")
        time.sleep(1)

        #click pg 2 next
        pyautogui.press('enter')
        #print("click pg 2 next")
        time.sleep(3)

        #select pg3 text field
        pyautogui.press('tab')
        #print("select pg3 text field")
        time.sleep(1)

        #enter text from mnames
        pyautogui.typewrite(words(mnames[math.floor(random.randint(0,len(mnames)-1))]))
        #print("enter text from mnames")
        time.sleep(1)

        #select pg3 back
        pyautogui.press('tab')
        #print("select pg3 back")
        time.sleep(1)

        #select pg3 next
        pyautogui.press('tab')
        #print("select pg3 next")
        time.sleep(1)

        #click pg3 next
        pyautogui.press('enter')
        #print("click pg3 next")
        time.sleep(3)

        #select pg4 submit another response
        pyautogui.press('tab')
        #print("select pg4 submit another response")
        time.sleep(1)

        #click pg4 submit another response
        pyautogui.press('enter')
        #print("click pg4 submit another response")
        time.sleep(3)

        numi = numi - 1

        time.sleep(random.randint(1,60) * 60)

    else:
        print("wrong time")
