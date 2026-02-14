import torch
import torch.nn as nn

class SimpleGNN(nn.Module):
    def __init__(self, node_dim=7, hidden=128, dim=4):
        super().__init__()

        # Deeper node embedding
        self.node_embed = nn.Sequential(
            nn.Linear(node_dim, hidden),
            nn.ReLU(),
            nn.Linear(hidden, hidden)
        )

        # Message passing layers
        self.message1 = nn.Linear(hidden, hidden)
        self.message2 = nn.Linear(hidden, hidden)

        # Update function
        self.update = nn.GRUCell(hidden, hidden)

        # Deeper readout
        self.readout = nn.Sequential(
            nn.Linear(hidden, hidden),
            nn.ReLU(),
            nn.Linear(hidden, dim*dim)
        )

        self.dim = dim

    def forward(self, x):
        # x: (batch, nodes, features)
        h = self.node_embed(x)

        # --- Message Passing Round 1 ---
        agg1 = torch.mean(torch.relu(self.message1(h)), dim=1)
        h = self.update(agg1, h.mean(dim=1))

        # --- Message Passing Round 2 ---
        agg2 = torch.mean(torch.relu(self.message2(h.unsqueeze(1))), dim=1)
        h = self.update(agg2, h)

        # Readout
        L_flat = self.readout(h)
        L = L_flat.view(-1, self.dim, self.dim)

        L = torch.tril(L)

        rho = L @ L.transpose(-2,-1).conj()

        trace = torch.diagonal(rho, dim1=-2, dim2=-1).sum(-1)
        rho = rho / trace.view(-1,1,1)

        return rho
