import numpy as np

def newton_raphson(f, df, x0, tol=1e-7, max_iter=100):
    x = np.array(x0, dtype=float)
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        try:
            dx = np.linalg.solve(dfx, -fx)
        except np.linalg.LinAlgError:
            print(f"Jacobian singular or not square at iteration {i+1}")
            return None
        x_new = x + dx
        if np.linalg.norm(dx) < tol:
            print(f"Converged at iteration {i+1}")
            return x_new
        x = x_new
    print("Did not converge in specified number of iterations.")
    return x
