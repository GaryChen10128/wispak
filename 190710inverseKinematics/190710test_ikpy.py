# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:25:19 2019

@author: 180218
"""

import ikpy
import numpy as np
from ikpy import plot_utils
#my_chain = ikpy.chain.Chain.from_urdf_file("../190709github_package_data/idk/poppy_ergo.URDF")
from ikpy.chain import Chain
from ikpy.link import OriginLink, URDFLink

my_chain = Chain(name='left_arm', links=[
    OriginLink(),
    URDFLink(
      name="shoulder",
      translation_vector=[-10, 0, 5],
      orientation=[0, 1.57, 0],
#      orientation=[0, 3.14, 0],
      rotation=[0, 1, 0],
    ),
    URDFLink(
      name="elbow",
      translation_vector=[35, 0, 0],
      orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    ),
    URDFLink(
      name="wrist",
      translation_vector=[22, 0, 0],
      orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    )
])


target_vector = [ 0.1, -0.2, 0.1]
target_frame = np.eye(4)
target_frame[:3, 3] = target_vector
print("The angles of each joints are : ", my_chain.inverse_kinematics(target_frame))
real_frame = my_chain.forward_kinematics(my_chain.inverse_kinematics(target_frame))
print("Computed position vector : %s, original position vector : %s" % (real_frame[:3, 3], target_frame[:3, 3]))
# If there is a matplotlib error, uncomment the next line, and comment the line below it.
# %matplotlib inline
#%matplotlib notebook
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
#figure(num=None, figsize=(18, 16), dpi=80, facecolor='w', edgecolor='k')
ax = plot_utils.init_3d_figure()
#ax.set_ylim([-10, 10])
#ax.set_xlim([-10, 10])
#my_chain.plot(my_chain.inverse_kinematics(target_frame), target=target_vector)
#ax.set_zlim(-50, 50)
#ax.set_xlim(-50, 50)
#ax.set_ylim(-50, 50)
ax.grid(linestyle='-', linewidth='0.5', color='red')
my_chain.plot(my_chain.inverse_kinematics(target_frame), ax, target=target_vector)

#plt.xlim(-0.1, 0.1)
#plt.ylim(-0.1, 0.1)
zo=50
ax.set_zlim(-zo, zo)
ax.set_xlim(-zo, zo)
ax.set_ylim(-zo, zo)
ax.grid(linestyle='-', linewidth='0.5', color='red')
#ax.grid(color='r', linestyle='-', linewidth=2)
#ax.legend()
plt.show()
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#import numpy as np
#
#xs = np.random.random(10)
#ys = np.random.random(10)
#zs = np.random.random(10)
#
#fig = plt.figure()  
#ax = fig.add_subplot(111, projection='3d')  
#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_zlabel('Z')
#ax.scatter(xs, ys, zs)  
#ax.set_zlim(-10,10)