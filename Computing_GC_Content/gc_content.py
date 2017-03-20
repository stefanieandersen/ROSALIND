#http://rosalind.info/problems/gc/

from collections import Counter

rosalind_file = open('rosalind_gc.txt')

best_name = ""
best_ratio = 0

current_name = ""
current_cg = 0
current_at = 1

while True:
    line = rosalind_file.readline()
    if line == "" or line[0] == ">":
        #finish up the previous block
        current_ratio = (1.0 * current_cg) / (current_cg + current_at)
        if current_ratio > best_ratio:
            best_ratio = current_ratio
            best_name = current_name
        
        if (line == ""):
            break
        else:
            #start the new block   
            current_name = line[1:-1]
            current_cg = 0
            current_at = 0
    else:
        linecount = Counter(line)
        current_at += linecount['A'] + linecount['T']
        current_cg += linecount['C'] + linecount['G']

print best_name
print best_ratio
