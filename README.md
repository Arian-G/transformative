# Transformative

<br>

## About
This program implements a graphics pipeline, including window to viewport mapping, <br>
parallel and perspective projections, object transformations, camera flying, multiple <br> 
camera views, polygonal and smooth object representations, and raytracing. Certain features are <br>
still in development.
> [!NOTE]
> This program is a modification of an assignment for UTA's CSE 4304 Computer Graphics.

<br>

The objects are stored as .obj files, in `/assets`, with the following representation:
```
v 1 1 0      # Defines a vertex at (1, 1, 0)
v 0.5 0.5 1
f 4 2 1      # Defines a face of vertices 4, 2, 1
f 3 4 1
```

<br>

The camera(s) are stored as .cset files, in `/src/util`, with the following representation:
```
c                     # Defines a new camera
i front               # Camera name
t parallel            # Type of projection
r 0 0 4               # VRP (in World Coordinates)
n 0 0 -1              # VPN (in World Coordinates)
u 0 1 0               # VUP (in World Coordinates)
p 0 0 5               # PRP (in View Reference Coordinates)
w -4 4 -4 4 -20 100   # View volume (in View Reference Coordinates)
s 0.1 0.1 0.4 0.4     # Viewport
```
<br>

## Usages
- Use `python transf.py` to run the program.
- Use `python transf_test.py` to unit test the program.
> [!NOTE]
> This program requires DearPyGui to run.

<br>

## Creators
- Arian G.
