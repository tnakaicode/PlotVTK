import numpy as np
import matplotlib.pyplot as plt
import meshio

reader = meshio.read("pep1_7_OmegaV.vtu")
print(reader)
x = reader.points
triangles = reader.cells['triangle']
reader.point_data
u = reader.point_data['abs_term_u']

plt.figure(figsize=(8, 8))
plt.triplot(x[:, 0], x[:, 1], triangles)
plt.gca().set_aspect('equal')

# abs_u
plt.figure(figsize=(8, 8))
plt.tricontour(x[:, 0], x[:, 1], triangles, u, 16)

plt.figure(figsize=(8, 8))
plt.tricontourf(x[:, 0], x[:, 1], triangles, u, 16)
plt.show()
