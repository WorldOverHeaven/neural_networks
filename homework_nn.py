import numpy as np


def non_linear(a):
    return 1 / (1 + np.exp(-a))


f = non_linear


def non_linear_derivative(a):
    return f(a) * (1 - f(a))


class NeuralNetwork:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        np.random.seed(1)

        print(x.T.shape)
        print(y.T.shape)
        self.syn0 = 2 * np.random.random(x.T.shape) - 1
        self.syn1 = 2 * np.random.random(y.shape) - 1

    def train(self):
        for j in range(100000):

            # проходим вперёд по слоям 0, 1 и 2
            l0 = self.x
            l1 = non_linear(np.dot(l0, self.syn0))
            l2 = non_linear(np.dot(l1, self.syn1))

            # как сильно мы ошиблись относительно нужной величины?
            l2_error = self.y - l2

            if (j % 10000) == 0:
                print("Error:" + str(np.mean(np.abs(l2_error))))

            # в какую сторону нужно двигаться?
            # если мы были уверены в предсказании, то сильно менять его не надо
            l2_delta = l2_error * non_linear_derivative(l2)

            # как сильно значения l1 влияют на ошибки в l2?
            l1_error = l2_delta.dot(self.syn1.T)

            # в каком направлении нужно двигаться, чтобы прийти к l1?
            # если мы были уверены в предсказании, то сильно менять его не надо
            l1_delta = l1_error * non_linear_derivative(l1)

            self.syn1 += l1.T.dot(l2_delta)
            self.syn0 += l0.T.dot(l1_delta)

    def predict(self, x):
        l0 = x
        l1 = non_linear(np.dot(l0, self.syn0))
        l2 = non_linear(np.dot(l1, self.syn1))
        return l2


x = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1],
              [0, 0, 0]])

y = np.array([[1],
              [0],
              [0],
              [1],
              [1]])

net = NeuralNetwork(x, y)

net.train()

for i in x:
    print(i, net.predict(i))
