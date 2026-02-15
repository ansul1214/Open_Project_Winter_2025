import torch
import time
from torch.utils.data import DataLoader, TensorDataset

from dataset import generate_dataset
from model import SimpleGNN
from metrics import fidelity, trace_distance

device = "cpu"

X, Y = generate_dataset(n_samples=5000, shots=50)
X, Y = X.to(device), Y.to(device)

dataset = TensorDataset(X, Y)
loader = DataLoader(dataset, batch_size=64, shuffle=True)

model = SimpleGNN(hidden=128).to(device)

optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=50, gamma=0.5)
loss_fn = torch.nn.MSELoss()

epochs = 150

for epoch in range(epochs):
    model.train()
    total_loss = 0

    for xb, yb in loader:
        optimizer.zero_grad()
        pred = model(xb)
        loss = loss_fn(pred.real, yb.real)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    scheduler.step()
    print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(loader)}")

torch.save(model.state_dict(), "../outputs/model.pt")

model.eval()
test_X, test_Y = generate_dataset(n_samples=300, shots=50)

fids, tds = [], []

with torch.no_grad():
    for i in range(len(test_X)):
        pred = model(test_X[i].unsqueeze(0))
        fids.append(fidelity(pred[0], test_Y[i]))
        tds.append(trace_distance(pred[0], test_Y[i]))

mean_fid = sum(fids) / len(fids)
mean_td = sum(tds) / len(tds)

start = time.time()
_ = model(test_X[0].unsqueeze(0))
latency = time.time() - start

print("\nMean Fidelity:", mean_fid)
print("Mean Trace Distance:", mean_td)
print("Inference Latency:", latency)

with open("../outputs/metrics.txt", "w") as f:
    f.write(f"Mean Fidelity: {mean_fid}\n")
    f.write(f"Mean Trace Distance: {mean_td}\n")
    f.write(f"Inference Latency: {latency}\n")
