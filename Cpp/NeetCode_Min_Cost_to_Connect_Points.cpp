#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <stdlib>

using namespace std;

int getRep(vector<int>& du, int key) {
  int curr = key;
  while (du[curr] != curr) {
    du[curr] = du[du[curr]];
    curr = du[curr];
  }
  return curr;
}

int connect(vector<int>& du, int key1, int key2) {
  int rep1 = getRep(du, key1), rep2 = getRep(du, key2);
  if (rep1 == rep2) {
    return true;
  }

  if (rep1 < rep2) {
    du[rep2] = rep1;
  } else {
    du[rep1] = rep2;
  }
  return false;
}

int minCostConnectPoints(vector<vector<int>>& points) {
  int length = points.size();
  vector<int> disjointUnion(length, 0);
  priority_queue<
    pair<int, pair<int, int>>,
    vector<pair<int, pair<int, int>>>,
    greater<pair<int, pair<int, int>>>> heap;
  for (int i = 0; i < length; i++) {
    disjointUnion[i] = i;
  }
  for (int i = 0; i < length; i++) {
    for (int j = 0; j < length; j++) {
      int distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
      heap.push( { distance, { i, j } } );
    }
  }
  int total = 0;
  while (!heap.empty()) {
    int const& edge = heap.top();
    heap.pop();
    bool was_connected = connect(disjointUnion, edge.second.first, edge.second.second);
    if (!was_connected) {
      total += edge.first;
    }
  }
  return total;
}
