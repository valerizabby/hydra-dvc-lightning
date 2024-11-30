CXX=g++
CXXFLAGS=-std=c++11 -O3 -march=native -Wall -I$(SRC_DIR) $(shell python3 -m pybind11 --includes)
PY_LDFLAGS=$(shell python3-config --ldflags) -shared -fPIC -undefined dynamic_lookup
GTEST_FLAGS=-lgtest -lgtest_main -pthread
SRC_DIR=meanvector/src
TESTS_DIR=meanvector/tests
PYTHON_DIR=meanvector/python

all: MeanVector test

MeanVector: $(PYTHON_DIR)/bindings.o $(SRC_DIR)/MeanVector.o
	$(CXX) $^ -o $(PYTHON_DIR)/vector_core`python3-config --extension-suffix` $(PY_LDFLAGS) $(CXXFLAGS)

$(PYTHON_DIR)/bindings.o: $(PYTHON_DIR)/bindings.cpp $(SRC_DIR)/MeanVector.h
	$(CXX) $(CXXFLAGS) -fPIC -c $< -o $@

$(SRC_DIR)/MeanVector.o: $(SRC_DIR)/MeanVector.cpp $(SRC_DIR)/MeanVector.h
	$(CXX) $(CXXFLAGS) -fPIC -c $< -o $@

test: $(TESTS_DIR)/test_MeanVector.o $(SRC_DIR)/MeanVector.o
	$(CXX) $^ -o $(TESTS_DIR)/test_MeanVector $(GTEST_FLAGS) $(LDFLAGS)

$(TESTS_DIR)/test_MeanVector.o: $(TESTS_DIR)/test_MeanVector.cpp $(SRC_DIR)/MeanVector.h
	$(CXX) $(CXXFLAGS) -c $< -o $@

run_tests: test
	./$(TESTS_DIR)/test_MeanVector

clean:
	rm -f $(PYTHON_DIR)/*.o $(SRC_DIR)/*.o $(TESTS_DIR)/*.o $(PYTHON_DIR)/vector_core`python3-config --extension-suffix` $(TESTS_DIR)/test_MeanVector