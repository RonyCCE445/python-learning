name = input("Enter your name:")
dm = int(input("Enter your marks in discrete mathematics: "))
pr = int(input("Enter your marks in python programming: "))
st = int(input("Enter your marks in Statistics: "))

print("The student result is displayed here: ")
print("Student: ", name)
print("Discrete Mathematics: ", dm)
print("Python Programming: ", pr)
print("Statistics: ", st)
total = dm+pr+st
print("Total: ",total)
avg = total/3
print(f"Average: {avg:.2f}")
pm = 40
print("Passing marks: ",pm)
print("Passed: ",(avg > pm))


