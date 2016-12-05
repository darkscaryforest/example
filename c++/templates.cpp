#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>

using namespace std;

class A {
    public:
        int i;
};

class B {
    public:
        double r;
};

template <class T>
class ListTenElems {
    public:
        T elems[10];
        int curCount;
        int addElem(T elem);
        T printElemAt(int index) {
            cout << "variable i is " << elems[index].i << "\n";
            return elems[index];
        }
        ListTenElems() {
            int i = 0;
            curCount = 0;
            memset(elems, 0x0, sizeof(elems));
        }
};

template <class T>
int ListTenElems<T>::addElem(T elem) {
    if(curCount >= 10) {
        return -1;
    }
    elems[curCount] = elem;   
    curCount++;
    return curCount;
}

template <typename T> void printSize(T obj) {
    cout << "size of obj is " << sizeof(obj) << "\n";
}

int main() {
    A a;
    B b;
    a.i = 43;
    ListTenElems<A> list;
    printSize<A>(a);
    printSize<B>(b);

    list.addElem(a);
    a = list.printElemAt(0);
    return 0;
}
