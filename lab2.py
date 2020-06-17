import random
import math
from scipy.optimize import fminbound

def my_variant(x):
	"""My numbers in student's ticket"""
	return x**2+60*x+5

def bisection_meth(a_b,eps):
	""" Finding xmin and f_min using bisection method """
	a,b = a_b[0], a_b[1]
	while abs(b-a)>eps:
		x_m = (a+b)/2
		x_1 = a + (b-a)/4
		x_2 = b - (b-a)/4
		if my_variant(x_m) >= my_variant(x_2):
			a = x_m
		elif my_variant(x_m) >= my_variant(x_1):
			b = x_m
		else:
			a,b = x_1, x_2
	return x_m, my_variant(x_m)

def random_search(a_b):
	""" Finding x_min and f_min using randomsearch method """
	a,b = a_b[0], a_b[1]
	array = [random.uniform(a,b) for i in range(101)]
	array_with_func = map(my_variant,array)
	return min(zip(array,array_with_func))

if __name__ == "__main__":
	interval = [-32,31]
	eps = 0.01
	print("My interval: [-32;31]")
	print("My function: x^2 + 60x + 5")
	print("Built-in method(SciPy): x_min = {}, f_min = {}".format(fminbound(my_variant, -32, 31), my_variant(fminbound(my_variant, -32, 31))))
	print("Bisection method: xmin = {}, fmin = {}".format(*bisection_meth(interval, eps)))
	print("Random-search method: xmin = {}, fmin = {}".format(*random_search(interval)))
