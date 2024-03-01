#calculator

n1 = int(input("whats the first number?: \n"))
n2 = int(input("whats the second number?: \n"))

#Add

def add(n1, n2):
    return n1 + n2 

#Subtract
def subtract(n1, n2):
    return n1 - n2 

#multiply
def multiply(n1, n2):
    return n1 * n2 

#Divide
def divide(n1, n2):
    return n1 / n2 

operations = { 
    
    "+" : add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculate(n1, n2, do):
    op = operations[do]
    answer = op(n1, n2)
    return answer

for i in operations:
    print (i)

do = input ("Pick an operation from the line above\n")

result = calculate(n1, n2, do)
print (f"{n1} {do} {n2} = {result}")

def calculate2 (result):
    n3 = input ("enter the number \n")
    do = input ("select another operation \n")
    answer = calculate(result,n3,do)
    return answer

flag = True

while flag:
    temp= input("do you want to continue operating on the previous result? Y/N \n")
    temp=temp.lower()
    if temp == "n":
        break
    else:
        answer = calculate2(result)
        print (f"second answer is {answer}")






