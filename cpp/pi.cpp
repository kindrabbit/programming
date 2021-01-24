#include <stdio.h>
#include<iostream>
#include <math.h>
using namespace std;

int main() {
  double t = 1, pi = 0, n = 1.0, s = 1;
  while(fabs(t) >= 1e-4) {
  	
	cout << "n = " << n << " t = " << fabs(t) << endl;
  	
    pi += t;
    n += 2;
    s = -s;
    t = s/n;

  }
  
   pi *= 4;
  
  cout << "PI = " << pi << endl;
  
  return 0;
}
