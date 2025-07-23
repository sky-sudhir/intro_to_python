
age=input("Enter your age(1-120)")

def validateInput():
    num=0
    try:
        num = int(age)
    except ValueError:
        return "Enter a valid number"


    if(num>120 or num<1):
        return "The age is out of range"
    
    return f"You entered a valid age {num}"
    
val=validateInput()
print(val)