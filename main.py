from playsound import playsound
import pyautogui

x = 1

while x < 100:
    pyautogui.press('volumeup')
    x+=1
    
playsound('audio.mp3')
