import matplotlib.pyplot as plt

db_dir = r"D:\UFPR-ALPR dataset"

img = plt.imread(r"D:\UFPR-ALPR dataset\training\track0002\track0002[01].png")


# label_names = None # TODO the label names for your dataset (for example, in cifar-10 this would be ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog','horse', 'ship', 'truck'])
#
# train_generator = DataGenerator(db_dir, batch_size=32, input_shape=None, num_classes=10, shuffle=True)
#
# batch_x, batch_y = train_generator[0]

# fig, axes = plt.subplots(nrows=1, ncols=6, figsize=[16, 9])
# for i in range(len(axes)):
#     axes[i].set_title(label_names[batch_y[i]])
#     axes[i].imshow(batch_x[i])
# plt.show()
