for leap_year in range(2000,2200):
    if leap_year % 4 == 0:
        if leap_year % 100 == 0:
            if leap_year % 400 ==0:
                print("the year %s is a leap year" % (leap_year))
            else:
                pass
        else:
            print("the year %s is a leap year" % (leap_year))
    else:
        continue
