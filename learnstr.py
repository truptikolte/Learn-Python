str1 = 'welcome to'
str2 = 'python programming'
print ('String1 :',str1)
print ('String2 :',str2)
print('First letter of string 1:',str1[0]) # print first character from first string
print('Last letter of string 2: ',str2[-1]) # print last character from last string
print('Last letter from string 1:',str1[-1])
# extract welcome from first string
print('Extract string 1: ',(str1[0:7])) #index start on from 0
#find function
str3 = 'stringfunction1'
print(str3.find('tion')) # return the starting index number of substring
print(str3.find('in'))
print(str3[6:14]) #extract substring from string
print(str3.replace('ing',''))
print(str3.isalpha())
splitstr = 'Ayushi,Sakshi,Nitin,Swati'
print(splitstr.split(',')) #split string on base of comma
str4 = 'asevM#€¡'
print(max(str4))# return maximum ascii value of character from string
print (min(str4)) # return minimum assciv value of character from string
