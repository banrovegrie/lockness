import crypten
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.models as models
import torch

# Initialize CrypTen
crypten.init()

# Define your transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # Resize images to fit the input dimensions of the model
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Load the CIFAR-10 dataset
dataset = datasets.CIFAR10(root="./data", train=True, download=True, transform=transform)

# Load a pre-trained model, e.g., ResNet18
model = models.resnet18(pretrained=True)

# Prepare a dummy input for model conversion
image, _ = dataset[0]  # Get the first image and its label
image = image.unsqueeze(0)  # Add batch dimension

# Encrypt the model using CrypTen
model_enc = crypten.nn.from_pytorch(model, image).encrypt()

# Example of processing a single encrypted image
image, _ = dataset[1]  # Get the first image and its label
image = image.unsqueeze(0)  # Add batch dimension

# Encrypt the image using CrypTen
image_enc = crypten.cryptensor(image)

# Perform encrypted inference
output_enc = model_enc(image_enc)

# Decrypt the output to obtain plain text predictions
output = output_enc.get_plain_text()
