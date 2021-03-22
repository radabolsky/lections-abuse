import subprocess
import pyautogui
import time
import webbrowser
import pandas as pd
import datetime


def by_id_and_pass(zoomid, password):
    subprocess.call(r"C:\Users\Vladislav\AppData\Roaming\Zoom\bin\Zoom.exe")
    time.sleep(1)
    join_btn = pyautogui.locateCenterOnScreen('join-button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    pyautogui.write(zoomid)
    pyautogui.keyDown('Enter')
    pyautogui.write(password)
    pyautogui.keyDown('Enter')


def by_url(url):
    webbrowser.open(url, new=0, autoraise=True)
    pyautogui.keyDown('Enter')


while True:
    now = str(datetime.datetime.today().weekday()) + " " + str(datetime.datetime.now().strftime("%H:%M"))
    df = pd.read_csv('timings.csv', )
    if now in str(df['timings']):
        row = df.loc[df['timings'] == now]
        func_type = str(row.iloc[0, 1])
        if func_type == 'id':
            zoomid = str(row.iloc[0, 2].copy())
            password = str(row.iloc[0, 3].copy())
            by_id_and_pass(str(zoomid), str(password))
        else:
            by_url(str(row.iloc[0, 2]))
    else:
        print(now)
        print(str(df['timings']))