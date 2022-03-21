import time
import pyperclip
import pyautogui as pg
import pygetwindow as gw

def erp_driving_score_file_upload_f(company, dates):
    address = rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_BUS_DRIVING_INFO\ATFER"
    
    for date in dates:
        print(f"{company} 총 {len(dates)} 일 : {date} 진행")
        file_name = f"{company}_{date}_버스운행정보"
        window = gw.getWindowsWithTitle("BIS 자료 Upload(경기BIS)")[0]
        pg.click(window.left + 10, window.top + 10)
        time.sleep(0.5)

        pg.press("f6")
        time.sleep(0.5)
        pyperclip.copy(date)
        pg.hotkey("ctrl", "v")

        find_bth = pg.locateOnScreen(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_BUS_DRIVING_INFO\PNG\find_bth.PNG")
        pg.moveTo(find_bth)
        pg.click()

        time.sleep(1)
        down_bth = pg.locateOnScreen(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_BUS_DRIVING_INFO\PNG\down_bth.PNG")
        pg.moveTo(down_bth)
        pg.click()

        time.sleep(1)
        pyperclip.copy(address)
        pg.hotkey("ctrl", "v")
        pg.press("enter")

        time.sleep(1)
        file_name_bth = pg.locateOnScreen(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_BUS_DRIVING_INFO\PNG\file_name_bth.PNG")
        pg.moveTo(file_name_bth)
        pg.click()

        time.sleep(1)
        pyperclip.copy(file_name)
        pg.hotkey("ctrl", "v")
        pg.press("enter")

        time.sleep(1)
        pg.press("f2")
        time.sleep(0.5)
        pg.press("y")

        time.sleep(70)
        pg.press("enter")

    print("ALL_COMPLETE")