# from matplotlib import pyplot as plt
#
# unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff eq.', 'Applications']
# middle_school_a = [80, 85, 84, 83, 86]
# middle_school_b = [73, 78, 77, 82, 86]
#
# def create_x(t, w, n, d):
#     return [t*x + w*n for x in range(d)]
# school_a_x = create_x(2, 0.8, 1, 5)
# school_b_x = create_x(2, 0.8, 2, 5)
#
#
# ax = plt.subplot()
# plt.bar(school_a_x, middle_school_a)
# plt.bar(school_b_x, middle_school_b)
#
# plt.title('Final exam Averages')
# plt.ylabel('test average')
# plt.xlabel('Year')
#
# plt.savefig('Resources/my_bar_chart.png')
#
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks([])
plt.ylim(-1.5, 1.5)
plt.yticks([])

plt.show()