# nested loops: 'for', 'while' 

# nine times table - using 'for'
for i in range(1,10):
    for j in range(i):
        j = j + 1
        print ("%d*%d=%-3d"% (i,j,i*j),end="")
    print ("")

# nine times table - using 'while'
i=1
while i<10:
    j=1
    while j<=i:
        print("%d*%d=%d\t"%(j,i,j*i),end="")
        j+=1
    print()
    i+=1

# later, we'll learn sometihng called 'recursion'
# nine times table - recursion
def multiplication_table(n):
   if n < 1:
      return
   multiplication_table(n - 1)
   for m in range(1, n + 1):
      print("%d*%d=%d" % (m, n, m * n), end="\t")
   print()
multiplication_table(9)


