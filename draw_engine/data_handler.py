import random

import numpy as np
import matplotlib.pyplot as plt

from draw_engine.config import *


class DataHandler:
    def __init__(self):
        self.x_set = None
        self.y_set = None

    def new_x(self, x_set):
        self.x_set = x_set

    def new_y(self, y_set):
        self.y_set = y_set

    def load_x_data(self, path: str, filename: str):
        self.x_set = np.load(f"{path}{filename}.npy")

    def load_y_data(self, path: str, filename: str):
        self.y_set = np.load(f"{path}{filename}.npy")

    @property
    def get_x_set(self):
        return self.x_set

    @property
    def get_y_set(self):
        return self.y_set

    def get_x_index(self, index):
        return self.x_set[index]

    def get_y_index(self, index):
        return self.y_set[index]

    def vector_num(self, y_vector):
        return np.where(y_vector == 1)

    def save_x(self, path: str, filename: str):
        np.save(f"{path}{filename}.npy", self.x_set)

    def save_y(self, path: str, filename: str):
        np.save(f"{path}{filename}.npy", self.y_set)

    def append_x_data(self, new_x):
        self.x_set = np.concatenate((self.x_set, new_x))

    def append_y_data(self, new_y):
        self.y_set = np.concatenate((self.y_set, new_y))

    def shuffle_sets(self):
        indexes = [i for i in range(len(self.x_set))]
        random.shuffle(indexes)

        x_sh = []
        y_sh = []

        for i in indexes:
            x_sh.append(self.x_set[i])
            y_sh.append(self.y_set[i])

        self.x_set = np.array(x_sh)
        self.y_set = np.array(y_sh)

    def get_random_index(self):
        return random.randint(0, len(self.x_set) - 1)

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

    def img_(self):
        fig, axs = plt.subplots(1, 10)
        for i, vector in enumerate(self.x_set[len(self.x_set) - 10 : len(self.x_set)]):
            matrix = vector.reshape(PX_AMOUNT, PX_AMOUNT)
            axs[i].imshow(matrix, cmap="gray")
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
            axs[i].imshow(matrix, cmap="gray")
            axs[i].set_title(f"{key}")
        plt.show()

    def nums_counter(self):
        nums = {}
        for vector in self.y_set:
            for i in range(len(vector)):
                if vector[i] == 1:
                    if i not in nums.keys():
                        nums[i] = 1
                    else:
                        nums[i] += 1
                    break

        nums = sorted(nums.items(), key=lambda item: item[0])
        nums = {k: v for k, v in nums}

        return nums

    def len_dataset(self):
        return len(self.x_set), len(self.y_set)

    def print_data(self):
        for i in range(len(self.x_set)):
            print(i, self.x_set[i], self.y_set[i], sep="\n")
            print("_______________________________")

    def print_data_matrix(self):
        for i in range(len(self.x_set)):
            print(self.x_set[i].reshape(PX_AMOUNT, PX_AMOUNT))
            print()
            print(self.y_set[i])
            print("_______________________________")

    def print_data_matrix_index(self, index):
        print(self.x_set[index].reshape(PX_AMOUNT, PX_AMOUNT))
        print()
        print(self.y_set[index])
        print("_______________________________")

    def print_nums_counter(self):
        for k, v in self.nums_counter().items():
            print(k, ":", v)

    def print_len(self):
        print(self.len_dataset())
