#define a set (sets are unorder)
set1= {'lipstik','eyeshdow','nailpaint','eyeliner'}
print('Make Up set Declair: ',set1)
#insert element in set
set1.add('maskara')
print('Make Up set add: ',set1)
#Update item in set
set1.update(['compact','lip_bam'])
print('Make Up set update: ',set1)
#remove item from set
set1.remove('lip_bam')
print('Make Up set remove: ',set1)
set1.discard('eyeliner')
print('Make Up set : ',set1)
set1.discard('eyeh')
print('Make Up set : ',set1)
#set1.remove('eyes')
#print('Make Up set : ',set1)
#using pop will remove last item from set
mypop = set1.pop()
print(mypop)
print('Make Up set : ',set1)
#length of python
print(len(set1))
set2= {1,3,5,7,9,0}
set3={2,3,4,5}
print(set2 & set3) # intersection of two sets
print(set2 | set3) # unioin of two sets
print(set2.difference(set3)) #  return difference between two sets