weight=int(input("enter the weight:"))
height=float(input("enter the height:"))
BMI=weight/(height*height)
print(BMI)
if BMI>0:
  if(BMI<18.5):
    print("underweight")
  elif(BMI<=24.9 or BMI>=18.5):
    print("normal weight")
  elif(BMI>24.9 or BMI<30):
    print("overweight")
  else:
      print("obesity")
