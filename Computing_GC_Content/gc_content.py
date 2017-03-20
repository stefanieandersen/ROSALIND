#http://rosalind.info/problems/gc/

rosalind_file = open('rosalind_gc.txt')

strings = rosalind_file.read()

indexes = []
index = -1

# Loop while true.
while True:
    # Advance location by 1.
    index = strings.find(">", index + 1)
    
    # Break if not found.
    if index == -1: 
        break
    else:
        indexes.append(index)    

indexes.append(len(strings))


#find the highest cg ratio

iterations = len(indexes) - 1
AT = {}
CG = {}
highest = [0,0]

for i in range(0,iterations):
    key = strings[indexes[i]+1:indexes[i]+14]
    AT[key] = 0
    CG[key] = 0

    for x in strings[indexes[i]:indexes[i+1]]:

        if x == 'A' or x == 'T':
            AT[key] += 1
        elif x == 'C' or x == 'G':
            CG[key] += 1
        else:
            pass
    
    ratio = (CG[key]*100.0)/(AT[key]+CG[key])
    if highest[1] >= ratio:
        pass
    else:
        highest[0] = key
        highest[1] = ratio
        
print highest[0]
print highest[1]
