# find center of star graph
#https://leetcode.com/problems/find-center-of-star-graph/
import collections
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counter = {}
        for edge in edges:
            counter[edge[0]] = counter.get(edge[0], 0) + 1
            counter[edge[1]] = counter.get(edge[1], 0) + 1
        for key, value in counter.items():
            if value == len(edges):
                return key