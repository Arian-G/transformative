import dearpygui.dearpygui as dpg
import os

class tf_gui:
    def __init__( self ):
        dpg.create_context( )
        self.root = dpg.add_window( tag = "Primary Window" )
        dpg.create_viewport( title = "Transformative: A Graphics Application", width = 900, height = 700 )
        dpg.setup_dearpygui( )
        dpg.show_viewport( )
        dpg.set_primary_window( "Primary Window", True )
        self.create_menu_bar( )
        self.create_transformations_menu( )
        self.create_canvas( )
        self.main_loop( )

    def main_loop( self ):
        # dpg.start_dearpygui( )
        while dpg.is_dearpygui_running( ):
            dpg.render_dearpygui_frame( )
        dpg.destroy_context( )

    def create_menu_bar( self ):
        ##### Menu Bar
        menu_bar = dpg.add_menu_bar( parent = self.root )
        file_menu = dpg.add_menu( label = "File", parent = menu_bar )
        with dpg.group( horizontal = False, parent = file_menu ):
            dpg.add_menu_item( label = "Load", callback = lambda : self.select_file( "load" ))
            dpg.add_menu_item( label = "Save", callback = lambda : self.select_file( "save" ))
            dpg.add_menu_item( label = "Save As", callback = lambda : self.select_file( "save_as" ))

        ##### Settings Menu
        settings_menu = dpg.add_menu( label = "Settings", parent = menu_bar )
        with dpg.group( horizontal = True, parent = settings_menu ):
            with dpg.tooltip( dpg.add_text( "Steps:" )):
                dpg.add_text \
                (
                    "Determines the number of incremental steps in" +
                    "\nwhich to perform transformations or camera flys."
                )
            dpg.add_input_int( label = "", default_value = 5, width = 80, callback = lambda s: self.enforce_bounds( s, 1, 10 ))

        with dpg.group( horizontal = True, parent = settings_menu ):
            dpg.add_text( "" )

        with dpg.group( horizontal = False, parent = settings_menu ):
            with dpg.tooltip( dpg.add_button( label = "Reset Camera" )):
                dpg.add_text( "Resets the camera to its initial definition." )
            with dpg.tooltip(  dpg.add_button( label = "Reset Object" )):
                dpg.add_text( "Resets the object to its initial definition." )

        ##### About Menu
        about_menu = dpg.add_menu( label = "About", parent = menu_bar )
        with dpg.group( horizontal = False, parent = about_menu ):
            dpg.add_text \
            (
                "This program implements a graphics pipeline" +
                "\nincluding window to viewport mapping, parallel" +
                "\nand perspective projections, object transformations," +
                "\ncamera flying, multiple camera views, and polygonal" +
                "\nand smooth object representations."
            )

        with dpg.group( horizontal = True, parent = about_menu ): dpg.add_text( "" ) # Spacing.

        with dpg.group( horizontal = True, parent = about_menu ):
            dpg.add_text( "Transformative | Version 0.1" )

    def enforce_bounds( self, sender, min, max ):
        current_value = dpg.get_value( sender )
        if current_value < min:
            dpg.set_value( sender, min )
        elif current_value > max:
            dpg.set_value( sender, max )

    def select_file( option ):
        pass

    def create_transformations_menu( self ):
        transformation_menu = dpg.add_tree_node( label = "Transformations", parent = self.root )
        ##### Translation
        with dpg.tree_node( label = "Translation", parent = transformation_menu ):
            with dpg.group( horizontal = True ):
                dpg.add_text( "X Axis (Dx):" )
                dpg.add_input_float( default_value = 0.0, width = 100, 
                                     callback = lambda s: self.enforce_bounds( s, -100, 100 ), format = "%.1f" )
                dpg.add_text( "Y Axis (Dy):" )
                dpg.add_input_float( default_value = 0.0, width = 100, 
                                     callback = lambda s: self.enforce_bounds( s, -100, 100 ), format = "%.1f" )
                dpg.add_text( "Z Axis (Dz):" )
                dpg.add_input_float( default_value = 0.0, width = 100, 
                                     callback = lambda s: self.enforce_bounds( s, -100, 100 ), format = "%.1f" )
            dpg.add_button( label = "Translate" )
            # with dpg.group( horizontal = True, parent = transformation_menu ): dpg.add_text( "" ) # Spacing

        ##### Scaling
        with dpg.tree_node( label = "Scaling", parent = transformation_menu ):
            with dpg.group( horizontal = True ):
                dpg.add_text( "X Axis (Sx):" )
                dpg.add_input_float( default_value = 0.0, width = 100, 
                                     callback = lambda s: self.enforce_bounds( s, -100, 100 ), format = "%.1f" )
                dpg.add_text( "Y Axis (Sy):" )
                dpg.add_input_float( default_value = 0.0, width = 100, 
                                     callback = lambda s: self.enforce_bounds( s, -100, 100 ), format = "%.1f" )
                dpg.add_text( "Z Axis (Sz):" )
                dpg.add_input_float( default_value = 0.0, width = 100,
                                     callback = lambda s: self.enforce_bounds( s, -100, 100 ), format = "%.1f" )
            dpg.add_button( label = "Scale    " )
            # with dpg.group( horizontal = True, parent = transformation_menu ): dpg.add_text( "" ) # Spacing

        ##### Rotation
        with dpg.tree_node( label = "Rotation", parent = transformation_menu ):
            with dpg.group( horizontal = True ):
                dpg.add_text( "X Axis (Rx):" )
                dpg.add_input_float( default_value = 0.0, width = 100, 
                                     callback = lambda s: self.enforce_bounds( s, -100, 100 ), format = "%.1f" )
                dpg.add_text( "Y Axis (Ry):" )
                dpg.add_input_float( default_value = 0.0, width = 100, 
                                     callback = lambda s: self.enforce_bounds( s, -100, 100 ), format = "%.1f" )
                dpg.add_text( "Z Axis (Rz):" )
                dpg.add_input_float( default_value = 0.0, width = 100, 
                                     callback = lambda s: self.enforce_bounds( s, -100, 100 ), format = "%.1f" )
            dpg.add_button( label = "Rotate   " )
            # with dpg.group( horizontal = True, parent = transformation_menu ): dpg.add_text( "" ) # Spacing

    def create_canvas( self ):
        canvas_menu = dpg.add_tree_node( label = "Canvas", parent = self.root, selectable = True )
        with dpg.group( parent = canvas_menu ):
            with dpg.drawlist( width = 1920, height = 500, tag = "Canvas" ):
                dpg.draw_rectangle(( 100, 100 ), ( 200, 200 ), color = ( 255, 0, 0, 255 ), fill =( 200, 0, 0, 150 ))


tf_gui( )