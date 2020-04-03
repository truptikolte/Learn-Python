mylist = ['Ayushi', 91, 'croftonroad','A',99.99 ]# list can be mixed data type
print('MyList1 : ',mylist)
mylist1 = ['Sakshi', 91]
print('mylist2 : ',mylist1)
#list concatanation
mylist += mylist1
print('List after concatanation', mylist)
#reverse the list
mylist.reverse()
print('reverse list:',mylist)
#remove object from list
mylist.remove(91) #It remove only first object
print('List After remove object : ',mylist)
print(mylist[0]) #print the value from index number
print(mylist[2:5]) #extarct the list accirding to index number i.e slicing
mylist.append('swati') #update the list
print("List after update",mylist)
#insert object in list
mylist.insert(2,'66.6')
print('Insert object in list :',mylist)
