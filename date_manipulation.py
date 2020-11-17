import datetime as dt

today = dt.date.today()
#subtract 13 days
thirteen_days = dt.timedelta(days = 13)
print(type(thirteen_days))
print(thirteen_days)
past_day = today - thirteen_days
print(past_day)

next_year_day = dt.date(today.year+1, today.month, today.day)

print(next_year_day)

date_difference = next_year_day - past_day
print(date_difference)

date_from_string = dt.date.fromisoformat("")
print(date_from_string)

