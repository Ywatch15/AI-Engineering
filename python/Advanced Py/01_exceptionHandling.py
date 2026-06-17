try:
    # code block where exception could occur
    # a=b
    # a=1
    # b="aa"
    # c=a+b
    a=int(input("Enter the first no: "))
    b=int(input("Enter the second no: "))
    c=a/b
    d=a*b
    e=a+b
except NameError:
    print("The user haven't defined the variable")
except ZeroDivisionError:
    print("The user is trying to divide a number by zero.")
except TypeError:
    print("The data types used in the following operations aren't same.")
except Exception as ex:
    print(ex)
else:
    # print(d)
    # print(e)
    print(c)
finally:
    print("This block will be executed no matter what.")


# except:
#     print("Some problem may have occured.")