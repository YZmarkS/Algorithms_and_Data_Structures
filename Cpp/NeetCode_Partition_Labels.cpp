#include <iostream>
#include <vector>

using namespace std;

vector<int> partitionLabels(string s) {
  int length = s.size();
  vector<int> results;
  cout << "Hello" << endl;
  int lastOccurences[26] = {};
  for (int i = length - 1; i >= 0; i--) {
    lastOccurences[(int)(s.at(i) - 'a')] = max(lastOccurences[(int)(s.at(i) - 'a')], i);
  }
  for (int i : lastOccurences) {
    cout << i << endl;
  }

  int last = 0, atLeast = lastOccurences[(int)(s.at(last) - 'a')];
  while (atLeast < length) {
    cout << last << " " << atLeast << endl;
    int i = last;
    while (i <= atLeast) {
      atLeast = max(atLeast, lastOccurences[(int)(s.at(i) - 'a')]);
      i++;
    }
    cout << last << " " << atLeast << " " << (i - last) << endl;
    results.push_back(i - last);
    if (i >= length) {
      break;
    }
    last = i;
    atLeast = lastOccurences[(int)(s.at(last) - 'a')];
  }
  return results;
}

int main() {
  vector<int> results = partitionLabels("xyxxyzbzbbisl");
  return 0;
}
