# bill division
n, k = map(int,input("n,k:").split())
bill = list(map(int,input("bill: ").split()))
b = int(input("b: "))
# cal
anna = (sum(bill)-bill[k])/2
if b > anna:
    print(b-anna)
else:
    print("bon appetit")


