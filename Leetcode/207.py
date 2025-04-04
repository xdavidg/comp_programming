from collections import deque


def canFinish(numCourses, prerequisites):
    adjacency = [[] for _ in range(numCourses)]
    degrees = [0] * numCourses

    for u, v in prerequisites:
        adjacency[u].append(v)
        degrees[v] += 1

    dq = deque(i for i in range(numCourses) if degrees[i] == 0)

    top_order = []
    count_visited = 0

    while dq:
        x = dq.popleft()
        top_order.append(x)
        count_visited += 1

        for neighbor in adjacency[x]:
            degrees[neighbor] -= 1
            if degrees[neighbor] == 0:
                dq.append(neighbor)

    return False if count_visited != numCourses else True


def main():
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]

    canFinish(numCourses, prerequisites)


if __name__ == "__main__":

    main()
