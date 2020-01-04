#counting vowels
import array
s=str(raw_input('Input the string: '))
#s = 'azcbobobegghakl'
vcnt=0
h=('a', 'e', 'i', 'o', 'u')
nVowel=len(h)
for turn in range(nVowel):
    a=int(h[turn] in s);
    vcnt=vcnt+a
print('Number of vowels appearing in the string: '+str(vcnt))

#from MITedX
total = 0
for c in s:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        total += 1
print "Number of occurances of any vowel in the string: " + str(total)