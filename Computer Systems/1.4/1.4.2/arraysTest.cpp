#include <iostream>
#include <stdlib.h>
#include <string>

using namespace std;

int main(){
    //define 1D names array
    string names[5] = {"Julie", "John", "Janice", "Jerome", "Juan"};
    
    //print first 3 names in the array
    cout << "1.\n";
    for(int i=0; i < 3; i++){
        cout << names[i] << "\n";
    }
    
    //replace John with Jacob
    for(int i=0; i < 5; i++){
        if (names[i] == "John"){
            names[i] = "Jacob";
        }
    }
    
    // define 2D names array
    string names2[2][5]{
        {names[0],names[1],names[2],names[3],names[4]},
        {"Jeff", "Janet", "Joyce", "Jamie", "Josh"}
    };
    
    //print 2D names array
    cout << "\n2.\n";
    for(int i=0; i < 2; i++){
        for(int j=0; j < 5; j++){
            cout << names2[i][j] << "\n";
        }
    }
    
    //replace Jamie with a random string
    for(int i=0; i < 2; i++){
        for(int j=0; j < 5; j++){
            if (names2[i][j] == "Jamie"){
                names2[i][j] = "NULL";
            }
        }
    }
}
