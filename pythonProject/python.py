#Write a program that print the following shape (pyramid) by using nested for loops.
#for i in range(9,0,-1):
#    for j in range(i,0,-1):
#        print(j, end='')
#    print()

#write a progra  that prints the following chapter session
for chapter in range(1,3):
    print(chapter)
    for baslik in range(1,6):
        print(str(chapter)+ '.'+str(baslik))
        for altbaslik in range(1,5):
            print(str(chapter)+'.'+str(baslik)+'.'+ str(altbaslik))
        print()
print("------------------------------------")

n=int(input("n değerini giriniz: "))
s=int(input("s değerini giriniz: "))

for satir in range (n):
    for sutun in range(n):
        if satir==sutun:
            print(s, end=" ")
        else:
            print(0, end=" ")
    print()