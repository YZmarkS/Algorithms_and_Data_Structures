#include <iostream>
#include <vector>
#include <set>

using namespace std;

void helper(vector<int> const & pool, set<int>& used, vector<int> curr, vector<vector<int>>& result) {
  // for (const auto& element : curr) {
  //   cout << element << " ";
  // }
  // cout << endl;
  // for (const auto& element : pool) {
  //   cout << element << " ";
  // }
  // cout << endl;

  if (pool.size() == used.size()) {
    result.push_back(curr);
    return;
  }

  for (int num : pool) {
    if (used.find(num) != used.end()) {
      continue;
    }
    curr.push_back(num);
    used.insert(num);
    helper(pool, used, curr, result);
    curr.pop_back();
    used.erase(num);
  }

}

vector<vector<int>> permute(vector<int>& nums) {
  vector<int> curr;
  vector<vector<int>> result;
  set<int> used;
  helper(nums, used, curr, result);

  return result;

}

int main() {
  vector<int> pool = {1, 2, 3};
  vector<vector<int>> result = permute(pool);
  for (vector<int> & perm : result) {
    for (int elem : perm) {
      cout << elem << " ";
    }
    cout << endl;
  }
}
