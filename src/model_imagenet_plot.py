from matplotlib import pyplot as plt
import numpy as np


fig, axs = plt.subplots(2, 1)
accuracy_plt = axs[0]
loss_plt = axs[1]

# epoche di riferimento per Model IMAGENET
epochs = np.array([0, 25, 50, 75, 100, 125, 150, 175, 200,
                   225, 250, 275, 300, 325, 350, 375])

# Accuracy di train e test
accuracy_train = np.array([0.282, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                          1, 1, 1, 1, 1, 1])
accuracy_test = np.array([0.5304, 0.8159, 0.8638, 0.8507, 0.8623, 0.8565,
                          0.8623, 0.8638, 0.8638, 0.8710, 0.8725,
                          0.8652, 0.8638, 0.8638, 0.8667, 0.8609])

# plotting dell'accuracy
accuracy_plt.plot(epochs, accuracy_train, label='train')
accuracy_plt.plot(epochs, accuracy_test, label='test')
accuracy_plt.set_xlabel('epochs')
accuracy_plt.set_ylabel('accuracy')
accuracy_plt.legend()

# Loss di traing e test
loss_train = np.array([3.1998, 9.5772E-4, 1.5434E-5, 1.3239E-7,
                       3.8864E-8, 3.5993E-8, 4.0553E-8, 4.2024E-8,
                       3.8945E-8, 3.7161E-8, 4.0969E-8, 4.3402E-8,
                       4.1513E-8, 4.7972E-8, 4.8109E-8, 5.0497E-8])
loss_test = np.array([2.4001, 0.8852, 0.6024, 0.5549, 0.5576,
                      0.5420, 0.5448, 0.5391, 0.5360, 0.5382,
                      0.5397, 0.5427, 0.5466, 0.5530, 0.5535,
                      0.5634])

# plotting della loss
loss_plt.plot(epochs, loss_train, label='train')
loss_plt.plot(epochs, loss_test, label='test')
loss_plt.set_xlabel('epochs')
loss_plt.set_ylabel('loss')
loss_plt.legend()

# plot datas
plt.show()
