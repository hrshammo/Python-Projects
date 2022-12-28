import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = int(time.strftime( '%H' ))
print(timestamp)

if(6 < timestamp <10):
    print("Good Morning ")
elif(10< timestamp < 16):
    print("It's Mid day ")
elif(16< timestamp <18):
    print("Good noon ")
elif(18< timestamp<21):
    print("Good Evening ")
else:
    print("It's night")