#1
from datetime import datetime, timedelta
today_date = datetime.now()
five_days_ago = today_date - timedelta(days=5)
print("Today:", today_date.strftime("%d.%m.%Y"))
print("Five days before:", five_days_ago.strftime("%d.%m.%Y"))


#2
from datetime import datetime, timedelta
today_date=datetime.now()
yesterday=today_date - timedelta(days=1)
tomorrow=today_date + timedelta(days=1)
print("Yesterday:", yesterday.strftime("%d.%m.%Y"))
print("Today:", today_date.strftime("%d.%m.%Y"))
print("Tomorrow:", tomorrow.strftime("%d.%m.%Y"))

#3
from datetime import datetime
datetime_without_micros = datetime.now().replace(microsecond=0)
print("Datetime:", datetime.now())
print("Without microseconds:", datetime_without_micros)

#4
import datetime
first_date = input("First date (YYYY-MM-DD HH:MM:SS): ")
scnd_date = input("Second date (YYYY-MM-DD HH:MM:SS): ")
date_format = '%Y-%m-%d %H:%M:%S'
d1 = datetime.datetime.strptime(first_date, date_format)
d2 = datetime.datetime.strptime(scnd_date, date_format)
diff_of_time = d2 - d1
diff_in_seconds = diff_of_time.total_seconds()
print(f"{diff_in_seconds}")