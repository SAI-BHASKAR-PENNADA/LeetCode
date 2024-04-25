class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        heap = []
        heapq.heappush(heap,[0,k])
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        while heap:
            wei,node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited)==n:
                return wei

            for nei,w in graph[node]:
                heapq.heappush(heap,[w+wei,nei])

        return -1