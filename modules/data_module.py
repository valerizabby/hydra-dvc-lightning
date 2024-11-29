from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from torchvision.datasets import MNIST
from pytorch_lightning import LightningDataModule
from meanvector import MeanVector
import numpy as np


class CustomDataset(Dataset):
    def __init__(self, data_dir, train=True, transform=None, download=False):
        self.data = MNIST(root=data_dir, train=train, download=True)
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        image, label = self.data[idx]
        if self.transform:
            image = self.transform(image)

        # вычисляем среднее значение вектора с помощью биндинга из прошлой лабы
        vector_size = 12
        vector_1 = np.random.rand(vector_size)
        mean_value = MeanVector.meanVector(vector_1)

        return image, label


class CustomDataModule(LightningDataModule):
    def __init__(self, data_dir, batch_size):
        super().__init__()
        self.val_dataset = None
        self.train_dataset = None
        self.data_dir = data_dir
        self.batch_size = batch_size
        self.transform = transforms.Compose([
            transforms.ToTensor(),
        ])

    def setup(self, stage=None):
        self.train_dataset = CustomDataset(self.data_dir, train=True, transform=self.transform, download=True)
        self.val_dataset = CustomDataset(self.data_dir, train=False, transform=self.transform, download=True)

    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=True)

    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.batch_size)