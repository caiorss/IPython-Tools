# -*- coding: utf-8 -*-
# 000-start.py
# usage:
#     $ ipython --profile=chordMe

__ip__ = get_ipython()

print("Type %usage:")


def exec_userns(code):
    exec(code, __ip__.user_ns)


def magic(name):
    """
    Decorator to register Ipython Magic
    """
    def wrap(f):
        __ip__.define_magic(name, f)
    return wrap
    
#--------------------------------------------------------------------#

import os
import sys

from utils3 import Chain, Path
from utils3 import hof
from utils3.hof import ( mapl, zipl, zipwith )

from m2py.misc import units
from m2py.misc import constants as const


import matplotlib.pyplot as plt
plt.ion()
plot = plt.plot
scatter = plt.scatter 
show = plt.show
grid = plt.grid
xlabel = plt.xlabel
ylabel = plt.ylabel
title = plt.title


#from utils import paste_run

#import matplotlib.pyplot as plt
#from   matplotlib.pyplot import show, grid, scatter, plot, xtitle, ytitle, title

#plt.ion())

#plt.ion()

import numpy as np
from numpy import ( 
#trigonometric functions
sin, cos, tan, tanh, sinh, cosh, array, arcsin, arctan,
arccos, exp, sqrt, log, log10, power, 
# Statistical
cumsum, cumprod, random, std, var, mean, average, histogram,
# Matrix
transpose, arange, linspace, logspace, zeros, eye,
# Misc
nan, pi, round, 
# Polynomia
poly, polyadd, polyder, polydiv, polyfit, polyint, polymul, polysub, polyval,
)

#from m2py.thermo import xsteam, gas
#from m2py.finance import dtime


    
    
@magic("addpath")
def __addpath(self, path):
    """ 
    Add path to sys.path 
    
    %addpath <path>
    """
    sys.path.append(path)

#ip.define_magic("addpath", __addpath)


@magic("see")
def __see(self, args):
    """
    Explore Object members

    Usage:

        %see <type> <object>

        <type>

        a       : Print all object members
        f       : Print all object functions
        m       : Print all object modules
        c       : Print all classes defined in object
        file    : See which file the object is defined
        v       : Print all values (float, ndarray defined in module)

    Example:
    In [14]: import os
    In [15]: see f os
    _execvpe ._exists ._get_exports_list ._make_stat_result ...

    """

    import inspect

    try:
        type, obj = args.split()
        obj = eval(obj, __ip__.user_ns)
    except Exception as err:
        print("""
        Explore Object members

        Usage:

            %see <type> <object>

            <type>

            a       : Print all object members
            f       : Print all object functions
            m       : Print all object modules
            c       : Print all classes defined in object
            file    : See which file the object is defined
            v       : Print all values (float, ndarray defined in module)

        Example:
        In [14]: import os
        In [15]: see f os
        _execvpe ._exists ._get_exports_list ._make_stat_result ...
        """)

        print(err)
        return

    members = inspect.getmembers(obj)

    filter_member = lambda filterfunc: \
        [m[0] for m in members if filterfunc(m[1])]

    if type == "a":

        print(" ".join([m[0] for m in members]))

    elif type == "f":
        #funcs = [m[0] for m in members if inspect.isfunction(m[1])]
        funcs = filter_member(inspect.isfunction)
        print(" .".join(funcs))

    elif type == "file":
        print(inspect.getsourcefile(obj))

    elif type == "c":
        #classes = [m[0] for m in members if inspect.isclass(m[1])]
        classes = filter_member(inspect.isclass)
        print(" .".join(classes))

    elif type == "m":
        #classes = [m[0] for m in members if inspect.isclass(m[1])]
        modules = filter_member(inspect.ismodule)
        print(" ".join(modules))

    elif type == "v":
        #classes = [m[0] for m in members if inspect.isclass(m[1])]
        vfilter = lambda obj: isinstance(obj, float) or isinstance(obj, int)

        modules = filter_member(vfilter)
        print(" ".join(modules))

@magic("finance_mode")
def __finance_mode(self, arg):
    """
    Load financial extensions
    
    finance/fin     -  Financial calculations PV, FV, PMT, i_pmt, IRR, XIRR,
    factor          -  Financial factors
    bonds           -  Bond pricing and evaluation
    brbonds/br      -  Brazilian bond pricing
    dtime/dt        -  Date and day counting and operations related to date
    yahoo           -  Data from Yahoo Finance API
    """
    print("""
    FINANCIAL MODULE

    Name/Short Name
    ------------------------------------------------------------------------
    finance/fin     -  Financial calculations PV, FV, PMT, i_pmt, IRR, XIRR,
    factor          -  Financial factors
    bonds           -  Bond pricing and evaluation
    brbonds/br      -  Brazilian bond pricing
    dtime/dt        -  Date and day counting and operations related to date

    """)
    exec ("from m2py.finance import finance, factor", __ip__.user_ns)
    exec ("from m2py.finance import dtime as dt", __ip__.user_ns)
    exec ("from m2py.finance import brbonds as br", __ip__.user_ns)
    exec ("from m2py.finance import bonds", __ip__.user_ns)
    exec ("from m2py.finance.series import yahoo", __ip__.user_ns)
    exec ("fin = finance",__ip__.user_ns)
    


def disp(*params, **options):
    """
    Function To Display Numpy Matrix 
    on terminal in a nice way.
    
    """
    from tabulate import tabulate
    
    headers  = options.get("headers", "")
    tablefmt = options.get("tablefmt", "plain")
    
    if not params:
        return
    
    if len(params) == 1:    
        if isinstance(params, list) or isinstance(params[0], tuple):
            out = list(zip(*params[0]))
            #print tabulate(zip(*params[0]), headers=headers)
    
        else:
            #print tabulate(map(lambda x: [x], map(float, params[0])), headers=headers)
            out = [[x] for x in list(map(float, params[0]))]
    else:
        out = list(zip(*params))
        #print tabulate(zip(*params), headers=headers)
    
    print(tabulate(out, headers=headers, tablefmt=tablefmt))
    



__factors__ = { "10^-9": "p","10^-6": "u",  "10^-3": "m", "10^3": "k", "10^6": "M", "10^9": "G" }

def deg2rad(deg):
    return deg * pi / 180

def rad2deg(rad):
    return rad / pi * 180

def sind(x):
    return sin(deg2rad(x))

def cosd(x):
    return cos(deg2rad(x))

def tand(x):
    return sind(x)/cosd(x)

# def atand(x):
#     return rad2deg(atan(x))

def arctan2d(x, y):
    return rad2deg(arctan2(x, y))


def __powerise10__(x):

    """ Returns x as a * 10 ^ b with 0<= a <10
    """
    if x == 0: return 0 , 0
    Neg = x <0
    if Neg : x = -x
    a = 1.0 * x / 10**(floor(log10(x)))
    b = int(floor(log10(x)))
    if Neg : a = -a
    return a ,b

def eng(x):
    from math import floor
    """Return a string representing x in an engineer friendly notation"""
    a , b = __powerise10__(x)
    if -3<b<3: return "%.4g" % x
    a = a * 10**(b%3)
    b = b - b%3
    return "%.4g*10^%s" %(a,b)


def eng2(x):
    """Return a string representing x in an engineer friendly with prefix"""
    e = eng(x)
    base, factor = e.split("*")

    try:
        s= __factors__[factor]
        return "%s %s" % (base, s)
    except:
        return e
