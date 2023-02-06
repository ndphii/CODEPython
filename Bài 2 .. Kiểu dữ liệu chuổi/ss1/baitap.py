a = ['nguyen','duc','phi']
b = "python 3 ez"
c,d= "1230321","abcdefg"
result = a if len(a) > len(b) else b
print(result)

reverse = a[::-1] 
print(reverse)

sym = c[None:None:-1]
symm = d[None:None:-1]
# cách 1 s
sym = "symmetry" if sym == c else "unsymmetry"
print(sym)
# cách 2 un
if symm == d:
    print("symmetry")
else:
   print("unsymmetry")
# ý tưởng là input vào 1 chuổi hỗn hợp gồm str và int và output chỉ str
x = int,str(input("enter string:"))
for z in x:
    if z == (x[z] >= 'a' and x[z] <= 'z'):
	    print(z)