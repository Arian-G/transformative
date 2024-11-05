import dearpygui.dearpygui as dpg
import os

class tf_gui:
    def __init__( self ):
        dpg.create_context( )
        self.root = dpg.add_window( tag = "Primary Window" )
        dpg.create_viewport( title = "Transformative: A Graphics Application", width = 800, height = 600 )
        dpg.setup_dearpygui( )
        dpg.show_viewport( )
        dpg.set_primary_window( "Primary Window", True )
        self.create_menu_bar( )
        # self.create_
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

        with dpg.group( horizontal = True, parent = about_menu ):
            dpg.add_text( "" )

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

tf_gui( )