import pandas as pd
import time
import pyautogui as pg
import pygetwindow as gw
import pyperclip

target_list = pd.read_csv(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\list.csv", encoding="euc-kr", header=None)

edit_list = target_list.values.tolist()

address = rf"\\kjnas\KJNAS\1.기획부\9.개발팀\ERP_TAX_CLEARANCE_SALARIES"

print(f"총 {len(edit_list)} 건 ING")

for index, i in enumerate(edit_list):
    print(f"{i[1]}_{i[2]} 변환 총 {len(edit_list)} 건 중 : {index} 번 진행")
    time.sleep(1)

    employee_one_bth = pg.locateOnScreen(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_BUS_DRIVING_INFO\PNG\employee_1_bth.PNG")
    pg.moveTo(employee_one_bth)
    pg.click()

    pyperclip.copy(i[1])
    time.sleep(0.3)
    pg.hotkey("ctrl", "v")
    time.sleep(0.3)
    pg.press("tab")
    time.sleep(0.3)
    pg.hotkey("ctrl", "v")
    time.sleep(0.3)

    pg.press("f11")

    time.sleep(2)
    pg.click()

    test_bth = pg.locateOnScreen(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_BUS_DRIVING_INFO\PNG\test_bth.PNG")
    pg.moveTo(test_bth)
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
    file_form_bth = pg.locateOnScreen(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_BUS_DRIVING_INFO\PNG\tax_file_form_bth.PNG")
    pg.moveTo(file_form_bth)
    pg.click()
    pg.press("down")
    pg.press("enter")

    time.sleep(1)
    file_name_bth = pg.locateOnScreen(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_BUS_DRIVING_INFO\PNG\tax_file_name_bth.PNG")
    pg.moveTo(file_name_bth)
    pg.click()

    time.sleep(1)
    pyperclip.copy(f"{i[1]}_{i[2]}")
    pg.hotkey("ctrl", "v")
    pg.press("enter")

    time.sleep(2)
    pg.press("esc", presses=2)
    
    time.sleep(1)
    employee_two_bth = pg.locateOnScreen(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_BUS_DRIVING_INFO\PNG\employee_2_bth.PNG")
    pg.moveTo(employee_two_bth)
    pg.click()

    time.sleep(1)
    ejal_bth = pg.locateOnScreen(rf"\\kjnas\KJNAS\1.기획부\9.개발팀\BIS_BUS_DRIVING_INFO\PNG\ejal_bth.PNG")
    pg.moveTo(ejal_bth)
    pg.click()
    time.sleep(0.5)
    pg.click()
print("ALL_COMPLETE")