# -*- coding: utf-8 -*-

import webbrowser as wb
import datetime as dt


datetime = "https://docs.python.org/3/library/datetime.html"
wb.open(datetime)


dt.MINYEAR
dt.MAXYEAR

d1 = "08/10/2017"
d2 = "08/10/2016"
max(d1,d2)

#d1 - d2# TypeError

d1 = dt.date(2017,8,10)
d2 = dt.date(2016,8,10)
max(d1,d2)
print(d1-d2)
print(d2 - d1)

d3 = dt.datetime.now()
#print(d3-d1)# TypeError
print(d1 - dt.date.today)

now = dt.date.today()
print(now)

now = dt.date.now()
#print(now)# AttributeError

now = dt.datetime.today()
print(now)

now = dt.datetime.now()
print(now)



my_age = dt.date.today() - dt.date(1990,8,25); print(my_age)

my_age = (dt.date.today() - dt.date(1990,8,25)).days; print(my_age)

my_age = round((dt.date.today() - dt.date(1990,8,25)).days / 365, 0); print(my_age)



d1 = dt.date(2017,2,31) # ValueError day out of range

century_start = dt.date(2000,1,1)
today = dt.date.today()
print(century_start,"-->", today)
print("We are", today - century_start, "days into this century")
print("We are", (today - century_start).days, "days into this century")

century_start = dt.datetime(2000,1,1,0,0,0); print(century_start)
time_now = dt.datetime.now(); print(time_now)
time_since_century_start = time_now - century_start; print(time_since_century_start)
print("days since century start",time_since_century_start.days)
print("seconds since century start",int(time_since_century_start.total_seconds()))
print("minutes since century start", int(time_since_century_start.total_seconds()/60))
print("hours since century start", int(time_since_century_start.total_seconds()/60/60))


date_and_time_now = dt.datetime.now()
time_now = date_and_time_now.time(); print(time_now)


### TIMEDELTA
today = dt.date.today()
ten_days_later = today + dt.timedelta(days = 10)
print(ten_days_later)
print(((today + dt.timedelta(days = 10)) - today).days)

today = dt.date.today()
ten_days_earlier = today + dt.timedelta(days = -10)
print(ten_days_earlier)



now = dt.datetime.today()
five_min_and_five_sec_later = now + dt.timedelta(minutes = 5, seconds = 5)
print(five_min_and_five_sec_later)

now=datetime.datetime.today()
five_minutes_and_five_seconds_earlier = now+datetime.timedelta(minutes=-5,seconds=-5)
print(five_minutes_and_five_seconds_earlier)

time_now = dt.datetime.now().time()
print(time_now)

thirty_seconds = dt.timedelta(seconds = 30)
time_later = time_now + thirty_seconds# can't use timedelta on time objects TypeError


# we can fix it with functions
def add_to_time(time_object, time_delta):
    import datetime as dt
    temp_date_time_object = dt.datetime(500,1,1, time_object.hour, time_object.minute, time_object.second)
    return (temp_date_time_object + time_delta).time()

time_now= dt.datetime.now().time()
thirty_seconds = dt.timedelta(seconds=30)
print(time_now,add_to_time(time_now,thirty_seconds))

# STRPTIME
# datetime.strptime(): grabs time from a string and creates a date or datetime or time object
# We need to tell the function what format the string is using

# date and time conversion
wb.open("http://pubs.opengroup.org/onlinepubs/009695399/functions/strptime.html")


date = '01-Apr-03'
date_object = dt.datetime.strptime(date, '%d-%b-%y')
print(date_object)

# date don't have attribute "strptime"
date = '01-Apr-03'
date_object = dt.date.strptime(date, '%d-%b-%y')
print(date_object)# AtributeError

date = '30.06.2017'
date_object = dt.datetime.strptime(date, '%d.%m.%Y')
print(date, "-->", date_object)

# no similar thing for time delta
bus_travel_time = '2:15:30'
hours, minutes, seconds = bus_travel_time.split(":")
x = dt.timedelta(hours = int(hours), minutes = int(minutes), seconds = int(seconds))
print(x)

# or write function
def get_timedelta(time_string):
    import datetime as dt
    hours, minutes, seconds = time_string.split(":")
    return dt.timedelta(hours = int(hours), minutes = int(minutes), seconds = int(seconds))

get_timedelta("3:33:15")



# STRFTIME
# Converts a datetime object to a string

now = dt.datetime.now()
print(now)
string_now = dt.datetime.strftime(now, '%m/%d/%y %H:%M:%S')
print(now, "-->", string_now)




f = open('sample_data.csv', 'r')
[line for line in f]

data_tuples = []
with open('sample_data.csv', 'r') as f:
    for line in f:
        data_tuples.append(line.strip().split(","))
        
data_tuples[:10]

data_tuples[0][0]

format_str = '%Y-%m-%d %H:%M:%S'
for i in range(len(data_tuples)):
    data_tuples[i][0] = dt.datetime.strptime(data_tuples[i][0], format_str)
    data_tuples[i][1] = float(data_tuples[i][1])

data_tuples[0][0]
data_tuples[0][0].hour

data_tuples = [(data_tuples[i][0].hour, data_tuples[i][1]) for i in range(len(data_tuples))]
data_tuples[:10]

# function
def get_data(filename):
    data_tuples = list()
    with open(filename,'r') as f:
        for line in f:
            data_tuples.append(line.strip().split(','))
    import datetime
    format_str = "%Y-%m-%d %H:%M:%S"
    data_tuples = [(datetime.datetime.strptime(x[0],format_str).hour,float(x[1])) for x in data_tuples]
    return data_tuples    

buckets = {}
for i in get_data('sample_data.csv'): 
    if i[0] not in buckets:
        buckets[i[0]] = [1, i[1]]
    else:
        buckets[i[0]][0] += 1
        buckets[i[0]][1] += i[1]
        
buckets

# another way
buckets = {}
buckets1 = {}
for i in  get_data('sample_data.csv'):
    buckets[i[0]] = buckets.get(i[0], 0) + 1
for i in  get_data('sample_data.csv'):
    buckets1[i[0]] = buckets1.get(i[0], 0) + i[1]
for k in buckets1:
    buckets[k] = [buckets[k], buckets1[k]]


["Hour: " + str(key) + " Average: "+ str(value[1]/value[0]) for key, value in buckets.items()]


# function
def get_hour_bucket_averages(filename):
    def get_data(filename):
        data_tuples = list()
        with open(filename,'r') as f:
            for line in f:
                data_tuples.append(line.strip().split(','))
        import datetime
        format_str = "%Y-%m-%d %H:%M:%S"
        data_tuples = [(datetime.datetime.strptime(x[0],format_str).hour,float(x[1])) for x in data_tuples]
        return data_tuples        
    buckets = dict()
    for item in get_data(filename):
        if item[0] in buckets:
            buckets[item[0]][0] += 1
            buckets[item[0]][1] += item[1]
        else:
            buckets[item[0]] = [1,item[1]]  
    return [(key,value[1]/value[0]) for key,value in buckets.items()]

get_hour_bucket_averages('sample_data.csv')