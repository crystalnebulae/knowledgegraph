from win32gui import GetWindowText, GetForegroundWindow
import time
from datetime import datetime
from pathlib import Path
dt_l = datetime.now()
log_startstamp = dt_l.strftime("%Y-%b-%d_%H%M_%S_%f")
log_time = dt_l.strftime("%Y-%b-%d_%H:%M:%S:%f")
log_path = Path.joinpath(Path(__file__).parent.parent, "kg_logs\\activewinlog_" + log_startstamp + ".csv")
f = open(log_path, "w", encoding="utf-8")
f.write("Window Title, Start Time, End Time, Start Timestamp, End Timestamp\n")
last_win = GetWindowText(GetForegroundWindow())
last_timestamp = log_startstamp
last_time = log_time
write_counter = 0
while True:
    time.sleep(0.3)
    write_counter += 1
    if(write_counter % 30 == 0):
        f.close()
        f = open(log_path, "a", encoding="utf-8")

    curr_win = GetWindowText(GetForegroundWindow())
    
    if(write_counter % 200 == 0):
        write_counter = 0
        dt = datetime.now()
        curr_timestamp = dt.strftime("%Y-%b-%d_%H%M_%S_%f")
        curr_time = dt.strftime("%H:%M:%S:%f")
        change_str = last_win + "," + last_time + "," + curr_time + "," + last_timestamp + "," + curr_timestamp + "\n"
        f.write(change_str)
        last_win = curr_win
        last_timestamp = curr_timestamp
        last_time = curr_time
    if(curr_win != last_win):
        dt = datetime.now()
        curr_timestamp = dt.strftime("%Y-%b-%d_%H%M_%S_%f")
        curr_time = dt.strftime("%H:%M:%S:%f")
        change_str = last_win + "," + last_time + "," + curr_time + "," + last_timestamp + "," + curr_timestamp + "\n"
        f.write(change_str)
        last_win = curr_win
        last_timestamp = curr_timestamp
        last_time = curr_time