bool canJump(vector<int>& nums) {
  int len = nums.size();
  int furthest = 0;
  int curr = 0;
  while (curr <= furthest && curr < len) {
    int reachFromCurr = curr + nums[curr];
    furthest = max(furthest, reachFromCurr);
    curr++;
  }
  return curr == len;
}
