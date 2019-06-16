i=int(input()) 
jk=list(map(int,input().split()))
list_set = set(jk) 
unique_list = (list(list_set))  
for x in unique_list:
  if (jk.count(x)==1): 
    print(x)
