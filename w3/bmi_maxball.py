def bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25.0:
        return "Balance"
    if bmi < 30.0:
        return "Overweight"
    return "Obesity"

w = float(input("Weight (kg): "))
h = float(input("Height (m): "))
bmi = w / (h * h)
print("BMI =", bmi, bmi_status(bmi))

def max_ball(f, b, v):
    if f >= b:
        if f >= v:
            return "Football"
        else:
            return "Volleyball"
    else:
        if b >= v:
            return "Basketball"
        else:
            return "Volleyball"

f = int(input("Football: "))
b = int(input("Basketball: "))
v = int(input("Volleyball: "))
print("Most balls:", max_ball(f, b, v))
