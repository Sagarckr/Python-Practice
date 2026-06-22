# error handling

try :
    a = 10 + "tea"

except ZeroDivisionError as message:
    print(message)

except NameError as message:
    print(message)

except Exception as e:
    print(e)