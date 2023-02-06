def traingle(n):
   return (n//2)*n,n*3
n=int(input("A: "))
print("TTU yuzasi -",traingle(n)[0])
print("TTU perimetri -",traingle(n)[1])
print("3ta TTU yuzasi -",traingle(n)[0]*3)
print("3ta TTU perimetri -",traingle(n)[1]*3)
