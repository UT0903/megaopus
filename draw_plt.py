import matplotlib.pyplot as plt
import numpy as np
data_num = np.array([0.1, 0.5, 0.7,  1, 5, 10, 20, 50, 70, 100, 150]) * 880788 / 1e6
print(data_num)
spend_time = [14, 42, 65, 8, 26, 48, 55, 119, 228, 415, 715]
plt.plot(data_num, spend_time, marker='o')
plt.xlabel('data size (1e6)')
plt.ylabel('elapsed time (s)')
plt.savefig('performance.png')
plt.show()
