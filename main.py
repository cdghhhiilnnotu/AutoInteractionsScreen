import pyautogui
import time
# res = pyautogui.locateOnScreen("image.png")
# print(res)
# edit_button = pyautogui.center(res)

# pyautogui.moveTo(edit_button)
# res = pyautogui.locateCenterOnScreen("image.png")
# print(res)

channel_name = pyautogui.prompt(text="",title="Enter the Channel Name")
print(channel_name)
pyautogui.click()

pyautogui.hotkey("ctrl","t")

pyautogui.write("https://www.youtube.com/")
pyautogui.hotkey("enter")
time.sleep(2)
x, y = pyautogui.locateCenterOnScreen("youtube_search.png", confidence=0.9)
pyautogui.moveTo(x,y,1)
pyautogui.click()
time.sleep(2)



pyautogui.write(channel_name)
pyautogui.hotkey("enter")
time.sleep(1)
x, y = pyautogui.locateCenterOnScreen("youtube_mck.png", confidence=0.9)
pyautogui.moveTo(x,y,1)
pyautogui.click()
time.sleep(2)
x, y = pyautogui.locateCenterOnScreen("subcribe.png", confidence=0.9)
pyautogui.moveTo(x,y,1)
pyautogui.click()
