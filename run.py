from bernoulli import bernoulli
from geometric import geometric

bernoulli(0.8, 3)
geometric(0.01, 15)

# import matplotlib.pyplot as plt

# data = []

# for k in range(0, 51):
#     data.append((geometric(0.01, k), k))


# p_values = [item[0] for item in data]
# k_values = [item[1] for item in data]

# plt.bar(k_values, p_values)

# plt.xlabel('k')
# plt.ylabel('P(X = k)')
# plt.title('')

# plt.show()
