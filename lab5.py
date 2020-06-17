import numpy as np
from scipy.optimize import linprog

# Values according to my task
my_task = np.array([[0.5,  0, 0],
              [1, 0.5, 0],
              [1, 1, 0.5]])


# Creating my coeficients and limitations
coefs = limitations = np.array([1, 1, 1]) 



# Finding my saddle point
def sad_p(a):
    maxmin, minmax = a.min(axis=1).max(), a.max(axis=0).min()
    print(maxmin, minmax,  minmax == maxmin)
    


# Solving my task
def solve(c, a, b):
    result = linprog(c, a, b, bounds=[(0, None)]*len(a), method='interior-point')
    return (*result.x * 1/sum(result.x), 1/sum(result.x)) 

def main():
    print("Finding my saddle point:")
    sad_p(my_task)
    print("Solving of my task:")
    tralshik, mine = solve(-(coefs), my_task, limitations), solve(coefs, -(my_task.transpose()), -(limitations))
    print("The minesweeper mixed strategy = {}, with sum {}"
          .format(tralshik[0:-1], tralshik[-1]))
    print("The mine mixed strategies = {}, with sum {}\n"
          .format(mine[0:-1], mine[-1]))


if __name__ == "__main__":
    main()
