
print("Medical Patient Assessment")
def calculate_bmi(w, h) :
     bmi = w / h**2
     return bmi
def bmi_category(bmi) :
     if bmi < 18.5 :
      return("underweight")
     elif  18.5 <= bmi <= 24.99 :
      return ("normal")
     elif 25<= bmi <= 29.99 :
      return("overweight")
     elif bmi >=30 :
      return("obese")
choice = "yes"
tot_patiant = 0
while choice == "yes"  :
  n = input("enter pataint name : ")
  age = input("enter pataint age : ")
  wt = input("enter pataint weight (kg) :")
  ht = input("enter pataint height (m) :")
  w = float(wt)
  h = float(ht)
  a = int(age)
  bmi = calculate_bmi(w, h)
  category = bmi_category(bmi)
  print("BMI:" , bmi)
  print(category)
  tot_patiant = tot_patiant +1
  choice = input("do yo want to enter anthor patiant? yes , no :")
  if choice == "no" :
      break
  print("total patients entered:" , tot_patiant)

