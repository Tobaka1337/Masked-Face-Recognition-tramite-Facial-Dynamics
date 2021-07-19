from matplotlib import pyplot as plt
import numpy as np


fig, axs = plt.subplots(2, 1)
accuracy_plt = axs[0]
loss_plt = axs[1]

# epoche di riferimento per Model VGGFACE
epochs = np.array([0, 25, 50, 75, 100, 125, 150, 175, 200,
                   225, 250, 275, 300, 325, 350, 375])

# Accuracy di train e test
accuracy_train = np.array([0.2935, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                          1, 1, 1, 1, 1, 1])
accuracy_test = np.array([0.5087, 0.8681, 0.8826, 0.8855, 0.8826,
                          0.8826, 0.8870, 0.8884, 0.8884, 0.8884,
                          0.8884, 0.8899, 0.8870, 0.8913, 0.8870,
                          0.8855])

# plotting dell'accuracy
accuracy_plt.plot(epochs, accuracy_train, label='train')
accuracy_plt.plot(epochs, accuracy_test, label='test')
accuracy_plt.set_xlabel('epochs')
accuracy_plt.set_ylabel('accuracy')
accuracy_plt.legend()

# Loss di traing e test
loss_train = np.array([3.2550, 0.0025, 3.1807E-5, 3.4401E-7,
                       6.0179E-8, 3.3187E-8, 3.6754E-8, 3.3918E-8,
                       4.6037E-8, 4.3244E-8, 4.2407E-8, 4.0914E-8,
                       4.4778E-8, 4.7918E-8, 4.5472E-8, 4.6947E-8])
loss_test = np.array([2.5793, 0.6820, 0.4899, 0.4531, 0.4492, 0.4528,
                      0.4467, 0.4526, 0.4569, 0.4690, 0.4823, 0.4828,
                      0.4855, 0.4798, 0.4867, 0.4999])

# plotting della loss
loss_plt.plot(epochs, loss_train, label='train')
loss_plt.plot(epochs, loss_test, label='test')
loss_plt.set_xlabel('epochs')
loss_plt.set_ylabel('loss')
loss_plt.legend()

# plot datas
plt.show()
