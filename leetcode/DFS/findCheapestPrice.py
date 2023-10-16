##787. Cheapest Flights Within K Stops
#There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
#You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.




class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        self.destinations = set()
        self.graph = self.construct_graph(flights)
        self.dst = dst
        if dst not in self.destinations:
            return
        ans = self.dfs(src,k)
        if ans == float("inf"):
            return -1
        return ans

    def construct_graph(self,flights):
        graph = defaultdict(list)
        for i,j,price in flights:
            self.destinations.add(j)
            graph[i].append([j,price])
        return graph
    @lru_cache(None)
    def dfs(self,src,k):
        if src == self.dst:
            return 0
        if k < 0:
            return float("inf")
        ans = float("inf")
        for next,price in self.graph[src]:
            ans = min (ans, self.dfs(next,k-1) + price)
        return ans


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dic = defaultdict(dict)
        destinations = set()
        for start, end, price in flights:
            destinations.add(end)
            dic[start][end] = price
        if dst not in destinations:
            return -1
        @lru_cache(None)
        def findCheapestPrice(k, src):
            if src == dst:
                return 0
            if k < 0:
                return inf
            ans = inf
            for nxt in dic[src]:
                ans = min(ans, findCheapestPrice(k - 1, nxt) + dic[src][nxt])
            return ans
        cheapest = findCheapestPrice(k, src)
        return cheapest if cheapest != inf else -1




