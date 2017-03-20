#http://rosalind.info/problems/hamm/

#two given DNA strings
rosalind = open('rosalind_hamm.txt')

string = {}
string[0] = rosalind.readline()[:-1]
string[1] = rosalind.readline()

hamming_distance = 0

for n in range(len(string[0])):
    if string[0][n] == string[1][n]:
        pass
    else:
        hamming_distance += 1
        
print hamming_distance
