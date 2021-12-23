#!/usr/bin/python3.8

import sys
from image_detect_src import cuiqifan

cuiqifan( data_path=sys.argv[1] , res_path=sys.argv[2] , gain=sys.argv[3] ,
          magzp=sys.argv[4] , seeingdetimage=sys.argv[5])