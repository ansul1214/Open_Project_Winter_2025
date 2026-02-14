import torch
import numpy as np
import itertools

# 2-qubit Pauli matrices
I = torch.tensor([[1,0],[0,1]], dtype=torch.cfloat)
X = torch.tensor([[0,1],[1,0]], dtype=torch.cfloat)
Y = torch.tensor([[0,-1j],[1j,0]], dtype=torch.cfloat)
Z = torch.tensor([[1,0],[0,-1]], dtype=torch.cfloat)

paulis = {'X':X, 'Y':Y, 'Z':Z}

def kron(a,b):
    return torch.kron(a,b)

def random_density_matrix(dim=4):
    A = torch.randn(dim, dim, dtype=torch.cfloat)
    rho = A @ A.conj().T
    rho = rho / torch.trace(rho)
    return rho

def classical_shadow_2qubit(rho, shots=30):
    features = []

    bases = list(itertools.product(['X','Y','Z'], repeat=2))

    for _ in range(shots):
        b = bases[np.random.randint(len(bases))]
        P = kron(paulis[b[0]], paulis[b[1]])

        expectation = torch.real(torch.trace(rho @ P))
        outcome = 1 if expectation > 0 else -1

        basis_encoding = [
            int(b[0]=='X'), int(b[0]=='Y'), int(b[0]=='Z'),
            int(b[1]=='X'), int(b[1]=='Y'), int(b[1]=='Z')
        ]

        features.append(basis_encoding + [outcome])

    return torch.tensor(features, dtype=torch.float32)

def generate_dataset(n_samples=1500, shots=30):
    X, Y = [], []

    for _ in range(n_samples):
        rho = random_density_matrix()
        shadow = classical_shadow_2qubit(rho, shots)

        X.append(shadow)
        Y.append(rho)

    return torch.stack(X), torch.stack(Y)
