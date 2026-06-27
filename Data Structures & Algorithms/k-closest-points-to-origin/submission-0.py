import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # points = [ [x-c, y-c], [x-c.y-c] ... ]

        # k = 2
        # 1-c -> heap
        # top [1-c]
        # 2-c -> heap
        # top [1-c, 2-c]
        # 3-c -> heap
        # 1-c > 3-c ? 

        max_h = []

        for x, y in points:
            # 0,0  ------- x,y
            e_distance = (x ** 2) + ( y**2 )

            # add to the heap
            # will pair distance with the appropriate coordinates
            heapq.heappush(max_h, (-e_distance, x, y))

            # [1-c, 2-c, 3-c] -- top
            # pop 3-c
            # [2-c, 1-c] -- top
            if len(max_h) > k:
                heapq.heappop(max_h)
        
        # max_heap will have 2 smallest coordinates 

        final = []

        final = [ [x,y] for (_, x, y) in max_h]

        return final









