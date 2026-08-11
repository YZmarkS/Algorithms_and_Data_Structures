#include <iostream>
#include <vector>
#include <deque>

int validTree(int n, vector<vector<int>>& edges) {
  if (edges.size() != n - 1) {
    return false;
  }
  vector<vector<int>> graph(n);
  for (vector<int>& pair : edges) {
    int src = pair[0], tgt = pair[1];
    graph[src].push_back(tgt);
    graph[tgt].push_back(src);
  }

  set<int> visited;
  deque<int> q;
  q.push_back(0);
  while (!q.empty()) {
    int src = q.pop_front();
    visited.insert(src);
    for (int next : graph[src]) {
      if (visited.find(next) == visited.end()) {
	q.push_back(next);
      }
    }
  }
  return visited.size() == n;
}
