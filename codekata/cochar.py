W = input()
count = 0
for i in range(len(W)):
  if W[i] in "!@#$%^&*_(){}[]:;,./?":
    count += 1
print(count)
