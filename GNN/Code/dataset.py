# -*- coding: utf-8 -*-
'''
This is a walkthrough for creating a Dataset using PyTorch Geometric.
PyG datasets are divided into `InMemoryDataset` and `Dataset`
 - `InMemoryDataset` is used when the whole dataset could fit into the RAM
 - `Dataset` is used otherwise
There are a few methods that need to be implemented when creating a dataset:
 - `raw_file_names()`: 
 - `processed_file_names()`: 
 - `download()`: Downloads raw data into `raw_dir` (Could be `pass`ed or skip overwritting)
 - `processed()`: Processes raw data and saves it into the `processed_dir`
 - `len()`: Returns number of examples in dataset (Dataset only)
 - `get()`: Implements the logic of loading a single graph (Dataset only)

Could directly pass in a regular python list with `torch_geometric.data.Data` objects and pass into `torch_geometric.data.DataLoader`.
'''


from torch_geometric import InMemoryDataset, Dataset
import torch
import os

class RandomDataset(Dataset):
    def __init__(self, root, transform=None, pre_transform=None):
        super(RandomDataset, self).__init__(root, transform, pre_transform)
        self.data, self.slices = torch.load(self.processed_paths[0])

    @property
    def raw_file_names(self):
        return ['path_to_file']

    @property
    def processed_file_names(self):
        return ['./data/processed.pt']

    def download(self):
        # Download to self.raw_dir
        pass

    def process(self):
        i = 0
        for raw_path in self.raw_paths:
            # Read data from `raw_path` into `Data` list
            data = Data(...)

            if self.pre_filter is not None and not self.pre_filter(data):
                continue

            if self.pre_transform is not None:
                data = self.pre_transform(data)

            torch.save(data, os.path.join(self.processed_dir, f'data_{i}.pt'))
            i += 1

    def len(self):
        return len(self.processed_file_names)

    def get(self, idx):
        data = torch.load(os.path.join(self.processed_dir, f'data_{idx}.pt'))
        return