f = open('/Users/nitin/pfiles/example.txt','r')
print(f.read()) # read file
f.close()

f = open('/Users/nitin/pfiles/example.txt','r')
print('only part of file')
print(f.read(4)) # read parts of the file
f.close()

f = open('/Users/nitin/pfiles/example.txt','r')
print('line from file')
print(f.readline())
print(f.readline())
f.close()

f = open('/Users/nitin/pfiles/example.txt','r')
for x in f:
    print(x)
f.close()

f= open('/users/nitin/pfiles/example.txt','w')
print(f.write('This will over write everything'))
f.close()

f= open('/users/nitin/pfiles/example.txt','a')
print(f.write(' \n hello my name is Trupti.'
              '\nthis is line 2'))
f.close()

f = open('/Users/nitin/pfiles/example.txt','r')
for x in f:
    print(x)
f.close()

#created newfile through program
f=open('/users/nitin/pfiles/example1.txt','x')
print(f.write('new file creation'))
f.close()

import os
os.remove('/users/nitin/pfiles/example1.txt')
print('file removed')