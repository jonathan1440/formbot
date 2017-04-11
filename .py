import webbrowser
import pyautogui
import random
import math
import time 

#king and queen
#url = "https://docs.google.com/forms/d/e/1FAIpQLSenKUkczIp3jhx_sy_SFaoVHi06RKRJQrUSXhbvU-PUZCSikA/viewform?c=0&w=1"

#prince and princess
url = "https://docs.google.com/a/ziesmer.us/forms/d/e/1FAIpQLSc-fTsjkPPm-IH6jshrGZXSVI19VNXs2_2S3BbJCYJD9Nz7UQ/viewform?c=0&w=1"

#female name spelling options
fnames = [""]

#male name spelling options
mnames = ["vincent rooyakkers","vincent royakkers","vincent rooyakers","vincent royakers"]

#open page
webbrowser.open_new(url)
time.sleep(3)

#select next on pg 1
pyautogui.press('tab')
time.sleep(1)   

#click next on pg 1
pyautogui.press('enter')
time.sleep(3)

#select pg 2 text field
pyautogui.press('tab')
time.sleep(1)

#enter text from fnames
pyautogui.typewrite(fnames[math.floor(random.randint(0,len(fnames)-1))])
time.sleep(1)

#selet pg 2 back
pyautogui.press('tab')
time.sleep(1)

#select pg 2 next
pyautogui.press('tab')
time.sleep(1)

#click pg 2 next
pyautogui.press('enter')
time.sleep(3)

#select pg3 text field
pyautogui.press('tab')
time.sleep(1)

#enter text from mnames
pyautogui.typewrite(mnames[math.floor(random.randint(0,len(mnames)-1))])
time.sleep(1)

#select pg3 back
pyautogui.press('tab')
time.sleep(1)

#select pg3 next
pyautogui.press('tab')
time.sleep(1)

#click pg3 next
pyautogui.press('enter')
time.sleep(3)

#select pg4 submit another response
pyautogui.press('tab')
time.sleep(1)

#click pg4 submit another response
pyautogui.press('enter')
time.sleep(3)
