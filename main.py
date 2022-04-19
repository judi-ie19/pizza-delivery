food=("nuts","mango juices","chicken","pizza")
prices=[21,79,50,45]

myorderfood=[]
myordercost=[]

print("welcome to Lucioles")
print("can i get your order?")

foodOrder=input("please enter item")
if foodOrder=="mango juice":
    myorderfood.append(food[1])
    myorderfood.append(prices[1])
    print()    
