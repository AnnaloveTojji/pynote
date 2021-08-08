#grade calculator
print("*** grade calculator ***")
score = int(input("Please enter a score:"))
if score >= 90: print("A")
elif score >= 80: print("B")
elif score >= 70: print("C")
elif score >= 60: print("D")
else : print ("E")

#function
# define a function
def calculator(n):
   if n >= 90: return "A"
   elif n >= 80: return "B"
   elif n >= 70: return "C"
   elif n >= 60: return "D"
   else : return "E"
print("*** call the calculator function ***")
score2 = int(input("Please enter a score:"))
print("Your grade is: %s"%(calculator(score2)))

