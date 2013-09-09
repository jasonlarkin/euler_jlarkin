#include <iostream>
#include <string>
#include <sstream>
using namespace std;

struct movies_t {
 string title;
 int year;
};

int main ()
{
 string mystr;

 movies_t amovie;
 movies_t * pmovie;
 pmovie = &amovie;

 cout << "Enter title: ";
 getline (cin, amovie.title);
 cout << "Enter year: ";
 getline (cin, mystr);
 (stringstream) mystr >> amovie.year;

 cout << "\nYou have entered:\n";
 cout << pmovie->title;
 cout << " (" << pmovie->year << ")\n";

 return 0;
}
