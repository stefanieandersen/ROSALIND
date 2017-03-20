#http://rosalind.info/problems/iprb/

AA = 16.0 #k given
Aa = 16.0 #m given
aa = 15.0 #n given

total = AA + Aa + aa

probability_of_aa = (Aa/total * (Aa-1)/(total-1) * .25) + (Aa/total * aa/(total-1) * .5) + (aa/total * Aa/(total-1) * .5) + (aa/total * (aa-1)/(total-1))
answer = 1 - probability_of_aa

print answer
