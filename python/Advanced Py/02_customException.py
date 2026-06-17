class Error(Exception):
    pass


class dobException(Error):
    pass


year =int(input("Enter your DOB: "))
age=2026-year

try:
    if age<18 or age>23:
        print("You are eligible for this course.")
    else:
        raise dobException
    
except dobException:
    print("You are not eligible for this course.")