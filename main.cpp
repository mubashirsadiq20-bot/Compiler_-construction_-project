#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    cout << "===== Mini Compiler Project =====\n";
    cout << "1. Lexical Analyzer\n";
    cout << "2. Exit\n";

    int choice;
    cout << "Enter your choice: ";
    cin >> choice;

    if(choice == 1){
        system("g++ lexer.cpp -o lexer");
        cout << "\nRunning Lexical Analyzer...\n";
        system("./lexer");
    }
    else{
        cout << "Exiting Program...\n";
    }

    return 0;
}