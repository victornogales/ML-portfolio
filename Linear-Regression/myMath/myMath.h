#pragma once
#include <vector>
#include <fstream>

using namespace std;

class myMath {
	vector<float> x;
	vector<float> y;
	string x_label;
	string y_label;
	public:
	void boo();
	int readData(const char* aFileName);
	void printData();
	void computeCost(float& total_cost, float w, float b);
	void computeGradient(float& dj_dw, float& dj_db, float w, float b);
	void gradientDescent(float& w, float& b, float alfa, int num_iters);
};
