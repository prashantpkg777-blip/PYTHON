m1=int(input("Enter your marks of subject 1:"))
m2=int(input("Enter your marks of subject 2:"))
m3=int(input("Enter your marks of subject 3:"))

total_percent = (m1+m2+m3)/3

if(total_percent>=40 and m1>=33 and m2>=33 and m3>=33):
  print("Your percentage is ",total_percent)
  print("Congrats! You passed the exam.")
else:
  print("Your percentage is ",total_percent)
  print("Failed! Better luck next time.")
    