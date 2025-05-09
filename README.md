# Transformative: A Graphics Application
## About
This program implements a graphics pipeline, including window to viewport mapping, <br>
parallel and perspective projections, object transformations, camera flying, multiple <br> 
camera views, and polygonal and smooth object representations. Certain features are still in development. <br> <br>
The objects are stored as .obj files, in `/assets` with the following representation:
```
v 1 1 0      # Defines a vertex at (1, 1, 0)
v 0.5 0.5 1
f 4 2 1      # Defines a face of vertices 4, 2, 1
f 3 4 1
```
The camera(s) are stored as .cset files, in `/src/util` with the following representation:
```
c                     # Defines a new camera
i front               # Camera name
t parallel            # Type of projection
r 0 0 4               # VRP (in WC)
n 0 0 -1              # VPN (in WC)
u 0 1 0               # VUP (in WC)
p 0 0 5               # PRP (in VRC)
w -4 4 -4 4 -20 100   # View volume (in VRC)
s 0.1 0.1 0.4 0.4     # Viewport
```
## Usages
- Use `python transf_gui.py` to run the program.
- Use `python transf_test.py` to unit test the program.
> [!NOTE]
> This program requires DearPyGui to run.
## Creators
- Arian G.
