// my first program in C++

#include <iostream>
#include <string>
#include <sstream>
using namespace std;


int main ()
{
  unsigned int a; unsigned int b; 
  cout << "Hello World!";
  a = 1;
  b = 2;
  double big = 6.02e23;
  cout << '\n' << a << '\n' << big << '\v' << big << '\r' << big 
<< '\a';
  a = 11 / 3;
  cout << '\n' << a << '\n';
  ++a;
  cout << '\n' << a << '\n';
  a+=2;
  cout << '\n' << a << '\n';
  int B=3; int A=++B; 
  cout << '\n' << A << '\n' << B << '\n';
  B=3; A=B++;  
  cout << '\n' << A << '\n' << B << '\n';
  
  
  cout << '\n' << (7==5) << '\n';  

  cout << '\n' << !(5==5) << '\n';  

  cout << '\n' << !(6<=4) << '\n';  
  cout << '\n' << ( (5 == 5) && (3 > 6) ) << '\n';  

int i;
  cout << "Please enter an integer value: "<< '\n';
  cin >> i;
  cout << "The value you entered is " << i;
  cout << " and its double is " << i*2 << '\n';

string mystr;
  float price=0;
  int quantity=0;

  cout << '\n'  << "Enter price: ";
  getline (cin,mystr);
  stringstream(mystr) >> price;
  cout << "Enter quantity: ";
  getline (cin,mystr);
  stringstream(mystr) >> quantity;
  cout << "Total price: " << price*quantity << endl;

  return 0;
}
