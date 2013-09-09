// custom countdown using while

#include <iostream>
using namespace std;

int main ()
{


  int n;
  cout << "Enter the starting number > ";
  cin >> n;

  while (n>0) {
    cout << n << ", ";
    --n;
  }

  cout << "FIRE!\n";


unsigned long m;
  do {
    cout << "Enter number (0 to end): ";
    cin >> m;
    cout << "You entered: " << m << "\n";
  } while (m != 0);


for (n=10; n>0; n--)
  {
    cout << n << ", ";
    if (n==3)
    {
      cout << "countdown aborted!";
      break;
    }
  }


for (int n=10; n>0; n--) {
    if (n==5) continue;
    cout << n << ", ";
  }
  cout << "FIRE!\n";


n=10;
  loop:
  cout << n << ", ";
  n--;
  if (n>0) goto loop;
  cout << "FIRE!\n";

  return 0;
}








 
