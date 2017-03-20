# http://rosalind.info/problems/fibd/

months = 91 #n given
lifespan = 16 #m given

age = [0] * lifespan
age[0] = 1

for month in range(months-1):
    print(age)
    
    babies = 0;
    for i in range(lifespan-1, 0, -1):
        if i > 0:
            babies += age[i]
            
        age[i] = age[i-1]
        
    age[0] = babies

print(age)  
        

print sum(age)
