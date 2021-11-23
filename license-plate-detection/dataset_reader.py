import os
from typing import List, Tuple
import glob

class DatasetGateway(object):
    def __init__(self, db_path: str):
        self.db_path = db_path
        pass

    @staticmethod
    def get_label(path) -> Tuple[int, int, int, int]:
        """
        Reads the position of the license plate from the label file
        :param path: label file path
        :return: [int, int, int, int]
        """
        with open(path) as f:
            for line_number, line in enumerate(f):
                if line_number == 7:
                    line = line.strip(" \n")
                    lhs, rhs = line.split(":")
                    coords = rhs.split(" ")[1:]
                    coords = [int(x) for x in coords]
        return coords

    def get_image(self):
        pass

    def get_all_paths(self):
        """

        :return: List[image_path, data_path]
        """
        data = []
        labels = []

        for image_folder in os.listdir(self.db_path):
            for file in os.listdir(os.path.join(self.db_path, image_folder)):
                if file.endswith(".png"):
                    basename = file[:-4]
                    label_path = os.path.join(os.path.join(self.db_path, image_folder), basename + ".txt")
                    image_path = os.path.join(os.path.join(self.db_path, image_folder), basename + ".png")
                    data.append(image_path)
                    labels.append(label_path)

        return data, labels


dataset_gateway = DatasetGateway(r"D:\UFPR-ALPR dataset\testing")
data, labels = dataset_gateway.get_all_paths()
labels = [DatasetGateway.get_label(path) for path in labels]
print(len(labels))