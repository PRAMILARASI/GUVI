mp,jp=map(str,input().split())

ax=0

if len(mp)>len(jp):

  mp,jp=jp,mp

i=0

while i<len(mp):

  ax+=(ord(jp[i])-ord(mp[i]))

  i+=1

for i in range(i,len(jp)):

  ax+=ord(jp[i])-ord('a')+1

print(ax)
