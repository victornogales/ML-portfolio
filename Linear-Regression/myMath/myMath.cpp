#include <iostream>
#include <string>
#include <sstream>
#include "myMath.h"

using namespace std;

void myMath::boo() {
    cout << "Boo!\n";
}

int myMath::readData(const char* aFileName){

    ifstream input_file;
    string line, word;
    int rowIdx = 0;
    int colIdx = 0;
    
    // Opens the file
    input_file.open(aFileName, ios::in);

    // Loop over file lines
    while(getline(input_file, line)) {

        // Create a stringstream of the current line
        stringstream ss(line);

        // Extract each column from row
        while(getline(ss, word, ',')){
            if (colIdx==0)
                x.push_back(atof(word.c_str()));
            else
                y.push_back(atof(word.c_str()));
            colIdx++;
        }
        colIdx = 0;
        rowIdx++;
    }

    // Close the file
    input_file.close();
    return 0; 
}

void myMath::printData() {

    // Checks if there's data in the vectors
    if (x.empty()) {
        cout << "No data in memory." << endl;
    }

    // Print all data
    for (int i = 0; i < x.size(); i++) 
        cout << x[i] << "\t" << y[i] << endl;

    // Print Sizes
    cout << endl << "Size of x = " << x.size() << " Size of y = " << y.size() << endl << endl ;
}

void myMath::computeCost(float& total_cost, float w, float b) {

    float sum_cost = 0.0;
    // Run through all vector
    for (int i = 0; i < x.size(); i++) 
        sum_cost = sum_cost + pow(( w * x[i] + b ) - y[i],2);
    
    total_cost = sum_cost * ( 1 / (float) (x.size() * 2));
}

void myMath::computeGradient(float& dj_dw, float& dj_db, float w, float b) {

    float f_wb;
    int m = x.size();
    
    dj_db = 0;
    dj_dw = 0;

    for (int i = 0; i < m; i++) {
        f_wb = ( w * x[i] + b );
        dj_db = dj_db + f_wb - y[i];
        dj_dw = dj_dw + (f_wb - y[i]) * x[i];
    }
    dj_db = dj_db / (float) m;
    dj_dw = dj_dw / (float) m;
}

void myMath::gradientDescent(float& w, float& b, float alfa, int num_iters){

    float   dj_db = 0,
            dj_dw = 0;
    float   total_cost;

    for (int it = 0; it < num_iters; it++){

        // Calculate Gradient
        computeGradient(dj_dw, dj_db,w,b);

        computeCost(total_cost, w,b);

        // Update w and b
        w = w - alfa * dj_dw;
        b = b - alfa * dj_db;
    }   
}