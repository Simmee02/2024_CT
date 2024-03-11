num1=input()
num2=input()

A1,A2,A3= map(int,num1)
B1,B2,B3= map(int,num2)

print((A3*B3)+(A2*B3)*10+(A1*B3)*100)
print((A3*B2)+(A2*B2)*10+(A1*B2)*100)
print((A3*B1)+(A2*B1)*10+(A1*B1)*100)
print((A3*B3)+(A2*B3)*10+(A1*B3)*100+((A3*B2)+(A2*B2)*10+(A1*B2)*100)*10+((A3*B1)+(A2*B1)*10+(A1*B1)*100)*100)

