import matplotlib.pyplot as plt

likes = [10, 50, 80, 100, 200]
shares = [10, 2, 4, 3, 6]

plt.scatter(likes, shares, color = "red", label = "likes")

# plt.show()

plt.savefig("grafico-dispersion.png")