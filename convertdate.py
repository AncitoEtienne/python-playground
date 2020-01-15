#by Ancito and David
from datetime import datetime

birthday = "1-May-12"
date_format = "%d-%b-%y"

parsed_date = datetime.strptime(birthday, "%d-%b-%y")
date_str = parsed_date.strftime("%-m/%-d/%Y") # 01/11/17
print(date_str)