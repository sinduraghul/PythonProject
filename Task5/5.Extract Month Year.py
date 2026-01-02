import datetime  # import datetime from python

#using lambda function to print current year month and day
f = lambda : print("Year: ", datetime.datetime.now().year,
", Month: ", datetime.datetime.now().month,
", Day: ", datetime.datetime.now().day)
f() #calls lambda function