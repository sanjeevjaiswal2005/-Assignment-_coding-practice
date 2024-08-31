cp=eval(input("Enter the cost price "))
sp=eval(input("enter the sellin price"))
profit=sp-cp
loss=cp-sp
if sp>cp:
print("profi=",profit)
else:
print('loss=',loss)
