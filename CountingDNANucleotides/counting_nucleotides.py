##http://rosalind.info/problems/dna/

##input a string of letters
given_file = open('/home/steffiemarie/Documents/Python/counting.txt')

nucleotides = given_file.read()
As = 0
Gs = 0
Cs = 0
Ts = 0

##read a letter and if it's the right one then
for nucleotide in nucleotides:
    if nucleotide == 'A':
        As = As + 1
    elif nucleotide == 'G':
        Gs = Gs + 1
    elif nucleotide == 'C':
        Cs = Cs + 1
    elif nucleotide == 'T':
        Ts = Ts + 1


print(nucleotides)
print(As, Gs, Cs, Ts)
