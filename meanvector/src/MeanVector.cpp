#include "MeanVector.h"

#include <vector>

double MeanVector::meanVector(const std::vector<double> &v){
    int sum = 0;
    for (double item : v) {
        sum += item;
    }
    return sum / v.size();
}