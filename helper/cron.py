from datetime import date, datetime

from NailSalon.settings import BASE_DIR

def open_time_job():
    import helper.techs_queue as techs_queue
    current_date = date(2022, 12, 11)
    print(f"[{current_date}]")
    techs_queue.build_fresh_wait_queue(current_date, f"{BASE_DIR}/helper/techs_queue")
    print(f"- Built fresh queue at [{datetime.now().time()}]\n")
    
def appointment_timeout_job():
    pass

def appointment_buildframe_job():
    pass