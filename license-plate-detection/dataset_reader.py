import os
from typing import List, Tuple
import glob

class DatasetGateway(object):
    def __init__(self, db_path: str):
        self.db_path = db_path
        pass

    @staticmethod
    def get_label(self, path):
        pass

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
                    label_path = os.path.join(self.db_path, basename+".txt")
                    image_path = os.path.join(self.db_path, basename+".png")
                    data.append(image_path)
                    labels.append(label_path)

        return data, labels


dataset_gateway = DatasetGateway(r"D:\UFPR-ALPR dataset\testing")
data, labels = dataset_gateway.get_all_paths()
labels = [DatasetGateway.get_label(path) for path in labels]