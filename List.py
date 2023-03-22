myList = ["apple","banana","mango","papaya","papaya"]
print(type(myList))

print(myList)

print(len(myList))
list1=["a",True,5,"abc"]
print(list1)
thisList = ["apple","banana","cherry"]
print(thisList[0])
print(thisList[-3])

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:5])

print(thislist[:4])

print(thislist[2:])

if "apple" in thislist:
    print("yes,it is present")

thislist[1]="blackcherry"
print(thislist)

thislist[1:3]= ["papaya","grapes"]
print(thislist)

thislist[4:6]= ["papaya","grapes","guava"]
print(thislist)

thislist.insert(2,"watermelon")
print(thislist)

thislist.append("pomegranate")
print(thislist)

abc = ["aam","aaam"]
thislist.extend(abc)
print(thislist)

thislist.remove("aam")
print(thislist)

thislist.pop(2)
print(thislist)

del thislist[3]
print(thislist)

for x in thislist:
    print(x)

lis = ["orange","mango","kivi","pineapple"]
lis.sort()
print(lis)

lis.sort(reverse=True)
print(lis)

thislist1 = ["banana", "Orange", "Kiwi", "cherry"]

thislist1.sort()

print(thislist1)

thislist1.sort(key=str.lower)

print(thislist1)

thislist1.reverse()

print(thislist1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list2=["why are you going to muzaffarpur"]

a=list2.pop()
print(a)

thislist = ["apple", "banana", "cherry"]
a = thislist.pop()
print(len(a))

sentence = "why are you going to muzaffarfur"
words = sentence.split()
p = words.pop()
print(p)
print(len(p))