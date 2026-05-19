#include <iostream>
#include <iomanip>

#define LIMIT 1000

using namespace std;

int capacityOfJuga;
int capacityOfJugb;

// function declearations
void displayStatus(int step, int a, int b);
int findMinimum(int value1, int value2);
bool findSolution(int required, int &steps);

int main()
{
    int required, steps = 0;

    cout << "Capacity of Jug A: ";
    cin >> capacityOfJuga;

    cout << "Capacity of Jug B: ";
    cin >> capacityOfJugb;

    cout << "Required water in Jug A: ";
    cin >> required;

    // Error checking
    if (capacityOfJuga < required)
    {
        cout << "\nError!Required water cannot fit in Jug A.\n";
    }
    else if ((capacityOfJuga == capacityOfJugb) &&
             capacityOfJuga != required)
    {

        cout << "\nError! Invalid input values.\n";
    }
    else
    {

        if (findSolution(required, steps))
        {
            cout << "\nSolution found in "
                 << steps << " steps.\n";
        }
        else 
        {
            cout << "\nSolution not found even after "
            << steps << " steps.\n";
        }
    }

    return 0;
}

// function to find minimum value

int findMinimum(int value1, int value2)
{
    int returnvalue = 0;
    if (value1 < value2)
        returnvalue = value1;
    else
        returnvalue = value2;

    return returnvalue;
}

// Main ai Logic
bool findSolution(int required, int &steps)
{
    int returnvalue = false;

    int a = 0;
    int b = 0;
    int step = 0;
    int temp = 0;

    cout << endl;
    cout << left
         << setw(20) << "operation"
         << setw(10) << "step#"
         << setw(10) << "Jug A"
         << setw(10) << "Jug B"
         << endl;
    cout << endl; 

    while (a != required && step < LIMIT)
    {

        step++;

        // if jug a empty -> fill it
        if (a == 0)
        {
            a = capacityOfJuga;
            cout << setw(20) << "Fill jug A";
            displayStatus(step, a, b);
        }

        // if jug B full -> Empty it

        else if (b == capacityOfJugb)
        {
            b = 0;
            cout << setw(20) << "Empty jug B";
            displayStatus(step, a, b);
        }

        // pour water form A to B
        else
        {
            temp = findMinimum(capacityOfJugb - b, a);

            b = b + temp;
            a = a - temp;
            cout << setw(20) << "pure A in B";
            displayStatus(step, a, b);
        }
    }
    steps = step;

    if (step ==  LIMIT)
        returnvalue = false;
    else
        returnvalue = true;

    return returnvalue;
}

void displayStatus(int step, int a, int b)
{

    cout << setw(10) << step
         << setw(10) << a
         << setw(10) << b
         << endl;
}