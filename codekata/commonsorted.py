aa1 = list(map(int,input().split()))
aa2 = list(map(int,input().split()))
aa3=  aa2[0:aa1[0]]
aa4 = aa2[aa1[0]:aa1[0]+aa1[1]]
for i in aa4:
  if aa3.count(i) >= 1:
    print(i,end=' ')
