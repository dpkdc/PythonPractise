# i=1
# sum=int(input("Enter a number :"))
# while i<=10:
#     print(sum*i)
#     i +=1
#
# list= [34,56,3,4,45,56,23,56,78,67]
# i=0
# while i<len(list):
#     print(list[i])
#     i+=1

tup=(23,45,67,43,55,56,7,8,99,456,556)
input_data=int(input("Enter a number from 23,45,67,43,55,56,7,8,99,456,556 ="))
i=0
while i<len(tup):
    if tup[i]==input_data:
        print(input_data," Is present in tuple")
        break
    else:

        i+=1
    print(input_data, " Is not present in tuple")









