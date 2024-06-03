from keras.models import Sequential, load_model
from keras.layers import Dense, Flatten


class NeuralNetwork:
    def __init__(self):
        self.model = Sequential(
            [
                Flatten(input_shape=(256,)),
                Dense(128, activation="relu"),
                Dense(10, activation="softmax"),
            ]
        )

    def compile(self):
        self.model.compile(
            loss="categorical_crossentropy", optimizer="sgd", metrics="accuracy"
        )

    def print_log(self):
        self.model.summary()

    def train_model(self, x_train, y_train, epochs):
        self.model.fit(x_train, y_train, epochs=epochs)

    def evaluate(self, x_test, y_test):
        loss, accuracy = self.model.evaluate(x_test, y_test)
        return accuracy

    def predict(self, x_pr):
        return self.model.predict(x_pr)

    def save_model(self, model_name):
        self.model.save(f"learning_models/{model_name}.h5")

    def load_model(self, model_name):
        self.model = load_model(f"learning_models/{model_name}.h5")
