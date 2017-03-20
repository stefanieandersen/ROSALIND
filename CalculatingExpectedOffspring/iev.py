# http://rosalind.info/problems/iev/

dataset = open('rosalind_eo.txt')
P = [int(i) for i in dataset.readline().split()]

total = sum(P) * 2

exp_aa = 0

for i in range(len(P)):
    if i <= 2:
        pass
    else:
        if i == 3:
            exp_aa += 0.25 * 2*P[i]
        elif i == 4:
            exp_aa += 0.5 * 2*P[i]
        else:
            exp_aa += 1 * 2*P[i]
            
print total - exp_aa
