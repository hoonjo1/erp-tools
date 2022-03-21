from pyautogui_start import company_sel, start_date_sel, end_date_sel, last_check, date_range, will_work, company_sel_bus_info
from erp_driving_score_file_upload import erp_driving_score_file_upload_f
from erp_driving_score_route_upload import erp_driving_score_route_upload_f

work_sel = will_work()
if work_sel =="휴게시간 DATA UPLOAD":
    user_company_sel = company_sel()
    user_start_date_sel = start_date_sel()
    user_end_date_sel = end_date_sel()
    user_last_check = last_check(user_company_sel, user_start_date_sel, user_end_date_sel)
    dates = date_range(user_start_date_sel, user_end_date_sel)
    upload = erp_driving_score_file_upload_f(user_company_sel, dates)

elif work_sel =="휴게시간 DATA ROUTE_UPLOAD":
    user_company_sel = company_sel()
    user_start_date_sel = start_date_sel()
    user_end_date_sel = end_date_sel()
    user_last_check = last_check(user_company_sel, user_start_date_sel, user_end_date_sel)
    dates = date_range(user_start_date_sel, user_end_date_sel)
    upload = erp_driving_score_route_upload_f(user_company_sel, dates)
        