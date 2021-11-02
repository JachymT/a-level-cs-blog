#include <iostream>
#include <stdlib.h>
#include <time.h>

using namespace std;

int main() 
{
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
          int childSol = num1 * num2;
          int temp = num1;
          num1 = childSol;
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
      } else{
        cout << "the answer was " << sol << "\n";
      }
    }
    
    cout << "your score was " << score;
    return 0;
}
