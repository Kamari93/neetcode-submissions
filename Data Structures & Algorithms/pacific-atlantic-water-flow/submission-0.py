class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from itertools import pairwise

        if not heights or not heights[0]:
            return []
        
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prev_height):
            if (r, c) in visited or heights[r][c] < prev_height:
                return
            
            visited.add((r, c))
            directions = (-1, 0, 1, 0, -1)

            for (dr, dc) in pairwise(directions):
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    dfs(nr, nc, visited, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        return [list(rc) for rc in pac & atl]