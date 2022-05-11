from torch import nn, load, tensor, squeeze
import numpy as np

class SBANeuralNet(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, means, std_devs, iterations):
        super(SBANeuralNet, self).__init__()
        # Storing means and std_devs for future queries
        self.means = means
        self.std_devs = std_devs
        self.iterations = iterations

        # Fully-connected Layers
        self.full_1 = nn.Linear(input_dim, hidden_dim)
        self.full_2 = nn.Linear(hidden_dim, output_dim)

        # Activation function
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # Aggregation of layer 1
        out = self.full_1(x)
        # Activation of layer 1
        out = self.sigmoid(out)

        # Aggregation of layer 2
        out = self.full_2(out)
        # Activation of layer 2
        out = self.sigmoid(out)
        return out

def query_nn(sample, model='country'):

    input_dim = 11
    hidden_dim = 16
    output_dim = 1

    means = [192686.97638362, 149488.78817546, 0.70938505,
                10.79725723, 110.7730781]
    std_devs = [283263.2337816198, 228414.4345042562, 0.1737809681118785,
                237.12046783672147, 78.85726121578227]
    iterations = 1
    country_model = SBANeuralNet(input_dim, hidden_dim, output_dim, means, std_devs, iterations)
    country_model.load_state_dict(load('./data/models/country_model.pt'))
    return {'code': 993}
    country_model.train(False)
    sample_tensor = tensor(np.array(sample).astype(np.float32))
    #TODO normalize

    output = squeeze(country_model(sample_tensor))
    output = int(output.round().detach().numpy())
    return output


if __name__ == '__main__':
    print(0)
