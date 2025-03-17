with open("sample.txt","r") as f:
    count=0
    data= f.read()
    num= data.split(",")
    for val in num:
        if int(val)%2==0:
            count+=1
    print(count)
