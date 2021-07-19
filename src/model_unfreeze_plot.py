from matplotlib import pyplot as plt
import numpy as np


fig, axs = plt.subplots(2, 1)
accuracy_plt = axs[0]
loss_plt = axs[1]

# epoche di riferimento per Model VGGFace con i layers unfreezed
epochs = np.array([0, 25, 50, 75, 100, 125, 150, 175, 200])

# Accuracy di train e test
accuracy_train = np.array([0.0152, 0.0279, 0.1268, 0.2402, 0.3042,
                           0.2936, 0.3160, 0.3193, 0.3050])
accuracy_test = np.array([0.0232, 0.0174, 0.0971, 0.1377, 0.1174,
                          0.1333, 0.1304, 0.1377, 0.1304])

# plotting dell'accuracy
accuracy_plt.plot(epochs, accuracy_train, label='train')
accuracy_plt.plot(epochs, accuracy_test, label='test')
accuracy_plt.set_xlabel('epochs')
accuracy_plt.set_ylabel('accuracy')
accuracy_plt.legend()

# Loss di traing e test
loss_train = np.array([4.0285, 3.8348, 3.6569, 3.4019, 3.2200,
                       3.0814, 2.9338, 2.8356, 2.7700])
loss_test = np.array([3.9126, 3.8309, 3.7173, 3.5845, 3.4986,
                      3.4388, 3.4005, 3.3779, 3.3672])

# plotting della loss
loss_plt.plot(epochs, loss_train, label='train')
loss_plt.plot(epochs, loss_test, label='test')
loss_plt.set_xlabel('epochs')
loss_plt.set_ylabel('loss')
loss_plt.legend()

# plot datas
plt.show()
