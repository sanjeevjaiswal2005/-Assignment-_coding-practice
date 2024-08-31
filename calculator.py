#Calculator program
print('Please enter your choice')
print('1.Addition\n2.Sub\n3.Mul\n4.Division\n5.Mod\n6.Sqr\n7.Flor')
ch=int(input())
print('ente your number')
a=eval(input())
b=eval(input())
if ch==1:
    Ans=a+b
    print('ANS',Ans)
elif ch==2:
    Ans=a-b
    print('ANS',Ans)
elif ch==3:
    Ans=a*b
    print('ANS',Ans)
elif ch==4:
    Ans=a/b
    print('ANS',Ans)  
elif ch==5:
    Ans=a%b
    print('ANS',Ans) 
elif ch==6:
    Ans=a**b
    print('ANS',Ans) 
elif ch==7:
    Ans=a//b
    print('ANS',Ans) 
else:
    print('PLASE ENTER YOUR CHOICE')           