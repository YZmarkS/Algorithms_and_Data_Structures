#include <iostream>
#include <pair>
#include <vector>
#include <deque>
#include <set>

bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
  vector<set<int>> outgoing(numCourses);
  vector<set<int>> incoming(numCourses);
  deque<int> q;
  for (vector<int>& pair : prerequisites) {
    int from = pair[0], to = pair[1];
    outgoing[from].insert(to);
    incoming[to].insert(from);
  }

  for (int i = 0; i < numCourses; i++) {
    if (incoming[i].size() == 0) {
      q.push_back(i);
    }
  }

  while (!q.empty()) {
    int from = q.front();
    q.pop_front();
    for (int to : outgoing[from]) {
      incoming[to].erase(from);
      if (incoming[to].size() == 0) {
	q.push_back(to);
      }
    }
  }

  int counter = 0;
  for (int i = 0; i < numCourses; i++) {
    counter += incoming[i].size();
  }

  return counter == 0;
}
