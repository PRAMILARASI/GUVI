f = True
while True:
  mm, op, n = map(str,raw_input().split())
  if op == '/':
    print int(mm) / int(n)
  elif op == '%':
    print int(mm) % int(n)
