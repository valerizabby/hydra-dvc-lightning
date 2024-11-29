#include "MeanVector.h"

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(vector_core, m) {
  m.doc() = R"doc(
    Python bindings for MeanVector library
  )doc";

  py::class_<MeanVector>(m, "MeanVector")
      .def_static("meanVector", &MeanVector::meanVector, R"doc(
          Compute mean value of vector using pure C++.

          Parameters:
            v : vector of float or integer values.

          Returns:
            float
                The mean value of vector.
      )doc");
}