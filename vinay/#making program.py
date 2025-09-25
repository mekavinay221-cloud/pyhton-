#making program
marks = int(input("Enter the marks (0-100): "))
 
if marks < 35:
    print("Fail")
elif marks < 59:
    print("Pass")
elif marks < 84:
    print("First Class")
else: 
    print("Distinction")
    
 