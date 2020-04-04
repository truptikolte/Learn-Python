username = {'ayushi' : 'Ayushik', 'sakshi ':'SakshiK'}
print('Please enter your name : ','')
name = input()
print(name)
#print(username[name])
if name in username:
    print('Your user name is : ', username[name])
else:
    print('invalid username')
    print('do you want to add new user name? please type yes or no ')
    yesno = input()
    if yesno == 'Yes' or yesno == 'yes' or yesno=='y' or yesno=='Y':
        while True:
            print('Please enter youe name :')
            newname = input()
            count = 0
            #print(username.values())
            if newname in username.values() :
                print('user name already exist')
            else:
                username[name] = newname
                print('Data updated')
                break
    else:
        print('Thank you')
print(username)
