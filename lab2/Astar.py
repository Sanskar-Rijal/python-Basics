from queue import PriorityQueue
import math
import pprint

G = {
    'Biratnagar': {'Itahari': 22, 'Rangeli': 25, 'Biratchowk': 30},
    'Itahari': {'Biratnagar': 22, 'Biratchowk': 11, 'Dharan': 20},
    'Biratchowk': {'Itahari': 11, 'Kanepokhari': 10, 'Biratnagar': 30},
    'Dharan': {'Itahari': 20},
    'Rangeli': {'Biratnagar': 25, 'Kanepokhari': 25},
    'Kanepokhari': {'Rangeli': 25, 'Biratchowk': 10, 'Urlabari': 12},
    'Urlabari': {'Kanepokhari': 12, 'Damak': 6},
    'Damak': {'Urlabari': 6}
}

h = {
    'Biratnagar': 46,
    'Itahari': 39,
    'Dharan': 41,
    'Rangeli': 28,
    'Biratchowk': 29,
    'Kanepokhari': 17,
    'Urlabari': 6,
    'Damak': 0
}

def aStar(G, h, start, goal):
    PQ = PriorityQueue()
    prev = {}
    visited = set()
    PQ.put((0 + h[start], (start, 0)))
    prev[start] = " "

    while not PQ.empty():
        outStateFscore, (outState, outStateGScore) = PQ.get()
        visited.add(outState)

        if outState == goal:
            return True, prev, outStateGScore

        for neighbor in G[outState]:
            if neighbor not in visited:
                neighborGScore = outStateGScore + G[outState][neighbor]
                PQ.put((neighborGScore + h[neighbor], (neighbor, neighborGScore)))
                prev[neighbor] = outState

    return False, prev, -math.inf


def reconstruct_path(G,prev,goal):
    path= goal
    while prev[goal] !=" ":
        path = prev[goal] + '->' + path
        goal = prev[goal]
    return path  



start = 'Dharan'
goal = 'Damak'
goalFound, prev, cost = aStar(G, h, start, goal)

if goalFound:
    print(reconstruct_path(G, prev, goal))
    print("Cost =", cost)
else:
    print("No solution found")
