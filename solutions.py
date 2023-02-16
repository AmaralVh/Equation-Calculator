import math    


def findDivisors(num):
    aux = int(num / 2)
    if aux < 0:
        aux *= -1
    
    div = []    
    for i in range(1, aux + 1):
        if num % i == 0:
            div.append(i)
            div.append(-i)
    div.append(int(num))
    div.append(int(-num))
    
    return div


def findOneRoot(div1, div2, degree, coef):
    for i in range(0, len(div1), 2):
        for j in range(len(div2)):
            candidate = div1[i] / div2[j]
            total = 0
            exp = degree
            for k in range(degree+1):
                total += coef[k] * (candidate ** exp)
                exp -= 1
            if total == 0:
                return candidate
            
            
def briotRuffini(degree, roots, coef):
    i = 0
    new_coef = []
    new_coef.append(coef[0])
    rest = coef[0]
    for j in range(degree):
        rest = (roots[i] * rest) + coef[j+1]
        new_coef.append(rest)
    return new_coef
    
    
def linearEquationSolution(coef):
    solution = (-1 * coef[1]) / coef[0]
    return solution


def quadraticEquationSolution(coef):
    delta = (coef[1] ** 2) - (4 * coef[0] * coef[2])
    print(f'Delta = {delta}')
    
    if delta < 0:
        return []
    elif delta == 0:
        solution = (-1 * coef[1]) / (2 * coef[0])
        return solution
    else:
        solution = []
        solution.append(( (-1 * coef[1]) + math.sqrt(delta) ) / (2 * coef[0]))
        solution.append(( (-1 * coef[1]) - math.sqrt(delta) ) / (2 * coef[0]))
        return solution

    
def highDegreeSolution(coef, degree):
    roots = []
    
    div1 = findDivisors(coef[-1])
    div2 = findDivisors(coef[0])
    
    print(f'Div1: {div1}')
    print(f'Div2: {div2}')
    
    # Find the first root:
    roots.append(findOneRoot(div1, div2, degree, coef))
    
    print(f'Roots: {roots}')
    
    #Briot-Ruffini
    new_coef = briotRuffini(degree, roots, coef)
    
    print(f'New coefficients: {new_coef}')
    
    roots = roots + quadraticEquationSolution(new_coef)
    return roots