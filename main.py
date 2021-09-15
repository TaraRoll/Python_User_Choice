#WRITE A PROGRAM IN PYTHON TO COMPUTE AREA AND PERIMETER OF DIFFERENT SHAPES USING USER CHOICE;(SQUARE,RECTANGLE,CIRCLE AND TRIANGLE)
print("SELECT YOUR OPTION\n")
print("1: Square Area and Perimeter\n2: Rectangle Area and Perimeter\n3: Circle Area and Perimeter\n4: Triangle Area and Perimeter")
a = int(input("Enter Choice:"))
if(a==1):
  l = int(input("Enter length:"))
  w = int(input("Enter width:"))
  print("Area is: ",l*w,"Perimeter: is ",2*w+2*l)
elif(a==2):
  l = int(input("Enter length:"))
  w = int(input("Enter width:"))
  print("Area is: ",l*w,"Perimeter: is ",2*w+2*l)
elif(a==3):
  r = int(input("Enter radius:"))
  print("Area is ",3.14*(r**2),"Perimeter is ",3.14*2*r)
elif(a==4):
  b = int(input("Enter base length:"))
  h = int(input("Enter height:"))
  s2 = int(input("Enter side 2:"))
  s3 = int(input("Enter side 3:"))
  print("Area is ", b*h*0.5,"Perimeter is ", b+s2+s3)
else:
  print("This is invalid.")

