#include <bits/stdc++.h>
#include "util/constants.cpp"
using namespace std;

class Point {
    // create an n-dimensional point in space
public:
    vector<float> coordinate;

    Point() {
        coordinate.resize(DIMENSION);
    }

    bool operator<(const Point& other) const {
        return coordinate < other.coordinate;  // Uses lexicographical comparison
    }

};