"""Mission 1 starter, created in student_submission/mission_1/planners.py.

Open that submission file in your editor and implement the four functions.
The guide creates it automatically and never overwrites an existing file.

Each function receives ctx with start, goal, grid, heuristic(cell) and
expand(cell, frontier_size). Return a list of (row, column) cells including
start and goal, or [] after exhausting the search. Call ctx.expand once per
expanded node. Record the actual frontier size, not the number of visited cells.
The runner enforces an expansion budget and a separate process time limit.
Use only the Python standard library. Do not import planning.reference_path.
When a free start is already the goal, return the single starting cell with
zero moves. No expansion is required for that case. Use the six small checks
on the Mission 1 page before running the full canonical-map evaluation.
"""
from collections import deque
from heapq import heappush, heappop
from planning.core import reconstruct

def bfs(ctx):
    """FIFO queue. Mark discovered cells when enqueuing and store parents.
    Use ctx.expand(current, len(frontier)+1) to obtain neighbours.
    BFS minimizes number of uni t-cost edges, not execution time on a robot.
    """
    grid = ctx.grid
    sr, sc = ctx.start
    gr, gc = ctx.goal
    rows, cols = len(grid), len(grid[0])
    if not (0 <= sr < rows and 0 <= sc < cols and 0 <= gr < rows and 0 <= gc < cols):
        return []
    if grid[sr][sc] == 1 or grid[gr][gc] == 1:
        return []
    if ctx.start == ctx.goal:
        return [ctx.start]

    parent = {ctx.start: None}
    queue = deque([ctx.start])
    while queue:
        current = queue.popleft()
        if current == ctx.goal:
            return reconstruct(parent, ctx.goal)
        for nxt in ctx.expand(current, len(queue) + 1):
            if nxt not in parent:
                parent[nxt] = current
                queue.append(nxt)
    return []

def dfs(ctx):
    """LIFO stack. Track discovered cells and parents to avoid cycles.
    A valid DFS path need not be shortest. Keep the supplied neighbour order.
    """
    grid = ctx.grid
    sr, sc = ctx.start
    gr, gc = ctx.goal
    rows, cols = len(grid), len(grid[0])
    if not (0 <= sr < rows and 0 <= sc < cols and 0 <= gr < rows and 0 <= gc < cols):
        return []
    if grid[sr][sc] == 1 or grid[gr][gc] == 1:
        return []
    if ctx.start == ctx.goal:
        return [ctx.start]

    parent = {ctx.start: None}
    stack = [ctx.start]
    while stack:
        current = stack.pop()
        if current == ctx.goal:
            return reconstruct(parent, ctx.goal)
        for nxt in ctx.expand(current, len(stack) + 1):
            if nxt not in parent:
                parent[nxt] = current
                stack.append(nxt)
    return []

def iddfs(ctx):
    """Run depth-limited DFS with bounds 0, 1, 2, ... .
    Prevent cycles on the current path. Do not keep a global visited set across
    depth limits. Count expansions again on every iteration. Return [] only
    after exhaustive failure. Catch no budget exceptions. The runner records
    resource_limit honestly if this expensive method reaches its budget.
    """
    grid = ctx.grid
    sr, sc = ctx.start
    gr, gc = ctx.goal
    rows, cols = len(grid), len(grid[0])
    if not (0 <= sr < rows and 0 <= sc < cols and 0 <= gr < rows and 0 <= gc < cols):
        return []
    if grid[sr][sc] == 1 or grid[gr][gc] == 1:
        return []
    if ctx.start == ctx.goal:
        return [ctx.start]

    limit = 0
    while True:
        cutoff = False             
        path = []                    
        on_path = set()                  
        stack = [(ctx.start, 0)]
        while stack:
            current, depth = stack.pop()
            while len(path) > depth:
                on_path.remove(path.pop())
            path.append(current)
            on_path.add(current)

            if current == ctx.goal:
                return path

            for nxt in ctx.expand(current, len(stack) + 1):
                if nxt in on_path:  
                    continue
                if depth < limit:
                    stack.append((nxt, depth + 1))
                else:
                    cutoff = True
        if not cutoff:      
            return []
        limit += 1

def astar(ctx):
    """Use a heap ordered by g + ctx.heuristic(cell).
    Keep best g costs and parents. Ignore outdated heap entries. Each edge
    costs 1. Stop when the goal is removed from the priority queue.
    """
    grid = ctx.grid
    sr, sc = ctx.start
    gr, gc = ctx.goal
    rows, cols = len(grid), len(grid[0])
    if not (0 <= sr < rows and 0 <= sc < cols and 0 <= gr < rows and 0 <= gc < cols):
        return []
    if grid[sr][sc] == 1 or grid[gr][gc] == 1:
        return []
    if ctx.start == ctx.goal:
        return [ctx.start]

    best_g = {ctx.start: 0}
    parent = {ctx.start: None}
    heap = []
    heappush(heap, (ctx.heuristic(ctx.start), 0, ctx.start))
    while heap:
        _, g, current = heappop(heap)
        if g > best_g.get(current, float('inf')):
            continue                 
        if current == ctx.goal:
            return reconstruct(parent, ctx.goal)
        for nxt in ctx.expand(current, len(heap) + 1):
            ng = g + 1
            if ng < best_g.get(nxt, float('inf')):
                best_g[nxt] = ng
                parent[nxt] = current
                heappush(heap, (ng + ctx.heuristic(nxt), ng, nxt))
    return []