# object.py
# Polygonal and Curved Object Definitions

from abc import ABC, abstractmethod

class object( ABC ):
    """
    """
    def __init__( self, name = "undefined" ):
        """
        """
        self.name = name
        self.type = None
        self.points = [ ]
        self.faces = [ ]

class polyg_object( object ):
    """
    """
    def __init__( self, name ):
        """
        """
        super( ).__init__( name )

class curved_object( object ):
    """
    """
    def __init__( self, name ):
        """
        """
        super( ).__init__( name )
     