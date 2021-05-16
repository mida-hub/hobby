import itertools
import numpy as np

h, w = map(int, input().split())

ahw = []
for i in range(h):
    ahw.append(list(map(int, input().split())))

ahw = np.array(ahw)
ahw_min = min(np.ravel(ahw))
print(sum(np.ravel(ahw-ahw_min)))
