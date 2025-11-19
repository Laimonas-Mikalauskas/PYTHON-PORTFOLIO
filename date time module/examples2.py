# Example 5
from datetime import datetime

start_date = datetime(2025, 6, 15, 15, 15, 15)

mail_to_inform_about_start_date = f"""
Hello,\n
\n
Thank you for using or service to buy ticket.\n
\n
Ticket number: 12345\n
\n
Event: Super programmers day\n
Doors open: {start_date}
"""

print(mail_to_inform_about_start_date)

# Example 4
# from datetime import datetime
#
# now = datetime.now()
# lock_date = datetime(2099, 1, 1)
#
# print(f'Now: {now}')
# print(f'Lock date: {lock_date}')
#
# if now > lock_date:
#     print('Irasas uzrakintas!')


# Example 3
# from datetime import datetime
#
# my_datetime = datetime(2010, 12, 31, 23, 59, 59)
# my_datetime_2 = datetime(2010, 12, 31)
# print(my_datetime)
# print(my_datetime_2)


# Example 2
# from datetime import datetime
#
# def is_monday(day):
#     if not isinstance(day, int):
#         raise ValueError('Day should be integer')
#     if day == 0:
#         return True
#     return False
#
# def book_table(day):
#     if not isinstance(day, int):
#         raise ValueError('Day should be integer')
#     if day < 0 or day > 6:
#         raise ValueError('Table can not be booked for not existing days!')
#
#     monday = is_monday(day)
#     if monday:
#         raise ValueError('Table can not be booked on mondays!')
#     return True
#
# now = datetime.now()
# week_day = now.day
#
# try:
#     book_table(week_day)
# except Exception as ex:
#     print(ex)

# Example 1
# from datetime import datetime
#
# now = datetime.now()

# print(now)
# print(now.weekday())
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)
