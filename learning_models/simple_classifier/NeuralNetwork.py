class Classifier:

    def __init__(self, layers, weights, activation_funcs):

        self.layers = layers
        self.weights = weights
        self.activations_funcs = activation_funcs
        
    def get_structure(self):
        ...

    def backpropagation_step(self, input_layer, predictable_value):
        ...

    def one_step_train(self, input_layer, ):
        ...

    def model_train(self, input_layers, output_layers):
        ...

    def model_predict(self):
        ...

    def calculate_accuracy(self):
        ...

    def set_new_structure(self, new_layers):
        ...

    def set_new_activation_funcs(self, new_activations_funcs):
        ...

    def get_model_structure(self):
        ...


