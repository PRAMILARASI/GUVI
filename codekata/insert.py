str=list(input())
l=len(str)-1
if l%2!=0:
    str[l//2]="*"
    str[l//2+1]="*"
else:
    str[l//2]="*"
print("".join(str))
