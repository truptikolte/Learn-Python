name = input("Enter your name: ")
name = name.lower()
#print(name)
print('Japanese Name: ', end='')
counter = 0
for i in name:
    char = (name[counter])
    counter += 1
    #print(char)
    if char == 'a':
        print('ka', end ='')
    elif char == 'b':
        print('tu', end='')
    elif char == 'c':
        print('mi', end='')
    elif char == 'd':
        print('te', end='')
    elif char == 'e':
        print('ku', end='')
    elif char == 'f':
        print('lu', end='')
    elif char == 'g':
        print('ji', end='')
    elif char == 'h':
        print('ri', end='')
    elif char == 'i':
        print('ki', end='')
    elif char == 'j':
        print('zu', end='')
    elif char == 'k':
        print('me', end='')
    elif char == 'l':
        print('ta', end='')
    elif char == 'm':
        print('rin', end='')
    elif char == 'n':
        print('to', end='')
    elif char == 'o':
        print('mo', end='')
    elif char == 'p':
        print('no', end='')
    elif char == 'q':
        print('ke', end='')
    elif char == 'r':
        print('shi', end='')
    elif char == 's':
        print('ari', end='')
    elif char == 't':
        print('chi', end='')
    elif char == 'u':
        print('do', end='')
    elif char == 'v':
        print('ru', end='')
    elif char == 'w':
        print('mei', end='')
    elif char == 'x':
        print('na', end='')
    elif char == 'y':
        print('fu', end='')
    else:
        print('zi')
