 #імпортуємл PuLP
from pulp import *
 
# створюємо нову задачу лінійного програмування з мінімізацією 
prob = LpProblem("FarmerProblem", LpMinimize)
 
# змінні оптимізації, цілі
x1 = LpVariable("x1", 0, 10, 'Integer')
x2 = LpVariable("x2", 0, 10, 'Integer')

 
# Цільова функція
prob += 14*x1 + 12*x2, "obj"
 
# Межі
prob += 35*x1 + 24*x2  >= 107, "c1"
 
# запускаємо вирішення
prob.solve()
 
# статус задачі
print( "Status:", LpStatus[prob.status])
 
# Виводимо отримані оптимальні значення змінних
for v in prob.variables():
  print (v.name, "=", v.varValue)
 
# Виводимо оптимальне значення цільової функції
print ("objective = %s$" % value(prob.objective))
