import torch
import numpy as np
import scipy.linalg as la

def fidelity(rho, sigma):
    rho_np = rho.detach().numpy()
    sigma_np = sigma.detach().numpy()

    sqrt_rho = la.sqrtm(rho_np)
    product = sqrt_rho @ sigma_np @ sqrt_rho
    return np.real(np.trace(la.sqrtm(product)))**2

def trace_distance(rho, sigma):
    diff = rho - sigma
    eigvals = torch.linalg.eigvals(diff)
    return 0.5 * torch.sum(torch.abs(eigvals)).real.item()
import torch
import numpy as np
import scipy.linalg as la

def fidelity(rho, sigma):
    rho_np = rho.detach().numpy()
    sigma_np = sigma.detach().numpy()

    sqrt_rho = la.sqrtm(rho_np)
    product = sqrt_rho @ sigma_np @ sqrt_rho
    return np.real(np.trace(la.sqrtm(product)))**2

def trace_distance(rho, sigma):
    diff = rho - sigma
    eigvals = torch.linalg.eigvals(diff)
    return 0.5 * torch.sum(torch.abs(eigvals)).real.item()
