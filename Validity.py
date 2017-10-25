from datetime import datetime, timedelta

date = datetime.now()

#add these separators if needed in code..date = datetime.strptime()

modified_date = date + timedelta(days=3)

#add seprators if needed in code..datetime.strftime(modified_date, "%Y/%m/%d")

print ('Signup date')
print (date)
print ('valid upto')
print (modified_date)
