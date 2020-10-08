#include <iostream>

using namespace std;

int main() {
    float epsilon = 1;
    bool sw = true;
    while (sw){
        if (epsilon + 1 <= 1)
            break;
        epsilon = epsilon / 2;
    }
    epsilon = 2 * epsilon;
    cout << "Epsilon en C++ es: "<<epsilon<<endl;
    return 0;
}