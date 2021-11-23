import os
from typing import Tuple
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


class DataGenerator(tf.keras.utils.Sequence):
    def __init__(self, db_dir, batch_size, input_shape, num_classes, shuffle=True):
        self.input_shape = input_shape
        self.batch_size = batch_size
        self.num_classes = num_classes
        self.shuffle = shuffle
        # load the data from the root directory
        self.data, self.labels = self.get_data(db_dir)
        self.indices = np.arange(len(self.data))
        self.on_epoch_end()

    def get_data(self, root_dir):
        """"
        Loads the paths to the images and their corresponding labels from the database directory
        """
        self.data = []  # array[images]
        self.labels = []  # array[coords]

        for image_folder in os.listdir(root_dir):
            for file in os.listdir(os.path.join(root_dir, image_folder)):
                if file.endswith(".png"):
                    basename = file[:-4]
                    label_path = os.path.join(root_dir, image_folder, basename + ".txt")
                    image_path = os.path.join(root_dir, image_folder, basename + ".png")
                    self.data.append(image_path)
                    self.labels.append(label_path)

        return self.data, self.labels

    def __len__(self):
        """
        Returns the number of batches per epoch: the total size of the dataset divided by the batch size
        """
        return int(np.floor(len(self.data) / self.batch_size))

    def __getitem__(self, index):
        """"
        Generates a batch of data
        """
        batch_indices = self.indices[index * self.batch_size: (index + 1) * self.batch_size]
        batch_x = [plt.imread(self.data[idx]) for idx in batch_indices]  # TODO load the image from batch_indices
        batch_y = [self.get_label(self.labels[idx]) for idx in
                   batch_indices]  # TODO load the corresponding labels of the images you loaded
        # optionally you can use: batch_y = tf.keras.utils.to_categorical(batch_y, num_classes=self.num_classes)
        return batch_x, batch_y

    def on_epoch_end(self):
        """"
        Called at the end of each epoch
        """
        # if required, shuffle your data after each epoch
        self.indices = np.arange(len(self.data))
        if self.shuffle:
            # TODO shuffle data
            # you might find np.random.shuffle useful here
            np.random.shuffle(self.indices)

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

    def show_imgs(self, limit):
        '''
        Show the images with a bounding box on the license plate based on the label coordinates
        :param limit: number of images to show
        '''
        for idx in range(limit):
            fig = plt.figure()
            ax = fig.gca()
            ax.imshow(plt.imread(self.data[idx]))
            startX = int(self.get_label(self.labels[idx])[0])
            startY = int(self.get_label(self.labels[idx])[1])
            width = int(self.get_label(self.labels[idx])[2])
            height = int(self.get_label(self.labels[idx])[3])

            ax.add_patch(Rectangle((startX, startY), width, height, color='red', fill=False, linewidth=1))
            plt.show()
