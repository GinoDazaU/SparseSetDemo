#include <vector>
#include <stdexcept>
using namespace std;

class SparseSet {
private:
    vector<int> sparse;
    vector<int> dense;
    int size;
    int range;

public:
    SparseSet(int N) : sparse(N, -1), dense(N), size(0), range(N) {}

    void insert(int x) {
        validateRange(x);
        if (!contains(x)) {
            sparse[x] = size;
            dense[size] = x;
            size++;
        }
    }

    void erase(int x) {
        validateRange(x);
        if (contains(x)) {
            int index = sparse[x];
            int lastElement = dense[--size];
            dense[index] = lastElement;
            sparse[lastElement] = index;
            sparse[x] = -1;
        }
    }

    bool contains(int x) const {
        if (x < 0 || x >= range) return false;
        return sparse[x] != -1 && sparse[x] < size && dense[sparse[x]] == x;
    }

    vector<int> elements() const {
        return vector<int>(dense.begin(), dense.begin() + size);
    }

    int getRange() const {
        return range;
    }

private:
    void validateRange(int x) const {
        if (x < 0 || x >= range) {
            throw out_of_range("El elemento está fuera del rango permitido.");
        }
    }
};
