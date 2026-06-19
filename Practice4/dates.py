# DATES IN PYTHON
# The datetime module is used to work with dates and times.

import datetime


# Example 1: Current date and time
current_datetime = datetime.datetime.now()

print("Current date and time:")
print(current_datetime)


# Example 2: Get year, month, day and weekday
print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Weekday name:", current_datetime.strftime("%A"))


# Example 3: Create a specific datetime object
custom_datetime = datetime.datetime(2022, 2, 22, 14, 30)

print("Custom datetime:")
print(custom_datetime)


# Example 4: Create a date object
custom_date = datetime.date(2026, 6, 19)

print("Custom date:")
print(custom_date)


# Example 5: Create a time object
custom_time = datetime.time(16, 30, 0)

print("Custom time:")
print(custom_time)


# Example 6: Formatting dates with strftime()
formatted_date_1 = current_datetime.strftime("%B")
formatted_date_2 = current_datetime.strftime("%d/%m/%Y")
formatted_date_3 = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

print("Month name:", formatted_date_1)
print("Formatted date:", formatted_date_2)
print("Formatted date and time:", formatted_date_3)


# Example 7: Difference between two dates
start_date = datetime.date(2026, 6, 1)
end_date = datetime.date(2026, 6, 19)

difference = end_date - start_date

print("Difference between dates:")
print(difference)
print("Days:", difference.days)


# Example 8: Using timedelta
today = datetime.date.today()
after_7_days = today + datetime.timedelta(days=7)
before_3_days = today - datetime.timedelta(days=3)

print("Today:", today)
print("After 7 days:", after_7_days)
print("Before 3 days:", before_3_days)


# Example 9: UTC time using timezone
utc_now = datetime.datetime.now(datetime.timezone.utc)

print("Current UTC datetime:")
print(utc_now)


# Example 10: Timezone with UTC offset
almaty_timezone = datetime.timezone(datetime.timedelta(hours=5))
almaty_time = datetime.datetime.now(almaty_timezone)

print("Current time with UTC+5 timezone:")
print(almaty_time)


# Example 11: Parsing string into datetime using strptime()
date_string = "2026-06-19"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d")

print("Parsed date:")
print(parsed_date)


print("Date examples completed.")