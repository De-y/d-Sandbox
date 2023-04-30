import pyautogui, time

time.sleep(3)

# Open the text file to read from
with open("typing_data.txt", "r") as f:
    lines = f.readlines()

# Iterate over the lines and type them out
for line in lines:
    pyautogui.typewrite(line)
    pyautogui.press("Enter")

