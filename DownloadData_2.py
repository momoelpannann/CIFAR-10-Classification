import torchvision
import torchvision.transforms as transforms
import torch

# Download CIFAR-10 dataset
trainset = torchvision.datasets.CIFAR10(
    root='./Data/RawData', train=True, download=True)
testset = torchvision.datasets.CIFAR10(
    root='./Data/RawData', train=False, download=True)
print("CIFAR-10 dataset has been downloaded.")

# Define transformations to load the images
transform = transforms.Compose([
    transforms.ToTensor(),
])

# Load CIFAR-10 dataset (training set)
trainset = torchvision.datasets.CIFAR10(
    root='./Data/RawData/', train=True, download=False, transform=transform)


# Check the total number of images in the training dataset
total_images = len(trainset)
print(f'Total images in the training dataset: {total_images}')

# Load one batch of images to verify initial the shape and the # of classes
batch_size = 100
trainloader = torch.utils.data.DataLoader(
    trainset, batch_size=batch_size, shuffle=False)
# Get one batch of images
images, labels = next(iter(trainloader))

# Check the number of images in the batch
batch_size_loaded = images.shape[0]
image_shape = images.shape[1:]  # (3, 32, 32)
print(f'Number of images in the batch: {batch_size_loaded}')
print(f'Shape of each image (channels, height, width): {image_shape}')

# Check the unique classes
classes = set(labels.numpy())
print(f'Unique classes in the batch: {classes}')