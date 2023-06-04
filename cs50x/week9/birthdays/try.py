from cs50 import SQL

db = SQL("sqlite:///birthdays.db")


name_month_day = db.execute("SELECT name,month,day FROM birthdays")
birthday_list = {}

for items in name_month_day:
    if items["name"] not in birthday_list:
        birthday_list[items["name"]] = str(items["month"]) + "/" + str(items["day"])

print(birthday_list)