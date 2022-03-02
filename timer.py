# input current time
time = list(input('time>'))

# determine am or pm
if time[-2] == 'a':
    am_pm = 'am'
else:
    am_pm = 'pm'

# remove am/pm from time input
del time[-2:]

# turn time into a string then into an integer
number = ''
for item in time:
    number += str(item)
time_int = int(number)

# input timer hours and add to time
timer_hours = int(input('timer hours>'))
time_new = time_int + timer_hours


# function for switching am/pm
def switch(x):
    if x == 'am':
        return 'pm'
    elif x == 'pm':
        return 'am'


# put new time in the right format
while time_new > 12:
    am_pm = switch(am_pm)
    time_new -= 12

# correct am/pm if end time is 12
if time_new == 12 and timer_hours != 0:
    am_pm = switch(am_pm)

# correct am/pm if initial time is 12
if time_int == 12 and timer_hours != 0:
    am_pm = switch(am_pm)

# create and print new time output
time_final = str(time_new) + am_pm
print(time_final)
