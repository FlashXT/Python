import NumPy as np
from NumPy.linalg import eigvals
def run_experiment(niter =100):
    K = 100
    results = []
    for _ in xrange(niter):
        mat = np.random.randn(K,K)
        max_eigenvalue = np.abs(eigvals(mat).max())
        results.append(max_eigenvalue)
    return results
#exit()%prun -l 7 -s cumulative run_experiment()

