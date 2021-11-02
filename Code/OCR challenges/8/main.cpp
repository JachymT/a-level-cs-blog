#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <string>

using namespace std;

int main() 
{
    cout << "Enter your name:\n";
    string name;
    cin >> name;
    cout << "Answer these 10 arithmatic questions:\n";
    
    int score = 0;
    srand (time(NULL));
    
    for(int i=0; i < 10; i++){
        int num1 = (rand() % 10) + 1;         //random number between 1 and 10
        int num2 = (rand() % 10) + 1;
        int symbolInt = (rand() % 4) + 1;
      
        char symbol;
        int sol, ans;
      
         if(symbolInt == 1){
            symbol = '+';
            sol = num1 + num2;
        }else if(symbolInt == 2){
            symbol = '-';
            sol = num1 - num2;
        }else if(symbolInt == 3){
            symbol = '/';
            int mult = num1 * num2;
            int temp = num1;
            num1 = mult;
            sol = temp;
        }else{
            symbol = 'x';
            sol = num1 * num2;
        }
      
        cout << num1 << symbol << num2 << "=";
        cin >> ans;
      
        if(ans == sol){
            cout << "correct\n";
            score++;
        }else{
            cout << "the answer was " << sol << "\n";
        }
    }
    cout << name << "'s score was " << score << " out of 10";
    return 0;
}
