def is_leap(year):
    leap = False
    leap1 = True
    if((year % 400 == 0) or  (year % 100 != 0) and  (year % 4 == 0)):
        return leap1
    else :
       return leap
