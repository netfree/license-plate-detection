import argparse
import matplotlib.pyplot as plt
from data_generator import DataGenerator

parser = argparse.ArgumentParser(description=r"data_generator_test.py -dataset [dataset_path]")
parser.add_argument("-dataset", "--dataset", help="Path to the dataset")
args = parser.parse_args()

label_names = None # TODO the label names for your dataset (for example, in cifar-10 this would be ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog','horse', 'ship', 'truck'])

db_dir = args.dataset
train_generator = DataGenerator(db_dir, batch_size=32, input_shape=None, num_classes=10, shuffle=True)
train_generator.show_imgs(5)
# batch_x, batch_y = train_generator[0]
#
# fig, axes = plt.subplots(nrows=1, ncols=6, figsize=[16, 9])
# for i in range(len(axes)):
#     axes[i].set_title(batch_y[i])
#     axes[i].imshow(batch_x[i])
# plt.show()
