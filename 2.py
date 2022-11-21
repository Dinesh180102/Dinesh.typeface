string1=input()
string2=input()
l=len(string2)
c=string2[l-1]
cop=0;
for i in range(0,len(string1)):
  if(string1[i]==c):
    cop=cop+1
print(cop)
