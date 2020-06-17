from scipy.integrate import odeint #импортируем функцию для точных значений
from numpy import array
from numpy import linspace
from math import sqrt


def dx_dt(t,x,y):
    '''первая производная по х (dx/dt)'''
    return 5 * t + x - y + 6

def dy_dt(x,y):
    '''первая производная по y (dy/dt)'''
    return -x + 5 * y

def for_built(t, mas):
  return array([5*t+mas[0]-mas[1]+6, -mas[0]+5*mas[1]])

def euler_metod(a,b,h):
    '''решение системы уравнений методом Эйлера'''

    x, y = 0.0, 0.0 #начальные условия
    answ = [(x,y)]
    a+=h
    while a <= b: #находим х и у по формулам
        x += h * dx_dt(a, x, y) 
        y += h * dy_dt(x, y)
        answ.append((x, y)) 
        a += h
    return answ
        

def runge_cutta_metod(a,b,h):
    '''решение системы уравнений методом Рунге-Кутта'''
    x, y = 0.0, 0.0 #начальные условия
    answ = [(x,y)]
    k1 = k2 = k3 = k4 = 0 #эта для х
    q1 = q2 = q3 = q4 = 0 #эта для у
    a+=h
    while a <= b:
       k1 = h * dx_dt(a, x, y) #находим все эты и подставляем в формулу
       q1 = h * dy_dt(x, y)
       
       k2 = h * dx_dt(a, x + h/2, y + k1/2)
       q2 = h * dy_dt(x + h/2, y + q1/2)

       k3 = h * dx_dt(a, x + h/2, y + k2/2)
       q3 = h * dy_dt(x + h/2, y + q2/2)

       k4 = h * dx_dt(a, x + h, y + k3)
       q4 = h * dy_dt(x + h, y + q3)

       x += 1/6 * (k1 + 2*k2 + 2*k3 + k4)
       y += 1/6 * (q1 + 2*q2 + 2*q3 + q4)
       answ.append((x,y))
       a += h
    return answ

def accuracy(mas1,mas2):
  answ = []
  for i in range(len(mas1)):
    answ.append((mas1[i][0] - mas2[i*2][0])**2)
    answ.append((mas1[i][1] - mas2[i*2][1])**2)
  return sqrt(1/(len(mas1) - 1)) * (sum(answ))


def final_func(what_m, a,b):
  e = 0.1
  h = 0.25
  new = what_m(a,b,h)
  last = what_m(a,b,h*2)
  while (accuracy(last,new) > e):
    h /= 2
    last = new
    new = what_m(a,b,h)
  return h,new


if __name__ == "__main__":
    print("Method from Python Library:")
    print(odeint(for_built, array([0, 0]), linspace(0, 1, 10), tfirst=True))
    h, answ = final_func(euler_metod, 0, 1)
    print("\nEuler's method: h = ", h)
    print("*    t0    |    dx    │    dy    *")
    print(''.join("*" for i in range(34)))
    for i in range(0,len(answ),100):
        print("{:^8.5}│{:^8.5}│{:^8.5}".format(h * i, answ[i][0], answ[i][1]))
    else:
        print("{:^8.5}│{:^8.5}│{:^8.5}".format("Last val: ", answ[-1][0], answ[-1][1]))
    h, answ = final_func(runge_cutta_metod, 0, 1)
    print("\nRunge-Kutta's method: h = ", h)
    print("*    t0    |    dx    │    dy    *")
    print(''.join("*" for i in range(34)))
    for i in range(0,len(answ),100):
        print("{:^8.5}│{:^8.5}│{:^8.5}".format(h * i, answ[i][0], answ[i][1]))
    else:
        print("{:^8.5}│{:^8.5}│{:^8.5}".format("Last val: ", answ[-1][0], answ[-1][1]))


