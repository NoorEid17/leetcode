class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pairs = 0
        rows = {}
        for i in range(n):
            row = []
            for j in range(n):
                row.append(grid[i][j])
            if tuple(row) in rows:
                rows[tuple(row)] += 1
            else:
                rows[tuple(row)] = 1

        pairs = 0
        for i in range(n):
            col = []
            for j in range(n):
                col.append(grid[j][i])
            if tuple(col) in rows:
                pairs += rows[tuple(col)]
        return pairs