# módulo de python: modulo_pcs
import numpy as np
def gradiente(fun,x):
    x = x.astype(float)
    h = 1e-5
    grad = np.zeros(len(x))
    fx = fun(x)
    for i in range(len(x)):
        x1 = x.copy()
        x1[i] = x1[i] + h
        grad[i] = (fun(x1) - fx)/h
    return grad

def fun(x):
    return -x[0]*x[1]*x[2] 

x = np.array([1,2,3])
grad_X = gradiente(fun,x)

grad_X