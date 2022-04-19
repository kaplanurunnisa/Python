#write a program that takes an integer n from the user
#and prints all possible combinations of two dices such that the
#sum of these dices is n
#example:
#input:5
#output:
#(1,4)
#(2,3)
#(3,2)
#(4,1)
n=int(input("Hangi sayının kombinasyonlarını görmek istyiorsunuz?: "))
for i in range (0,n):
    for j in range(n,0,-1):
        if (i+j==n):
            print('('+str(i) + ',' +str(j)+ ')')

