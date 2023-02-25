import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# hyperparameters of the model
learning_rate = 0.001
num_epochs = 1000

# model architecture
class ClarificationModel(nn.Module):
    def __init__(self):
        super(ClarificationModel, self).__init__()
        self.fc1 = nn.Linear(3, 5)
        self.fc2 = nn.Linear(5, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.fc1(x)
        x = self.sigmoid(x)
        x = self.fc2(x)
        x = self.sigmoid(x)
        return x

# to training the data
def generate_data(num_samples):
    X = np.random.randint(0, 256, size=(num_samples, 3))
    y = np.zeros((num_samples, 1))
    for i in range(num_samples):
        if X[i, 0] > X[i, 1] and X[i, 0] > X[i, 2]:
            y[i] = 1
    return X, y

# train using binary cross entropy loss and Adam optimizer
model = ClarificationModel()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

X, y = generate_data(100000)

for epoch in range(num_epochs):
    optimizer.zero_grad()
    inputs = torch.from_numpy(X).float()
    labels = torch.from_numpy(y).float()
    outputs = model(inputs / 255.0)
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()
    if epoch % 100 == 0:
        print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch+1, num_epochs, loss.item()))

# to use the model
def predict_color(model, color):
    inputs = torch.from_numpy(np.array(color)).float()
    output = model(inputs / 255.0)
    if output.item() > 0.5:
        return 'Some tone of orange'
    else:
        return 'Not some tone of orange'

# run some classification tests
print(predict_color(model, [255, 128, 0]))  # Some tone of orange
print(predict_color(model, [128, 255, 0]))  # Not some tone of orange
print(predict_color(model, [223, 118, 14]))  # Some tone of orange

# export the model to ONNX
input_names = ["input"]
output_names = ["output"]
dummy_input = torch.randn(1, 3)
torch.onnx.export(model, dummy_input, "classifier.onnx", input_names=input_names, output_names=output_names)

