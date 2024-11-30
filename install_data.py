from torchvision.datasets import MNIST

if __name__ == '__main__':
    MNIST(root='./data', train=True, download=True)
    MNIST(root='./data', train=False, download=True)