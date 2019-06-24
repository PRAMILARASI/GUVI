s=input()

r=input()

ga=[]

if (s.isalpha() or " " in s) and (r.isalpha() or " " in r):

    s=list(s.split(" "))

    r=list(r.split(" "))

    for i in s:

        if s.count(i) > r.count(i) and i not in g:

            ga.append(i)

    for i in r:

        if r.count(i)>s.count(i) and i not in ga:

            ga.append(i)

    print(*ga)

else:

    for i in s:

        if s.count(i)>r.count(i) and i not in g:

            ga.append(i)

    for j in r:

        if r.count(j)>s.count(j) and j not in ga:

            ga.append(j)

    print(*ga)
