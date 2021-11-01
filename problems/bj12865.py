#평범함배낭

#sol1
import sys
read = sys.stdin.readline
N, K = map(int, read().split())
cache = [0] * (K+1)
for _ in range(N):
    w, v = map(int, read().split())
    for j in range(K, w-1, -1):
        cache[j] = max(cache[j], cache[j-w] + v)
print(cache[-1])

#sol2
import sys
read = sys.stdin.readline
N, K = map(int, read().split())
cache = {0: 0}
for _ in range(N):
    curr_w, curr_v = map(int, read().split())
    temp = {}
    for w, v in cache.items():
        if curr_w + w <= K and curr_v + v > cache.get(curr_w + w, 0):
            temp[curr_w + w] = curr_v + v
    cache.update(temp)
print(max(cache.values()))