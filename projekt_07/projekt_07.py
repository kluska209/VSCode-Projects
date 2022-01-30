import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
import argparse
from PIL import Image
from numpy.core.numeric import indices
from rich.console import Console
import rich.traceback
from rich.progress import track
import time
import random
import math
from math import *
from scipy.ndimage import convolve, generate_binary_structure
from pathlib import Path
import os
import glob
import imageio
import sys, subprocess
import ffmpeg

sys.path.append(r'D:\Program Files\Python\Python39\ffmpeg-N-104939-g98f87c3d29-win64-gpl\bin\ffmpeg.exe')

parser = argparse.ArgumentParser()
parser.add_argument('size', help = 'size of spin lattice (n x n)', type = int)
parser.add_argument('J', help = 'value of parameter J', type = float)
parser.add_argument('beta', help = 'value of parameter Beta', type = float)
parser.add_argument('H', help = 'value of magnetic field', type = float)
parser.add_argument('steps', help = 'number of steps of simulation', type = int)
parser.add_argument('-d','--density', help = 'initial value of spin +1 density', type = float, default = 0.5)
parser.add_argument('-n','--name', help = 'name of file with pictures', default = 'step')
parser.add_argument('-m','--mag_name', help = 'name of file with magnetization in step function', default = 'magnetization')
parser.add_argument('-a','--anim_name', help = 'name of file with animation', default = 'animation')

args = parser.parse_args()

def init_lattice():
    lattice = np.zeros((args.size,args.size))
    options = [-1,1]

    for i in range(args.size):
        for j in range(args.size):
            result = random.choices(options, weights=[10-args.density*10,args.density*10]) #wypluwa listę
            lattice[i][j] = int("".join([str(e) for e in result])) #lista->str->int

    return lattice

class simulation:
    def __init__(self, lattice):
        self.lattice = lattice
        self.size = args.size
        self.steps = args.steps
        self.J = args.J
        self.H = args.H
        self.beta = args.beta
        self.name = args.name
        self.mag_name = args.mag_name
        self.anim_name = args.anim_name
        self.number_of_spins = self.size**2
        self.path = os.getcwd()+"\\simulation_results"
        self.mag_array = []
        self.steps_array = []
        self.fig = plt.figure(figsize = (self.size, self.size))
        self.data = plt.imshow(self.lattice)
        self.data_array =[]

    def calculate_energy(self, lattice):
        kernel = generate_binary_structure(2,1) #generujemy jądro 
        kernel[1][1] = False
        energy = -self.J*lattice*convolve(lattice, kernel, mode='constant', cval=0) -self.H*lattice.sum()
        return energy.sum()

    def create_image(self, lattice, step):
        image = Image.new('RGB', (self.size, self.size), (89,182,217))
        #draw = ImageDraw.Draw(image)
        Path(self.path).mkdir(parents=True, exist_ok=True)   
        for i in range(self.size):
            for j in range(self.size):
                spin = lattice[i][j]
                if (spin == -1):
                    image.putpixel((j,i), (252,80,97))

        a,b = image.size
        resized_image = image.resize((4*a,4*b), Image.ANTIALIAS)
        resized_image.save(self.path+f'\\{self.name}_{step+1}.png')

    def create_animation(self, lattice, step):
        
        self.data_array.append(lattice)

        if (step == self.steps-1):

            def frame(i):
                self.data.set_data(self.data_array[i])
                return self.data,
       
            anim = FuncAnimation(self.fig, frame, frames = self.steps)
            writer = FFMpegWriter(fps = 60)
            anim.save(self.path+f'\\{self.anim_name}.mp4', writer = writer)
            plt.close()

    def calculate_magnetization(self, lattice, step):
        magnetization = lattice.sum()/self.number_of_spins
        self.mag_array.append(magnetization)
        self.steps_array.append(step)

        if (step == self.steps-1):
            plt.plot(self.steps_array, self.mag_array)
            plt.title("Magnetyzacja w funkcji kroku")
            plt.xlabel("Numer kroku")
            plt.ylabel("Magnetyzacja")
            plt.savefig(f'{self.mag_name}.png')

    
    def monte_carlo(self):
        print('Symulacja...')

        for step in track(range(self.steps)):

            i = random.randint(0,self.size-1)
            j = random.randint(0,self.size-1)
            spin = self.lattice[i][j]
            flipped_spin = -1*spin

            flipped_lattice = self.lattice.copy()
            flipped_lattice[i][j] = flipped_spin

            energy_ini = self.calculate_energy(self.lattice)
            energy_flipped = self.calculate_energy(flipped_lattice)

            dE = self.J*(energy_flipped-energy_ini)

            if dE<=0:
                self.lattice[i][j] = flipped_spin
    
            elif (dE>0)*(np.random.random() < np.exp(-self.beta*dE)):
                self.lattice[i][j] = flipped_spin
            
            self.create_image(self.lattice, step)
            self.create_animation(self.lattice, step)
            self.calculate_magnetization(self.lattice, step)        

def create_animation():
    input = os.getcwd()+"\\simulation_results"+f'\\{args.name}_*.png'
    output =  os.getcwd()+"\\animation.mp4"
    frame_rate = 24
    cmd = f'ffmpeg -framerate {frame_rate} -l "{input}" "{output}"'
    print(cmd)
    subprocess.check_output(cmd, shell = True)

s1 = simulation(init_lattice())
s1.monte_carlo()
#create_animation()