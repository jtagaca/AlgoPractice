#include <iostream>

#include <string>

#include <bits/stdc++.h>

#include <chrono>

#include <sys/time.h>

using namespace std;

int fib1(int n, int &count) {

  if (n <= 1) {

    return n;

  } else {

    count++;

    return fib1(n - 1, count) + fib1(n - 2, count);
  }
}

void fib(int n) {

  int cot = 0;

  int f[n + 2];

  int i;

  f[0] = 0;

  f[1] = 1;

  for (i = 2; i <= n; i++) {

    f[i] = f[i - 1] + f[i - 2];

    cot++;
  }
  cout<<"This is type B"<<endl;

  cout << "The count was " << cot << endl;

  cout << "The " << n << " number was " << f[n] << endl;
};

int main() {

  int count = 0;

  int num1;

  cout << "Find the fib" << endl;

  cin >> num1;

  auto start = chrono::high_resolution_clock::now();

  ios_base::sync_with_stdio(false);

  fib(num1);

  auto end = chrono::high_resolution_clock::now();

  double time_taken =

      chrono::duration_cast<chrono::nanoseconds>(end - start).count();

  time_taken *= 1e-9;

  cout << "Time taken by program is : " << fixed << time_taken

       << setprecision(9);

  cout << " sec" << endl;

  start = chrono::high_resolution_clock::now();

  ios_base::sync_with_stdio(false);
  std::cout << "this is type A" << std::endl;
  cout << fib1(num1, count);
  cout << " And the count is " << count << endl;

  end = chrono::high_resolution_clock::now();

  double time_taken_ =

      chrono::duration_cast<chrono::nanoseconds>(end - start).count();

  time_taken_ *= 1e-9;

  cout << "Time taken by program is : " << fixed << time_taken

       << setprecision(9);

  cout << " sec" << endl;

  return 0;
}