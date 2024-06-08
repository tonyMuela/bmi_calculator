height = input("How tall are you in inches? ")
weight = input("How much do you weigh in lbs? ")

float_height = float(height)
float_weight = float(weight)

metric_height = float_height / 39.37
metric_weight = float_weight / 2.205


bmi = metric_weight / metric_height ** 2

bmi_round =(round(bmi, 1))

if bmi < 18.5:
  print(f"Your BMI is {bmi_round}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi_round}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi_round}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi_round}, you are obese.")
else:
  print(f"Your BMI is {bmi_round}, you are clinically obese.")
