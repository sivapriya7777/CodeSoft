a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("The operations are:"
      "\n1.add",
      "\n2.sub",
      "\n3.multiply",
      "\n4.divide")
while True:
    op=input("select your choice:")
    if op in ['1','2','3','4']:
        if(op=='1'):
            print(a,"+",b,"=",(a+b))
        elif(op=='2'):
            print(a,"-",b,"=",(a-b))
        elif(op=='3'):
            print(a,"*",b,"=",(a*b))
        elif(op=='4'):
            if(b!=0):
                print(a,"/",b,"=",(a/b))
            else:
                print("division by zero error")
        next_calc=input("let's do the next calculation?(yes/no):")
        if next_calc.lower()=="no":
            break
    else:
        print("invalid number")
    
