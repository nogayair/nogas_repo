letters=['a','b','c']
replace={'a':'d','b':'e','c':'f'}
enigmad=[]
for letter in letters:
        enigmad.append(replace[letter])
print(enigmad)


numbers=[1,2,3,4,5,6,7]
list1=[]
list2=[]
if len(numbers)%2==0:
    list1=numbers[:(int(len(numbers)/2))]
    list2=numbers[int(len(numbers)/2):]
else:
    list1=numbers[:int(len(numbers)/2+0.5)]
    list2=numbers[int(len(numbers)/2+0.5):]
print(list1)
print(list2)
