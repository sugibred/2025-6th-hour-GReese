#Name:Gregg
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be given a number as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

#Code Here:

#get input for weight then on separate line get height
weight = int(input("please type weight here in (lbs):"))
height = int(input("please type height here in (in):"))


#code for bmi calculater by weight divided by the height squared and multiply by 703
BMI_score = (weight/(int(height) ** 2))*703
print(round(BMI_score, 1))


# lastly us imbedded if statements to get
# underweight: less than 18.5 BMI
# normal weight: 18.5 to 24.9 BMI
# Overweight: 25 to 29.9 BMI
# Obese: 30 or more BMI
if BMI_score < 18.5 :
    print("you are Underweight")
elif BMI_score >= 18.5 and BMI_score < 24.9 :
    print("you are normal Weight")
elif BMI_score >= 24.9 and BMI_score < 29.9 :
    print("you are Overweight")
else:
    print("you are Obese")