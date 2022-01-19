import numpy as np
from doors_detector.dataset.dataset_deep_doors_2_labelled.datasets_creator_deep_doors_2_labelled import DatasetsCreatorDeepDoors2Labelled
from doors_detector.dataset.dataset_doors_final.datasets_creator_doors_final import DatasetsCreatorDoorsFinal

deep_doors_2_labelled_dataset_path = '/home/michele/myfiles/deep_doors_2_labelled'
final_doors_dataset_path = '/home/michele/myfiles/final_doors_dataset'


def get_deep_doors_2_labelled_sets():
    dataset_creator = DatasetsCreatorDeepDoors2Labelled(dataset_path=deep_doors_2_labelled_dataset_path)
    dataset_creator.consider_samples_with_label(label=1)
    train, test = dataset_creator.creates_dataset(train_size=0.8, test_size=0.2)
    labels = dataset_creator.get_labels()

    return train, test, labels, {0: (1, 0, 0), 1: (0, 0, 1), 2: (0, 1, 0)}


def get_final_doors_dataset(experiment: int, folder_name: str, train_size: float = 0.1, use_negatives: bool = False):
    dataset_creator = DatasetsCreatorDoorsFinal(dataset_path=final_doors_dataset_path)
    dataset_creator.set_experiment_number(experiment=experiment, folder_name=folder_name)
    dataset_creator.use_negatives(use_negatives=use_negatives)
    train, test = dataset_creator.create_datasets(train_size=train_size)
    labels = dataset_creator.get_labels()

    return train, test, labels, np.array([[1, 0, 0], [0, 1, 0]], dtype=float)