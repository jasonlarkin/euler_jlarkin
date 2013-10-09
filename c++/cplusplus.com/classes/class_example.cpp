// classes example
#include <iostream>
using namespace std;

class CRectangle {
    int x, y;
  public:
    void set_values (int,int);
    int area () {return (x*y);}
};

void CRectangle::set_values (int a, int b) {
  x = a;
  y = b;
}

class CRectangle_internal {
   int x, y;
  public:
   void set_values (int a, int b) {
    x = a;
    y = b;}
   int area () {return (x*y);}
};

class CRectangle_con {
    int x, y;
  public:
    CRectangle_con ();
    CRectangle_con (int,int);
    int area () {return (x * y);}
};

CRectangle_con::CRectangle_con () {
  x = 5;
  y = 5;
}

CRectangle_con::CRectangle_con (int a, int b) {
  x = a;
  y = b;
}

class CRectangle_des {
    int *x, *y;
  public:
    CRectangle_des (int,int);
    ~CRectangle_des ();
    int area () {return (*x * *y);}
};

CRectangle_des::CRectangle_des (int a, int b) {
  x = new int;
  y = new int;
  *x = a;
  *y = b;
}

CRectangle_des::~CRectangle_des () {
  delete x;
  delete y;
}

//class CRectangle_implicit {
//  public:
//    int a,b;
//    CRectangle_implicit (int x, int y) {a = x; b = y; };
//    int area () { a * b;}
//};

//CRectangle_implicit::CRectangle_implicit (const CRectangle_implicit& rv) {
//  a=rv.a; b=rv.b;
//}

class CExample {
  public:
    int a,b,c;
    CExample (int n, int m) { a=n; b=m; };
    void multiply () { c=a*b; };
  };

CExample::CExample (const CExample& rv) {
  a=rv.a;  b=rv.b;  c=rv.c;
  }


int main () {
//first example
  CRectangle rect;
  rect.set_values (3,4);
  cout << "area: " << rect.area() << "\n";
//example of internal vs external class func defn
  CRectangle_internal rect_internal;
  cout << "area internal: " << rect_internal.area() << "\n";
  rect_internal.set_values(3,4);
  cout << "area internal: " << rect_internal.area() << "\n";
//example of multiple instances
  CRectangle rectb;
  rectb.set_values(5,6);
  cout << "areab: " << rectb.area() << "\n";
//constructors
  CRectangle_con rectc;
  CRectangle_con rectd (5,6);
  cout << "rectc area: " << rectc.area() << endl;
  cout << "rectd area: " << rectd.area() << endl;
//destructor
//implicit default
//  CRectangle_implicit rect_implict (2,3);
//  CRectangle_implicit rect_implicit2 (rect_implicit);
//  cout << "rect_implict: " << rect_implict.area() << endl;
//  cout << "rect_implict2: " << rect_implict2.area() << endl;

//  CExample ex (2,3);
//  CExample ex2 (ex);

//pointers

  

  return 0;
}
