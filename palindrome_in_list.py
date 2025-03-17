list1=list(map(int,input("Enter your list: ").split()))
print(list1)
copylist1= list1.copy()
copylist1.reverse()
print(copylist1)

if(copylist1==list1):
    print("Palindrome")
else:
    print("Not Palindrome")


