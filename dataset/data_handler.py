import numpy as np
import matplotlib.pyplot as plt

from draw_engine.config import *


class DataHandler:
    def __init__(self):
        self.x_set = None
        self.y_set = None

    def load_x_data(self):
        self.x_set = np.load('dataset/xdataset.npy')

    def load_y_data(self):
        self.y_set = np.load('dataset/ydataset.npy')

    def load_sets(self):
        self.load_x_data()
        self.load_y_data()

    def save_x(self):
        np.save('dataset/xdataset.npy', self.x_set)

    def save_y(self):
        np.save('dataset/ydataset.npy', self.y_set)

    def append_x_data(self, new_x):
        self.load_x_data()
        self.x_set = np.concatenate((self.x_set, new_x))

    def append_y_data(self, new_y):
        self.load_y_data()
        self.y_set = np.concatenate((self.y_set, new_y))

    def find_empty(self):
        x_correct = []
        y_correct = []

        for i in range(len(self.x_set)):
            for j in self.x_set[i]:
                if j != 0:
                    x_correct.append(self.x_set[i])
                    y_correct.append(self.y_set[i])
                    break

        self.x_set = np.array(x_correct)
        self.y_set = np.array(y_correct)

    def remove(self, y_value):
        x_correct = []
        y_correct = []

        for i in range(len(self.x_set)):
            if self.y_set[i][y_value] == 1:
                break
            else:
                x_correct.append(self.x_set[i])
                y_correct.append(self.y_set[i])

        self.x_set = np.array(x_correct)
        self.y_set = np.array(y_correct)

    def print_data(self):
        for i in range(len(self.x_set)):
            print(i, self.x_set[i], self.y_set[i], sep='\n')
            print('_______________________________')

    def print_data_matrix(self):
        for i in range(len(self.x_set)):
            print(self.x_set[i].reshape(PX_AMOUNT, PX_AMOUNT))
            print()
            print(self.y_set[i])
            print('_______________________________')

    def img_(self):
        fig, axs = plt.subplots(1, 10)
        for i, vector in enumerate(self.x_set[len(self.x_set) - 10:len(self.x_set)]):
            matrix = vector.reshape(PX_AMOUNT, PX_AMOUNT)
            axs[i].imshow(matrix, cmap='gray')
        plt.show()

    def img_nums(self):
        nums = {}
        for i in range(len(self.y_set)):
            for j in range(len(self.y_set[i])):
                if self.y_set[i][j] == 1:
                    if j not in nums.keys():
                        nums[j] = i

        nums = sorted(nums.items(), key=lambda item: item[0])
        nums = {k: v for k, v in nums}

        fig, axs = plt.subplots(1, len(nums))
        for i, (key, value) in enumerate(nums.items()):
            matrix = self.x_set[value].reshape(PX_AMOUNT, PX_AMOUNT)
            axs[i].imshow(matrix, cmap='gray')
            axs[i].set_title(f"|{key}|")
        plt.show()

    def nums_counter(self):
        nums = {}
        for vector in self.y_set:
            for i in range(len(vector)):
                if vector[i] == 1:
                    if i not in nums.keys():
                        nums[i] = 0
                    else:
                        nums[i] += 1
                    break

        nums = sorted(nums.items(), key=lambda item: item[0])
        nums = {k: v for k, v in nums}

        return nums

    def len_dataset(self):
        return len(self.x_set), len(self.y_set)

    def print_nums_counter(self):
        for k, v in self.nums_counter().items():
            print(k, ':', v)

    def print_len(self):
        print(self.len_dataset())

    @staticmethod
    def save_x_data(x_set):
        np.save('dataset/xdataset.npy', x_set)

    @staticmethod
    def save_y_data(y_set):
        np.save('dataset/ydataset.npy', y_set)




