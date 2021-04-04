from setuptools import setup
import os
import shutil
from tkinter import Tk
from tkinter import *
from tkinter import messagebox as mb

setup(name='skjerns-utils',
      version='1.10',
      description='A collection of tools and boiler plate functions',
      url='http://github.com/skjerns/skjerns-utils',
      author='skjerns',
      author_email='nomail',
      license='GNU 2.0',
      packages=['stimer', 'sdill', 'ospath'],
      install_requires=['dill', 'dateparser', 'pyedflib', 'mat73', 'mss', 'lspopt', 'pytablewriter',
      'pybind11', 'emlearn', 'bleak', 'scikit-learn', 'dill','coverage', 'imageio', 'keras', 'natsort',
      'numba', 'tqdm', 'prettytable', 'pysnooper', 'mne', 'joblib', 'clipboard', 'dateparser', 
      'opencv-python==3.4.8.29', 'pygame', 'python-pptx', 'dominate'],
      zip_safe=False)


try:
    root = Tk()
    res = mb.askquestion('Copy startup script?', 'Do you want to copy the startup-imports.py to the ipython startup folder? This may have side-effects.\n\nIf you dont know what this does, click "No".')
    root.destroy()
    
    if res == 'yes':
        home = os.path.expanduser('~')
        ipython_path  = os.path.join(home, '.ipython', 'profile_default', 'startup')
        shutil.copy('./startup_imports.py', ipython_path)
        print('Copied startup-script to', ipython_path)
except:
    print('Could not copy to', ipython_path, '\ncopy manually')
import sys, os, traceback, types
