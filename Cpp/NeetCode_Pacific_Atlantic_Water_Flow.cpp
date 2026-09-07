#include <iostream>
#include <deque>
#include <vector>
#include <utility>

using namespace std;

bool inBound(int n, int m, int r, int c) {
  return 0 <= r && r < n && 0 <= c && c < m;
}

vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
  int n = heights.size(), m = heights[0].size();
  vector<vector<bool>> pacific = vector<vector<bool>>(n, vector<bool>(m, false));
  vector<vector<bool>> atlantic = vector<vector<bool>>(n, vector<bool>(m, false));

  pair<int, int> directions[] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };

  for (int r = 0; r < n; r++) {
    for (int c = 0; c < m; c++) {
      pacific[r][c] = false;
      atlantic[r][c] = false;
    }
  }

  deque<pair<int, int>> queue;
  bool visited[n][m] = {} ;

  for (int r = 0; r < n; r++) {
    pacific[r][0] = true;
    visited[r][0] = true;
    queue.push_back({r, 0});
  }
  for (int c = 0; c < m; c++) {
    pacific[0][c] = true;
    visited[0][c] = true;
    queue.push_back({0, c});
  }

  while (queue.empty() == 0) {
    pair<int, int> cell = queue.front();
    int r = cell.first, c = cell.second;
    for (pair<int, int> direction : directions) {
      int dr = direction.first, dc = direction.second;
      int rr = r + dr, cc = c + dc;
      if (inBound(n, m, rr, cc)
	  && !visited[rr][cc]
	  && heights[r][c] <= heights[rr][cc]) {
	pacific[rr][cc] = true;
	visited[rr][cc] = true;
	queue.push_back( {rr, cc} );
      }
    }
    queue.pop_front();
  }

  for (int r = 0; r < n; r++) {
    for (int c = 0; c < m; c++) {
      visited[r][c] = false;
    }
  }

  for (int r = 0; r < n; r++) {
    atlantic[r][m - 1] = true;
    visited[r][m - 1] = true;
    queue.push_back({r, m - 1});
  }
  for (int c = 0; c < m; c++) {
    atlantic[n - 1][c] = true;
    visited[n - 1][c] = true;
    queue.push_back({n - 1, c});
  }

  while (queue.empty() == 0) {
    pair<int, int> cell = queue.front();
    int r = cell.first, c = cell.second;
    for (pair<int, int> direction : directions) {
      int dr = direction.first, dc = direction.second;
      int rr = r + dr, cc = c + dc;
      if (inBound(n, m, rr, cc)
	  && !visited[rr][cc]
	  && heights[r][c] <= heights[rr][cc]) {
	atlantic[rr][cc] = true;
	visited[rr][cc] = true;
	queue.push_back( {rr, cc} );
      }
    }
    queue.pop_front();
  }

  vector<vector<int>> result;
  for (int r = 0; r < n; r++) {
    for (int c = 0; c < m; c++) {
      if (pacific[r][c] && atlantic[r][c]) {
	result.push_back( { r, c } );
      }
    }
  }

  return result;
}

int main() {
  vector<vector<int>> heights = { {4,2,7,3,4},
				  {7,4,6,4,7},
				  {6,3,5,3,6} };
  vector<vector<int>> result = pacificAtlantic(heights);
  for (vector<int> cell : result) {
    for (int i : cell) {
      cout << i << " ";
    }
    cout << endl;
  }
}
