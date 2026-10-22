tt=(10,20,30,40,50,60,70)
print(min(tt))
print(max(tt))
print(sum(tt))
print(len(tt))
print(tt[0])
print(min(tt))
print(list(reversed(tt))) 
print(tuple(reversed(tt)))
print(tt.index(30))
print(tt.count(10))
print(tt[0:3])

set
s={10,20,30,40,50,60,70}
print(s)
a= {10,20,30,40,50,60,70}
print(min(a))
print(max(a))
print(sum(a))
print(len(a))

a= {10,20,30,40,50,60,70}
a.add(80)
print(a)

a={10,20,30,40,50,60,70}
a.remove(30)
print(a)

a={10,20,30,40,50,60,70}# discard agar value exist nahi karta hai to error nahi aayega
a.discard(80)
print(a)

a={10,20,30,40,50,60,70}
a.pop()
print(a)

a={10,20,30,40,50,60,70,70}
b={10,20,30,40,50,60,70,70}
print(a.union(b))

a={10,20,30,40,50,60,70}
b={10,20,30,40,50,60,70}
print(a.intersection(b))

a={10,20,30,40,50,60,70}
b={10,20,30,40,50,60,70}
print(a.difference(b))
