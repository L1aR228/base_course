year = int(input())

if year % 100 == 0:
    print('ne visokosni')
elif ((year % 4 == 0) or (year % 400 == 0)):
    print('Visokosni')

else:
    print('Ne visokosni')