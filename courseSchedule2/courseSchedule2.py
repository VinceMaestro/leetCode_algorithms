#
#   @param {number} numCourses: int
#   @param {number[][]} prerequisites: List[List[int]]
#   @return {number[]} List[int]
#

class Solution:
    def findOrder(self, numCourses, prerequisites):
        nbr_prereqs = [0] * numCourses;
        graph = [[] for i in range(numCourses)];
        for i, j in prerequisites:
            graph[j].append(i);
            nbr_prereqs[i] += 1;

        path = [i for i in range(numCourses) if nbr_prereqs[i] == 0]

        for el in path:
            for prereqs in graph[el]:
                nbr_prereqs[prereqs] -= 1;
                if (nbr_prereqs[prereqs] == 0):
                    path.append(prereqs);
        return(path if len(path) == numCourses else []);

sol = Solution();

print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]));
print(sol.findOrder(3, [[0,1],[0,2],[1,2]]));
print(sol.findOrder(3, [[1,0], [0,1],[0,2],[1,2]]));
