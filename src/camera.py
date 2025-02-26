# camera.py
# Parallel and Perspective Camera Definitions

import numpy as np
from math import sqrt
from abc import ABC, abstractmethod

class camera( ABC ):
    """
    """
    __count = 1

    def __init__( self, name = f"Camera {__count}" ):
        """
        """
        self.name = name
        self.type = "parallel"
        self.vrp = np.array([ 0 ], [ 0 ], [ 0 ], [ 1 ])
        self.vpn = np.array([ 0 ], [ 0 ], [ 1 ], [ 1 ])
        self.vup = np.array([ 0 ], [ 1 ], [ 0 ], [ 1 ])
        self.prp = np.array([ 0 ], [ 0 ], [ 1 ], [ 1 ])
        self.umin, self.umax = -1, 1
        self.vmin, self.vmax = -1, 1
        self.nmin, self.nmax = -1, 1
        self.xmin, self.xmax = 0.1, 0.4
        self.ymin, self.ymax = 0.1, 0.4
        self.proj_matrix = None
        self.id = camera.__count
        camera.__count += 1
    
    @abstractmethod
    def create_proj_matrix( self ) -> None:
        """
        """
        pass
    
    @abstractmethod
    def clip( self ) -> None:
        """
        """
        pass

    @abstractmethod
    def project( self ) -> None:
        """
        """
        pass

class parallel_camera( camera ):
    """
    """
    def __init__( self, name ):
        super( ).__init__( name )

    def __create_proj_matrix( self ) -> None:
        """
        """
        # Create temps.
        vrp = self.vrp
        vpn = self.vpn
        vup = self.vup
        prp = self.prp

        # Translate VRP to the origin.
        dx, dy, dz = ( -vrp[ :3 ]).astype( float )
        trans_vrp = np.array \
        ([
            [ 1, 0, 0, dx ],
            [ 0, 1, 0, dy ],
            [ 0, 0, 1, dz ],
            [ 0, 0, 0, 1  ]
        ])

        # Rotate VPN ccw about x into xz plane.
        b, c = vpn[ 1: ].astype( float )
        denom = ( b ** 2 ) + ( c ** 2 )
        if denom != 0:
            denom = sqrt( denom )
            i = ( c ) / denom # i = c / sqrt(b^2 + c^2)
            j = ( b ) / denom # j = b / sqrt(b^2 + c^2)
        else:
            i = 1
            j = 0
        x_rot_vpn = np.array \
        ([
            [ 1, 0,  0, 0 ],
            [ 0, i, -j, 0 ],
            [ 0, j,  i, 0 ],
            [ 0, 0,  0, 1 ]
        ])
        # Update vectors.
        vpn = np.dot( x_rot_vpn, vpn )
        vup = np.dot( x_rot_vpn, vup )
    
    def __clip( self ) -> None:
        """
        """
        pass

    def __project( self ) -> None:
        """
        """
        pass


class perspective_camera( camera ):
    """
    """
    def __init__( self, name ):
        super( ).__init__( name )
        self.zmin = None

    def __create_proj_matrix( self ) -> None:
        """
        """
        pass
    
    def __clip( self ) -> None:
        """
        """
        pass

    def __project( self ) -> None:
        """
        """
        pass