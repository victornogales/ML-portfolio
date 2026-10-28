#include <iostream>
#include "myMath.h"

int main() {
    
    const char* inputFileName = "ex1data1.txt";
    myMath alinReg;

    float   b = 0, 
            w = 0,
            total_cost = 0;
    float   dj_db, dj_dw;


    if (alinReg.readData(inputFileName)) {
        cout << "Error opening " << inputFileName << endl;
        return 1;
    }

    // Print the date
    //alinReg.printData();

    // Calculates Total Cost
    alinReg.computeCost(total_cost,w,b);
    cout << "Total cost for w(" << w << ") and b(" << b << ") = " << total_cost << endl << endl;

    // Calculte Gradient
    alinReg.computeGradient(dj_dw, dj_db, w, b);
    cout << "Gradient at w(" << w << ") and b(" << b << ") = " << dj_dw << " " << dj_db << endl << endl;

    //    Gradient Descent
    alinReg.gradientDescent(w, b, 0.01, 1500);
    cout << "Converged w = " << w << "; Converged b = " << b << endl << endl;

    return 0;
}
