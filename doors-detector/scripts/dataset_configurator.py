import numpy as np

from doors_detector.dataset.dataset_deep_doors_2.dataset_creator_deep_doors_2 import DatasetCreatorDeepDoors2
from doors_detector.dataset.dataset_gibson.datasets_creator_gibson import DatasetsCreatorGibson


gibson_dataset_path = '/home/michele/myfiles/doors_dataset_labelled'
deep_doors_2_dataset_path = '/home/michele/myfiles/deep_doors_2'

COLORS = np.array([[255, 0, 0], [0, 0, 255], [0, 255, 0]], dtype=float) / np.array([[255, 255, 255], [255, 255, 255], [255, 255, 255]], dtype=float)


def get_my_doors_sets():
    datasets_creator = DatasetsCreatorGibson(gibson_dataset_path)
    datasets_creator.consider_samples_with_label(label=1)
    datasets_creator.consider_n_folders(1)
    train, test = datasets_creator.creates_dataset(train_size=0.9, test_size=0.1, split_folder=False, folder_train_ratio=0.8, use_all_samples=True)
    labels = datasets_creator.get_labels()

    return train, test, labels


def get_deep_doors_2_sets():
    dataset_creator = DatasetCreatorDeepDoors2(dataset_path=deep_doors_2_dataset_path)

    train, test = dataset_creator.creates_dataset(train_size=0.9, test_size=0.1)
    labels = dataset_creator.get_label()

    return train, test, labels