import numpy as np
import matplotlib.pyplot as plt
import vtk
from vtk.util.numpy_support import vtk_to_numpy
#from vtk.util.numpy_support import vtk_to_numpy

reader = vtk.vtkXMLUnstructuredGridReader()
reader.SetFileName("pep1_7_OmegaV.vtu")
reader.Update()
data = reader.GetOutput()

reader.GetNumberOfPoints()
reader.GetNumberOfCells()
reader.GetNumberOfPointArrays()

points = data.GetPoints()
npts = points.GetNumberOfPoints()
x = vtk_to_numpy(points.GetData())

triangles = vtk_to_numpy(data.GetCells().GetData())
ntri = triangles.size // 4  # number of cells
tri = np.take(triangles, [n for n in range(
    triangles.size) if n % 4 != 0]).reshape(ntri, 3)

n_arrays = reader.GetNumberOfPointArrays()
for i in range(n_arrays):
    print(reader.GetPointArrayName(i))

u = vtk_to_numpy(data.GetPointData().GetArray(2))

# Mesh
plt.figure(figsize=(8, 8))
plt.triplot(x[:, 0], x[:, 1], tri)
plt.gca().set_aspect('equal')

# abs_u
plt.figure(figsize=(8, 8))
plt.tricontour(x[:, 0], x[:, 1], tri, u, 16)

plt.figure(figsize=(8, 8))
plt.tricontourf(x[:, 0], x[:, 1], tri, u, 16)
plt.show()
