# Exercise 1

import datetime

current_date = datetime.datetime.today()

before_five_days = current_date - datetime.timedelta(days = 5)

print("Before five days from today:", before_five_days.date())


# Exercise 2

import datetime

def yesterdayTodayTomorrow():
    current_date = datetime.date.today()
    yesterday = current_date - datetime.timedelta(days = 1)
    tomorrow = current_date + datetime.timedelta(days = 1)

    print("Yesterday's date:", yesterday)
    print("Today's date:", current_date)
    print("Tomorrow's date:", tomorrow)

yesterdayTodayTomorrow()

# Exercise 3

import datetime

current_datetime = datetime.datetime.now()

print("Original datetime:")
print(current_datetime)

datetime_without_microseconds = current_datetime.replace(microsecond = 0)

print("Datetime without microseconds:")
print(datetime_without_microseconds)


# Exercise 4

import datetime

date_one = datetime.date.today()
date_two = datetime.date(2028, 6, 15)

difference = date_two - date_one
difference_in_seconds = difference.total_seconds()

print("Two date difference in seconds:", difference_in_seconds)

