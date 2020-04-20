height = float(input('What is your height?(m) '))
weight = float(input('What is your weight?(Kg) '))
bmi = weight / (height ** 2)  # Body Mass Index
print(f'Your height is {height:.2f}m and your weight is {weight:.1f}kg, so your BMI is \33[1;30m{bmi:.1f}\33[m.')
if bmi < 18.5:
    print('Take care! You are \33[1;4;32munderweight\33[m!')
elif bmi < 25:
    print('Congratulations! You are at the \33[1;4;34mideal weight\33[m!')
elif bmi < 30:
    print('Alert!! You are \33[1;4;33moverweight\33[m!')
elif bmi < 40:
    print('Be careful!! You are in \33[1;4;35mobesity\33[m!')
else:
    print('Look for a doctor!! You are in \33[1;4;31mmorbid obesity\33[m!')