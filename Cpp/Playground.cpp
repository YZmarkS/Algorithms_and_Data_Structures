#include <iostream>

using namespace std;

// class MyClass{
// public:
//   int num;
//   MyClass() {
//   }
// };

// void helper(MyClass &param) {
//   cout << param.num << "\n";
// }

void isArrayCopyByValue(int array[10]) {
  array[0] = 42;
}

int main() {
  int initArray[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

  cout << initArray[0] << "\n";
  isArrayCopyByValue(initArray);
  cout << initArray[0] << "\n";

  return 0;
}
