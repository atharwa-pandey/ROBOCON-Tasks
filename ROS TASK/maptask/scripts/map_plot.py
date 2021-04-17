#!/usr/bin/env python

from __future__ import print_function

import sys
from .map_from_image.srv import *
import rospy


def map_plot_client(centerX,centerY):
     rospy.wait_for_service('map_generate')
     try:
          map_generate = rospy.ServiceProxy('map_generate',map_from_image)
          resp1 = map_generate(centerX,centerY)
          return resp1
     except rospy.ServiceException as e:
          print("Service call failed: %s"%e)



def usage():
     return "%s [centerX centerY]"%sys.argv[0]

if __name__ == "__main__":
     if len(sys.argv) == 3:
          centerX = int(sys.argv[1])
          centerY = int(sys.argv[2])
     else:
           print(usage())
     sys.exit(1)
     image = Image.open(pathlib.Path('map4.jpg'))
     image = image.convert('1')

     return_array = []
     x_coordinates = []
     y_coordinates = []

     no_of_rays = 360

     image.thumbnail((400, 400))

     image_size = min(image.size)

     if image.getpixel((centerX, centerY)) == 0:
        print('invalid')
     else:
           for i in range(0,360,int(360/no_of_rays)):
               r  = 0

               currentX=round(centerX + r*math.cos(i*math.pi/180))
               currentY=round(centerY + r*math.sin(i*math.pi/180))

               while ((currentX < image_size and currentX >= 0) and (currentY < image_size and currentY >=0) and (image.getpixel((currentX, currentY)) != 0)):
                    currentX=round(centerX + r*math.cos(i*math.pi/180))
                    currentY=round(centerY + r*math.sin(i*math.pi/180))
                    r+=1
                    x_coordinates.append(currentX)
                    y_coordinates.append(currentY)

                    return_array.append((i, r))

     print(return_array)

     

     from PIL import Image
     import numpy as np
     img_w, img_h = 401,401
     data = np.zeros((img_h, img_w, 3), dtype=np.uint8)
     data[100, 100] = [255, 0, 0]
     for i in range(len(x_coordinates)):
          data[x_coordinates[i],y_coordinates[i]] = [255,255,255]
     img = Image.fromarray(data, 'RGB')
     img.show()
