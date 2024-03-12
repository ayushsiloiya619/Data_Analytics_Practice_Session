import datetime as gm
today=gm.date.today()
class time:
    def get_today_date_details(self):
        print("Today Date is:", today)
        print("Current Year is:",today.year)
        print("Current Month is:",today.month)
        print("Today's Day:",today.day)
obj=time()
obj.get_today_date_details()