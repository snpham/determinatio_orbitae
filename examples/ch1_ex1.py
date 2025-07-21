import numpy as np
from determinatio import newton_raphson

def calculate_rho_theta(X, t):
    x0, y0, X_dot, Y_dot, g = X

    # calculate position at time t
    x = x0 - Xs + X_dot * t
    y = y0 - Ys + Y_dot * t - g * t**2 / 2
    
    # calculate rho
    rho = np.sqrt(x**2 + y**2)
    
    # calculate theta
    theta = np.arctan2(y, x)
    
    return rho, theta

def F(x):

    deltas = []
    for t, r in zip(times, rhos_obs):
        rho, _ = calculate_rho_theta(x, t)
        deltas.append(rho-r)
    return np.array(deltas)

def dF(X):
    X0, Y0, X_dot, Y_dot, g = X
    J = []
    for t in times:
        x = X0 - Xs + X_dot * t
        y = Y0 - Ys + Y_dot * t - 0.5 * g * t**2
        rho = np.sqrt(x**2 + y**2)
        dX0    = x / rho
        dY0    = y / rho
        dXdot  = x * t / rho
        dYdot  = y * t / rho
        dg     = -y * t**2 / (2 * rho)
        J.append([dX0, dY0, dXdot, dYdot, dg])
    return np.array(J)


# define parameters

# fixed stations
Xs = 1.0
Ys = 1.0

# unitless initial conditions
x0 = 1.5
y0 = 10.0
X_dot = 2.2
Y_dot = 0.5
g = 0.3

# times
times = [0, 1., 2., 3., 4.,]
rhos_obs = [7.0, 8.00390597, 8.94427191, 9.801147892, 10.630145813]

# for t1
# rho1, theta1 = calculate_rho_theta(X0, Y0, Xs, Ys, X_dot, Y_dot, t1, g)
# for t2
# rho2, theta2 = calculate_rho_theta(X0, Y0, Xs, Ys, X_dot, Y_dot, t2, g)

# print("rho1 =", rho1)
# print("theta1 =", theta1)
# print("rho2 =", rho2)
# print("theta2 =", theta2)

X0 = [x0, y0, X_dot, Y_dot, g]
root = newton_raphson.newton_raphson(F, dF, X0, tol=1e-7, max_iter=100)
print(root)
