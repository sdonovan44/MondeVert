from datetime import datetime
excel_date = 1678180427
dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + excel_date - 2)
tt = dt.timetuple()
print (dt)