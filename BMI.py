# this is a program to calculate a persons BMI 

weight = float (input("enter weight kg:"))
height = float (input("enter height cm:"))


#weight in kg
#height in cm
heightsquared = (height*height)
#BMI = weight / height in m2
BMI= weight / (height **2)
print("your BMI is",BMI)
