#http://rosalind.info/problems/revc/

#given DNA strand
s = 'GAAAAAACAACTAGTTGTCGAAACGCATCTCAGGTTCCAATATTCGTACACGATCTCGCTCCCATGCTCGCGTCGGATGCGATCGAGTGATGGTTCTAGCGGAAGACCGTTGCAGTTTGTCGGTAATCTGATTAGTCTCCTAGCTAAATCTTGCTGCGAGTTAGACGTGAGTGTACAGACGTGTTGACCGTCCTCTTTCATGATGACAGTGTTTGCATTATCGTTCGGAACTACGAGAAACTTACAGGAAAGGCCGCAACAAGGCACTAATCAATTACGCACCGCATGTACTTCTAACGTCTAAGCATAAGCTCAGATATCGAGCGGTCGTATTCGACATTCGTGATCGGAAGCATCGCTAATCGAACAGTATTTCTGCCCTAAACCCAAGGTGAGCCGTTTTACAAGCCTGACAAGCATGAGCGTTATGCGAGTGGAAGGCGTGGTGGTAGGAATGGATGGCATAGTACCGAGCTCAGCCGCTCCTCGGGGCTAGTGTTCGCGTGGAGTATATCAACCCTTTACCGGTAACAATCGAGTTTTCTCAAGTGAGGGAGTCTATTCTTGTGTTTGTCACCGACTGAGATAACCCCGGTAGTTCAATCGTCTTCCAGAAACGGTGTCTGTGTCTGAATTTGCCGCAGTGGGGACGAATAAATGAGTGATCGATAGCTGATCTTAACCAAGAAACGTGCTGGTCTCACAGATGAGCGGGTAAGTCCGCGCTACGCGAGCGACATGGATGGGTGATATGCATCACAAGCAATATATGGGCCTTCTTAAGTTTAGCTAGTGGGTCACATTTA'

#start making the complement by reversing the original string
s_reverse = s[::-1]
s_c = []

#finish the complement by matching the nucleotide
for base in s_reverse:
    if base == 'A':
        s_c.append('T')
    elif base == 'T':
        s_c.append('A')
    elif base == 'G':
        s_c.append('C')
    elif base == 'C':
        s_c.append('G')
    else:
        print('Error')
    
s_c = ''.join(s_c)   
print(s_c)
