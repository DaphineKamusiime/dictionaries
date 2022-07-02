food_dict={}
food1=input("enter your first favourite food")
food_dict[1]=food1
food2=input("enter your second favourite food")
food_dict[2]=food2
food3=input("enter your third favourite food")
food_dict[3]=food3
food4=input("enter your fourth favourite food")
food_dict[4]=food4

print(food_dict)
getrid=int(input('which food do you want to remove'))
del food_dict[getrid]
print(sorted(food_dict.values()))

