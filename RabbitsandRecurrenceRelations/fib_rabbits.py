#http://rosalind.info/problems/fib/

#given: k is rabbit-pair progeny, b is starting pair(s)
k = 3
b = 1
months = 28

#Recursive function

F = [b, b]
n = 2

#for 5 months
while n <= months-1:

    F_n = F[n-1] + k*F[n-2]
    F.append(F_n)
    n = n + 1
    

print(F)
