import heapq
import sys

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, x)
    else:
        if len(heap) != 0:
            print(heapq.heappop(heap))
        else:
            print(0)