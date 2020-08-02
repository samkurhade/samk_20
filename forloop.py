list1=[["harry",1],[ "larry",2],[ "carry",3],["marie",4]]


for item,lollypop in list1:
    print(item, "and lolly is", lollypop)

dict1=dict(list1)
print(dict1)


for item,lollypop in dict1.items():
    print(item, "and lolly is", lollypop)

for item in dict1:
    print(item)

list2=["roy","if",1,34,45,5,6,3,756,34]
for i in list2:
    if str(i).isnumeric()  and i>6:
        print(i)




