# this is a program to calculate a persons BMI 

weight = float (input("enter weight kg:")) # asks user to input weight as a float number
height = float (input("enter height cm:")) # asks user to input height as a float number 


#weight in kg
#height in cm
heightcmtom = (height/100)
#BMI = weight / height in m2
BMI= weight / (heightcmtom **2)
print("your BMI is", BMI) # output string text and BMI result
