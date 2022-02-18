import matplotlib.pyplot as plt

data_num = [0.1, 0.5, 0.7,  1, 5, 10, 20, 50, 70, 100, 150]
spend_time = [14, 42, 65, 8, 26, 48, 55, 119, 228, 415, 715]
plt.plot(data_num, spend_time, marker='o')
plt.xlabel('data size (times, base size=880788, eg: 100*880788=88078800)')
plt.ylabel('elapsed time (s)')
plt.savefig('performance.png')
plt.show()
