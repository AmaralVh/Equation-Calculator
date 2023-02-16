import solutions as sl


print('\n-----WELCOME TO THE EQUATIONS CALCULATOR!-----\n\n')
print('Please, set the details of the equation:\n')

coef = []

degree = int(input('Set the degree of the equation:'))

# Get the coefficients of the equation in the general formula:
for i in range(degree+1):
    print(f'Coefficient {i+1}: ')
    coef.append(float(input()))
    
if degree == 1:
    solution = sl.linearEquationSolution(coef)
elif degree == 2:
    solution = sl.quadraticEquationSolution(coef)
else:
    solution = sl.highDegreeSolution(coef, degree)
    

print(f'The solution of the equation in the real numbers is {solution}')