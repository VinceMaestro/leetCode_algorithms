/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
let findOrder = function(numCourses, prerequisites) {
  if (!numCourses || prerequisites == null) {
    return([]);
  }
  let starts = [];
  let graph = [];
  // initialiser graph de connections et liste de potentiel points de departs
  for (let noeud = 0; noeud < numCourses; noeud++) {
    graph[noeud] = {visited: false, connections: []};
    starts.push(noeud);
  }
  // construire graph de connections et retirer des points de departs les noeuds qui sont dependant des autres
  for (let i = 0; i < prerequisites.length; i++) {
    graph[prerequisites[i][1]].connections.push(prerequisites[i][0])
    const j = starts.indexOf(prerequisites[i][0]);
    if (j >= 0) {
      starts.splice(j, 1);
    }
  }
  if (starts.length == 0) {
    return([]);
  }
  // connecter les start a tout les autres
  for (let i = 0; i < starts.length; i++) {
    graph[starts[i]].connections = [];
    for (let j = 0; j < numCourses; j++) {
      if (starts[i] != j) {
        graph[starts[i]].connections.push(j)
      }
    }
  }
  // console.log(graph)

  // Now we do breath first search
  let cur = starts[0];
  graph[cur].visited = true;
  const queue = [cur]
  const path = [cur]
  while (queue.length > 0 || graph[cur].visited == false) {
    cur = queue.shift();
    for (let i = 0; i < graph[cur].connections.length; i++) {
      if (graph[graph[cur].connections[i]].visited == false) {
        graph[graph[cur].connections[i]].visited = true;
        queue.push(graph[cur].connections[i]);
        path.push(graph[cur].connections[i])
      }
    }
  }
  return(path)
};


ret = findOrder(3, [[0,1],[0,2],[1,2]]);
console.log('My output:', ret, 'expected:', '[ 2, 1, 0 ]')

ret = findOrder(1, []);
console.log(ret)
ret = findOrder(4, [[1,0],[2,0],[3,1],[3,2]]);
console.log(ret)
ret = findOrder(2, [[1,0]]);
console.log(ret)
