#include "MeanVector.h"
#include <gtest/gtest.h>

TEST(MeanVectorTests, MeanVector) {
  std::vector<double> a = {1.0, 2.0, 3.0};
  std::vector<double> b = {1, 3};
  EXPECT_DOUBLE_EQ(5.0, MeanVector::meanVector(a));
  EXPECT_DOUBLE_EQ(2, MeanVector::meanVector(b));
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}