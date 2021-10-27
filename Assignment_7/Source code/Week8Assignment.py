file1 = '2000 Nissan              Altra EV                            85.0001999' 
file2 = 'GMC                 EV1                                         85.000'
minn = int(input('Enter the minimum mpg: '))
while(minn < 0):
    print("The mpg needs to be a number between 0 and 100")
    minn = int(input('Enter the minimum mpg: '))
while(minn > 100):
    print("The mpg needs to be a number between 0 and 100")
    minn = int(input('Enter the minimum mpg: '))
filee = input("Enter the name of the file: ")
if(filee == 'file1'):
    print(file1)
elif(filee == 'file2'):
    print(file2)
else:
    (filee != 'file1' or filee != 'file2')
    filee = input("Enter the name of the file: ")
