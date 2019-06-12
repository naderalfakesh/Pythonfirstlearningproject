#lists with nums
list1= [1,2,3,4,5,6,7,8,9,0]
list2= list((1,2,3,4,5))
list3=[1]
list4=[1,]
print("Type: ",type(list1) ,"Elements: ",list1)
print("Type: ",type(list2) ,"Elements: ",list2)
print("Type: ",type(list3) ,"Elements: ",list3)
print("Type: ",type(list4) ,"Elements: ",list4)

#lists with strings
lista1= ["a","b","c","d","e"]
lista2= list(("b","c","d"))
lista3=["apple"]
lista4=["orange",]
print("Type: ",type(lista1) ,"Elements: ",lista1)
print("Type: ",type(lista2) ,"Elements: ",lista2)
print("Type: ",type(lista3) ,"Elements: ",lista3)
print("Type: ",type(lista4) ,"Elements: ",lista4)

#list functions 
list1= [1,2,3,4,5,6,7,8,9,0]
list1.clear()
print("Type: ",type(list1) ,"Elements: ",list1)
list1= [1,2,3,4,5,6,7,8,9,0]
print("Type: ",type(list1) ,"Elements: ",list1)
list1.append(10)
print("Type: ",type(list1) ,"Elements: ",list1)
list1.append('apple')
print("Type: ",type(list1) ,"Elements: ",list1)
print(list1.count(2))