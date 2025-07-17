"""try:
    result=20/0
except ZeroDivisionError:
    print("can not divide by zero")"""
"""try:
    value=int(input())
    res=20/value
except ValueError:
    print("invalid input please enter a number")
except ZeroDivisionError:
    print("can not divide by zero")"""
"""try:
    value=int(input())
    res=20/value
except (ValueError,TypeError,ZeroDivisionError) as e:
     print(f"an error occured:{e}")"""
try:
    value=int(input())
    res=20/value
except ValueError:
    print("invalid input please enter a number")
except ZeroDivisionError:
    print("can not divide by zero")
else:
    print(f"successfully read value:{res}")
finally:
    print("cleanup completed")
     


