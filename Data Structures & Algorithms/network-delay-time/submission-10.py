import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #if len(network) < n return -1
        adjList = {}
        heap = []
        network = {}
        heapq.heappush(heap, (0, k))

        for src, tgt, time in times:
            if src not in adjList:
                adjList[src] = []
            if tgt not in adjList:
                adjList[tgt] = []
            adjList[src].append((time, tgt))

        while heap:
            cost, node = heapq.heappop(heap)

            if node not in network:
                network[node] = cost 
            else:
                continue

            for time, neighbor in adjList[node]:
                heapq.heappush(heap, (time + cost, neighbor))
        
        print(network)
        print(adjList)

        return max(network.values()) if len(network) == n else -1