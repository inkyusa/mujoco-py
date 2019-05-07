#!/usr/bin/env python3
"""
Example of visualizing xml model
"""
from mujoco_py import load_model_from_path, MjSim, MjViewer
import math
import os
import argparse

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-m','--model', help='Description for foo argument', required=True)
args = vars(parser.parse_args())

print("args=",args['model'])

model = load_model_from_path(args['model'])
sim = MjSim(model)
viewer = MjViewer(sim)

viewer.cam.trackbodyid = 1
viewer.cam.distance = model.stat.extent * 5.0
#viewer.cam.lookat[2] += .8
#viewer.cam.elevation = -20

t = 0
while True:
    sim.data.ctrl[0] = 3.9
    sim.data.ctrl[1] = 0
    sim.data.ctrl[2] = 0
    sim.data.ctrl[3] = 0
    
    t += 1
    sim.step()
    viewer.render()
    if t > 100 and os.getenv('TESTING') is not None:
        break
