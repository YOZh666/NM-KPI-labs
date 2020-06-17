from scipy.optimize import minimize
from random import uniform
from math import sqrt



# функція відповідно до мого варіанту
def my_variant(x_y):
    x, y = x_y[0], x_y[1]
    return x**2 + (y-6)**2 - 60*x + 5


def grad():
    '''використання градієнтного методу'''
    acc = 0.01
    step = 1
    def dx(x):
        '''похідна по x'''
        return 2*x-60
    def dy(y):
        '''похідна по y'''
        return 2*y-12

    #Знаходження похибки
    def eps(x,y):
        return dx(x)**2 + dy(y)**2

    #знаходимо значення наступної точки
    def new_point(x_curr,y_curr,h):
        x = x_curr+h*(-dx(x_curr))#від'ємна похідна
        y = y_curr+h*(-dy(y_curr))#від'ємна похідна
        return [x,y]

    #знаходимо початкові значення відповідно до варіанту
    x_new, y_new = new_point(32,3,step)
    while eps(x_new, y_new) > acc:
        while my_variant(new_point(x_new,y_new,step)) >= my_variant([x_new,y_new]):
            step /= 2
        x_new, y_new = new_point(x_new,y_new,step)
    return x_new,y_new

def adapt():
    '''використання адаптивного методу'''
    acc = 0.1
    step = 1
    counts = 5
    x_0,y_0 = 32, 3
    while 1:
        for i in range(counts):
            x_r,y_r = uniform(-counts,counts), uniform(-counts,counts)
            length = sqrt(x_r**2+y_r**2)
            x_last,y_last = x_r/length, y_r/length
            x,y = x_0 + step*x_last, y_0 + step*y_last
            if my_variant([x,y]) < my_variant([x_0, y_0]):
                x_0, y_0 = x,y
                step*=2
                break
        else:
            step/=2
        if step<acc:
            return x,y


    
# виводимо значення градієнтного методу
print("Gradient method: ", grad())
# виводимо значення адаптивного методу
print("Adaptive method: ", adapt())

#виводимо значення вбудованого методу
print("Built-in method: ", minimize(my_variant, [32,3]).x)
