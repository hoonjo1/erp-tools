import time
import pyautogui as pg
import pygetwindow as gw
import pyperclip

def erp_driving_score_route_upload_f(company, dates):
    if company == "경진여객":
        route_number = ["0","1","2","3","4","6","7","8","9","10","11","12","13","14","15"] # kj
    elif company =="용남고속":
        route_number =["2","4","5","6","11","16","18","22","24","29","33","41","44","46","53","55","56","66","67","68","70"]
    elif company == "제부여객":
        route_number = ["9","10","12","14","15","17","18","19","20","22","23","25","27","28","29","30","31","32"] # jb

    for date in dates:
        print(f"{company} 총 {len(dates)} 일 : {date} 진행")
        window = gw.getWindowsWithTitle("  휴게시간 자료 관리")[0]
        pg.click(window.left + 10, window.top + 10)
        time.sleep(0.3)
        pg.press("f6")
        time.sleep(0.3)
        pyperclip.copy(date)
        pg.hotkey("ctrl", "v")
        pg.press("tab")

        for index, route in enumerate(route_number):
            print(f"{company} 총 {len(route_number)} 노선 : {index} 노선 진행")
            pg.press("down", presses=int(route))
            pg.click(window.left + 10, window.top + 10)
            time.sleep(0.2)
            pg.press("f8")
            time.sleep(0.2)
            pg.press("y")
            time.sleep(5)
            pg.press("f2")
            time.sleep(3)
            pg.press("enter")
            pg.press("tab")

    print("ALL_COMPLETE")