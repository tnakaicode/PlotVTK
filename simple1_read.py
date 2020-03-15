import numpy as np
import matplotlib.pyplot as plt
import meshio
import sys
import time
import os
from optparse import OptionParser

from base import plot2d

if __name__ == '__main__':
    argvs = sys.argv
    parser = OptionParser()
    parser.add_option("--file", dest="file", default="ugridex.vtk")
    opt, argc = parser.parse_args(argvs)
    print(opt, argc)

    reader = meshio.read(opt.file)
    print(reader)

    xyz = reader.points
    tri = reader.cells["quad"]
    dat_scl = reader.point_data["scalars"]
    dat_vec = reader.point_data["vectors"]
    
    obj = plot2d()
    obj.new_3Dfig()
    obj.axs.plot(xyz[:, 0], xyz[:, 1], xyz[:, 2])
    obj.SavePng_Serial()
    
    obj.new_2Dfig()
    obj.axs.tricontourf(xyz[:, 0], xyz[:, 1], dat_scl, cmap="jet")
    obj.SavePng_Serial()
