import pyautogui
import time

amt = 1.25
# # Open web browser and go to YouTube
# pyautogui.hotkey('ctrl', 'alt')
# time.sleep(2)
# pyautogui.hotkey('ctrl', 't')
# pyautogui.typewrite('youtube.com\n')
# time.sleep(2)

# Search for video and click on first YouTube short
# pyautogui.click(679, 31)  # click on search bar
# pyautogui.typewrite('#minecraft #roblox #shorts #tiktok #viral #games #t3ddy #memes #engraçado #funny #qatar #trobux\n')
# time.sleep(2)
# pyautogui.press('enter')
# time.sleep(2)
# pyautogui.click(708, 229)  # click on first video

def report_video_for_spam():
    time.sleep(amt)
    pyautogui.click(1385, 945)  # click on three icons
    time.sleep(amt)
    pyautogui.click(1395, 866)  # click on report button
    time.sleep(amt)
    pyautogui.click(769, 597)  # click on spam button
    time.sleep(amt)
    pyautogui.click(862, 622)  # click on reason
    time.sleep(amt)
    pyautogui.click(1018, 868)  # click on reason
    time.sleep(amt)
    pyautogui.click(1145, 912)  # click on next
    time.sleep(amt)
    pyautogui.click(1144, 730)  # click on done
    time.sleep(amt)
    pyautogui.click(1145, 665)  # click on done
    time.sleep(amt)
    print('Done with reporting video. Onto the next one!')
    #Make pyautogui go back to the previous page
    pyautogui.click(1216, 29)  # click on done

if __name__ == "__main__":
    var = 230
    for i in range(3):
        var = var
        pyautogui.click(710,var)
        time.sleep(2)
        report_video_for_spam()
        time.sleep(2)
        var = var + 230