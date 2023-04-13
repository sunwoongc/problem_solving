import heapq
import sys

n = int(sys.stdin.readline())
leftHeap = [] # maxHeap (-minHeap)
rightHeap = [] # minHeap

for _ in range(n):
    num = int(sys.stdin.readline())
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)
    if rightHeap and (-leftHeap[0] > rightHeap[0]):
        left, right = heapq.heappop(leftHeap), heapq.heappop(rightHeap)
        heapq.heappush(leftHeap, -right)
        heapq.heappush(rightHeap, -left)

    print(-leftHeap[0])