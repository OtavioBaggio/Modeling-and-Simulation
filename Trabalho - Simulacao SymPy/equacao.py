from sympy import symbols, Function, Eq, dsolve, Derivative

# Definindo variável de tempo e função
t = symbols('t')
y = Function('y')(t)
k = symbols('k')

# Equação diferencial: dy/dt = k*y
ode = Eq(Derivative(y, t), k*y)

# Resolver a EDO
solucao = dsolve(ode)
print("Solução da EDO:", solucao)
