# transf_core
# Core Graphics Engine

class transf_core:
    """
    """
    def __init__( self ):
        """
        """
        pass

    def load( self, filename ) -> None:
        """
        """
        try:
            with open( filename, "r" ) as file:
                file.seek( 0 )
                for line in file:
                    params = line.split( )
                    id = params.pop( 0 )
                    match id:
                        # Check for vertex.
                        case "v":
                            x, y, z = params
                            pass
                        # Check for face.
                        case "f":
                            for i in range( 0, len( params )):
                                pass
                            pass
                        # Check for blank lines.
                        case _:
                            pass
        except FileNotFoundError:
            return False, "transf_core: File not found."
        except Exception:
            return False, "transf_core: Unexpected error encountered."
        return True, None