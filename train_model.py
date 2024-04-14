import crypten as lockness
import argparse
import torch
import pandas as pd  # or import numpy as np, depending on your data format
import torch.nn as nn
import torch.nn.functional as F

parser = argparse.ArgumentParser(description="Train a model on specified data and hyperparameters")
parser.add_argument('--data_path', type=str, required=True, help="Path to the input data file")
parser.add_argument('--model_path', type=str, required=True, help="Path to the PyTorch model file")
parser.add_argument('--output_path', type=str, required=True, help="Path to save the output results")
parser.add_argument('--epochs', type=int, default=10, help="Number of training epochs")
parser.add_argument('--learning_rate', type=float, default=0.01, help="Learning rate for the optimizer")

args = parser.parse_args()

def load_data(data_path):

    # Define source argument values for Alice and Bob
    ALICE = 0
    BOB = 1

    data_alice_enc = lockness.load_from_party('/tmp/alice_train.pth', src=ALICE)

    # We'll now set up the data for our small example below
    # For illustration purposes, we will create toy data
    # and encrypt all of it from source ALICE
    x_small = torch.rand(100, 1, 28, 28)
    y_small = torch.randint(1, (100,))

    # Transform labels into one-hot encoding
    label_eye = torch.eye(2)
    y_one_hot = label_eye[y_small]

    # Transform all data to CrypTensors
    x_train = lockness.cryptensor(x_small, src=ALICE)
    y_train = lockness.cryptensor(y_one_hot)

    return (x_train, y_train)

    # # Example: Load a CSV file into a DataFrame
    # data = pd.read_csv(data_path)
    # # Convert data to a tensor
    # data_tensor = torch.tensor(data.values, dtype=torch.float32)
    # return data_tensor

def load_model(model_path):

    #Define an example network
    class ExampleNet(nn.Module):
        def __init__(self):
            super(ExampleNet, self).__init__()
            self.conv1 = nn.Conv2d(1, 16, kernel_size=5, padding=0)
            self.fc1 = nn.Linear(16 * 12 * 12, 100)
            self.fc2 = nn.Linear(100, 2) # For binary classification, final layer needs only 2 outputs
    
        def forward(self, x):
            out = self.conv1(x)
            out = F.relu(out)
            out = F.max_pool2d(out, 2)
            out = out.view(-1, 16 * 12 * 12)
            out = self.fc1(out)
            out = F.relu(out)
            out = self.fc2(out)
            return out
        
    lockness.common.serial.register_safe_class(ExampleNet)

    model_plaintext = ExampleNet()
    dummy_input = torch.empty(1, 1, 28, 28)
    model = lockness.nn.from_pytorch(model_plaintext, dummy_input)
    model.encrypt()
    # model = torch.load(model_path)
    # model.eval()
    return model

def train_model(model, data, epochs=10, learning_rate=0.001):
    model.train() # Change to training mode
    loss = lockness.nn.MSELoss() # Choose loss functions

    x_train, y_train = data
        # Train the model: SGD on encrypted data
    for i in range(epochs):

        # forward pass
        output = model(x_train)
        loss_value = loss(output, y_train)
        
        # set gradients to zero
        model.zero_grad()

        # perform backward pass
        loss_value.backward()

        # update parameters
        model.update_parameters(learning_rate) 
        
        # examine the loss after each epoch
        print("Epoch: {0:d} Loss: {1:.4f}".format(i, loss_value.get_plain_text()))
    
    return model
    # criterion = torch.nn.MSELoss()  # Example loss function
    # optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    # for epoch in range(epochs):
    #     optimizer.zero_grad()
    #     outputs = model(data)
    #     loss = criterion(outputs, data)  # Example: using data as target itself
    #     loss.backward()
    #     optimizer.step()
    #     print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item()}')
    # return model

def save_output(model, output_path):
    torch.save(model.state_dict(), output_path)


if __name__ == "__main__":
    lockness.init()
    torch.set_num_threads(1)
    data = load_data(args.data_path)
    model = load_model(args.model_path)
    trained_model = train_model(model, data, args.epochs, args.learning_rate)
    save_output(trained_model, args.output_path)
