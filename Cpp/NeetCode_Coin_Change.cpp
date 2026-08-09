#include <iostream>
#include <vector>

int coinChain(vector<int>& coins, int amount) {
  int numCoins = coins.size();
  vector<vector<int>> dp(numCoins, vector<int>(amount + 1, -1));
  for (int i = 0; i < numCoins; i++) {
    dp[i][0] = 0;
  }
  for (int i = 0; i < numCoins; i++) {
    int coin = coins[i];
    for (int j = 1; j <= amount; j ++) {
      int prevLine = (i == 0) ? -1 : dp[i - 1][j];
      int earlierElem = ((j - coin) < 0) ? -1 : dp[i][j - coin];
      if (prevLine == -1 && earlierElem >= 0) {
	dp[i][j] = 1 + earlierElem;
      } else if (prevLine >= 0 && earlierElem == -1) {
	dp[i][j] = prevLine;
      } else if (prevLine >= 0 && earlierElem >= 0) {
	dp[i][j] = min(prevLine, 1 + earlierElem);
      }
    }
  }
  return dp[numCoins - 1][amount];
}
