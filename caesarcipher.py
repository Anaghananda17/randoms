from random import *
alphabets = list(map(chr,range(ord('a'),ord('z')+1)))
text = input("Enter the text to be encrypted").lower()
temp = []
shift = randint(1,9)
i=0
while i<len(text):
    j = alphabets.index(text[i])
    j+=shift
    temp.append(alphabets[j])
    i+=1
print("The encrypted text is ",end=" ")
for i in range(0,len(temp)):
    print(temp[i],end="")
ch = input("\nDo you want to decrypt? Enter yes or no").lower()
if ch == "yes":
    temp1 = []
    for i in range(0,len(text)):
        j  = alphabets.index(temp[i])
        j-=shift
        temp1.append(alphabets[j])
    print("The decrypted text is ",end=" ")
    for i in range(0,len(temp1)):
        print(temp1[i],end="")
else:
    exit(0)
