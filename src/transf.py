# transf.py
# GUI

import dearpygui.dearpygui as dpg
import os

import transf_core

class tf_gui:
    def __init__(self):
        dpg.create_context()
        self.root = dpg.add_window(tag = "Primary Window")
        dpg.create_viewport(title = "Transformative: A Graphics Application", width = 900, height = 700)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("Primary Window", True)
        self.create_menu_bar()
        self.create_transformations_menu()
        self.create_camera_menu()
        self.create_canvas()
        self.create_status()
        self.create_theme()
        self.main_loop()

    def main_loop(self):
        while dpg.is_dearpygui_running():
            dpg.render_dearpygui_frame()
        dpg.destroy_context()

    def create_menu_bar(self):
        ##### Menu Bar
        menu_bar = dpg.add_menu_bar(parent = self.root)
        file_menu = dpg.add_menu(label = "File", parent = menu_bar)
        with dpg.group(horizontal = False, parent = file_menu):
            dpg.add_menu_item(label = "Load", callback = lambda: self.select_file("load"))
            dpg.add_menu_item(label = "Save", callback = lambda: self.select_file("save"))
            dpg.add_menu_item(label = "Save As", callback = lambda: self.select_file("save_as"))

        ##### Settings Menu
        settings_menu = dpg.add_menu(label = "Settings", parent = menu_bar)
        with dpg.group(horizontal = True, parent = settings_menu):
            with dpg.tooltip(dpg.add_text("Steps:")):
                dpg.add_text \
                (
                    "Determines the number of incremental steps in" +
                    "\nwhich to perform transformations or camera flys."
                )
            dpg.add_input_int(label = "", default_value = 5, width = 80, callback = lambda s: self.enforce_bounds(s, 1, 10))

        with dpg.group(horizontal = True, parent = settings_menu):
            dpg.add_spacer(height = 10)

        with dpg.group(horizontal = False, parent = settings_menu):
            with dpg.tooltip(dpg.add_button(label = "Reset Camera", width = 100)):
                dpg.add_text("Resets the camera to its initial definition.")
            with dpg.tooltip(dpg.add_button(label = "Reset Object", width = 100)):
                dpg.add_text("Resets the object to its initial definition.")

        ##### About Menu
        about_menu = dpg.add_menu(label = "About", parent = menu_bar)
        with dpg.group(horizontal = False, parent = about_menu):
            dpg.add_text \
            (
                "This program implements a graphics pipeline" +
                "\nincluding window to viewport mapping, parallel" +
                "\nand perspective projections, object transformations," +
                "\ncamera flying, multiple camera views, polygonal" +
                "\nand smooth object representations, and raytracing."
            )

        with dpg.group(horizontal = True, parent = about_menu): dpg.add_text( "" ) # Spacing.

        with dpg.group(horizontal = True, parent = about_menu):
            dpg.add_text("Transformative | Version 0.1")

    def select_file(self, option):
        f_dialog = dpg.add_file_dialog(show = True, default_path = os.getcwd(), height = 300)
        dpg.add_file_extension(".txt", parent = f_dialog)
        if option == "load":
            dpg.set_item_callback(f_dialog, self.load)
        elif option == "save":
            dpg.set_item_callback(f_dialog, self.save)
        else:
            dpg.set_item_callback(f_dialog, self.save_as)

    def load(self, _, app_data):
        filename = app_data["file_name"]
        res, s = transf_core().load(filename)
        if not res:
            self.show_status(s)

    def save(self, _, app_data):
        pass
    
    def save_as(self, _, app_data):
        pass

    def create_transformations_menu(self):
        transformation_menu = dpg.add_tree_node(label = "Transformations", parent = self.root, selectable = True)
        ##### Translation
        with dpg.tree_node(label = "Translation", parent = transformation_menu, selectable = True):
            with dpg.group(horizontal = False):
                with dpg.group(horizontal = True):
                    dpg.add_text("Dx:")
                    dpg.add_input_float(default_value = 0.0, width = 100, step = 1, 
                                        callback = lambda s: self.enforce_bounds(s, -10, 10), format = "%.1f")
                dpg.add_spacer(height = 5)
                with dpg.group(horizontal = True):
                    dpg.add_text("Dy:")
                    dpg.add_input_float(default_value = 0.0, width = 100, step = 1, 
                                        callback = lambda s: self.enforce_bounds(s, -10, 10), format = "%.1f")
                dpg.add_spacer(height = 5)
                with dpg.group(horizontal = True):
                    dpg.add_text("Dz:")
                    dpg.add_input_float(default_value = 0.0, width = 100, step = 1, 
                                        callback = lambda s: self.enforce_bounds(s, -10, 10), format = "%.1f")
                dpg.add_spacer(height = 5)
            dpg.add_button(label = "Translate", width = 80)
            dpg.add_spacer(height = 10)

        ##### Scaling
        with dpg.tree_node(label = "Scaling", parent = transformation_menu, selectable = True):
            with dpg.group(horizontal = True):
                dpg.add_text("Scale About (x, y, z):")
                dpg.add_input_text(hint = "0, 0, 0", width = 100)
            dpg.add_spacer(height = 5)
            with dpg.group(horizontal = True):
                dpg.add_text("Sx:")
                dpg.add_input_float(default_value = 1.0, width = 100, step = 0.1,
                                    callback = lambda s: self.enforce_bounds(s, 0.1, 10), format = "%.1f")
            dpg.add_spacer(height = 5)
            with dpg.group(horizontal = True):
                dpg.add_text("Sy:")
                dpg.add_input_float(default_value = 1.0, width = 100, step = 0.1, 
                                    callback = lambda s: self.enforce_bounds(s, 0.1, 10), format = "%.1f")
            dpg.add_spacer(height = 5)
            with dpg.group(horizontal = True):
                dpg.add_text("Sz:")
                dpg.add_input_float(default_value = 1.0, width = 100, step = 0.1,
                                    callback = lambda s: self.enforce_bounds(s, 0.1, 10), format = "%.1f")
            dpg.add_spacer(height = 5)
            dpg.add_button(label = "Scale", width = 80)
            dpg.add_spacer(height = 10)

        ##### Rotation
        with dpg.tree_node(label = "Rotation", parent = transformation_menu, selectable = True):
            with dpg.group(horizontal = True):
                dpg.add_text("Rotate About:")
                dpg.add_radio_button(items = ["X-axis", "Y-axis", "Z-axis", "Line AB"], horizontal = True,
                                     callback = self.axis_selection, tag = "axis_selector")
            dpg.add_spacer(height = 5)
            with dpg.group(horizontal = True):
                dpg.add_text("A (x, y, z):")
                dpg.add_input_text( hint = "0, 0, 0", width = 100, tag = "a_input")
            dpg.add_spacer(height = 5 )
            with dpg.group(horizontal = True ):
                dpg.add_text("B (x, y, z):" )
                dpg.add_input_text(hint = "1, 1, 1", width = 100, tag = "b_input")
            dpg.add_spacer(height = 5)
            with dpg.group(horizontal = True):
                dpg.add_text("Rx:", tag = "deg_label" )
                dpg.add_input_float(default_value = 0.0, width = 100, step = 1,
                                    callback = lambda s: self.enforce_bounds(s, -360, 360), format = "%.1f")
            dpg.add_spacer(height = 5)
            dpg.add_button(label = "Rotate", width = 80)
            dpg.add_spacer(height = 10)

            dpg.disable_item("a_input")
            dpg.disable_item("b_input")

    def axis_selection(self, sender):
        curr_axis = dpg.get_value(sender)
        if curr_axis == "X-axis":
            dpg.set_value("deg_label", "Rx:")
            dpg.disable_item("a_input")
            dpg.disable_item("b_input")
        elif curr_axis == "Y-axis":
            dpg.set_value("deg_label", "Ry:")
            dpg.disable_item("a_input")
            dpg.disable_item("b_input")
        elif curr_axis == "Z-axis":
            dpg.set_value("deg_label", "Rz:")
            dpg.disable_item("a_input")
            dpg.disable_item("b_input")
        else:
            dpg.set_value("deg_label", "Rv:")
            dpg.enable_item("a_input")
            dpg.enable_item("b_input")

    def create_camera_menu(self):
        with dpg.tree_node(label = "Camera", parent = self.root, selectable = True):
            with dpg.group(horizontal = True ):
                dpg.add_text("Camera:")
                dpg.add_combo(items = ["camera_1"], default_value = "camera_1", width = 100, tag = "camera_selector")
            dpg.add_spacer(height = 5)
            with dpg.group(horizontal = True):
                dpg.add_text("Current VRP (x, y, z):")
                dpg.add_input_text(hint = "", width = 100, tag = "curr_vrp")
                dpg.disable_item("curr_vrp")
            dpg.add_spacer(height = 5)
            with dpg.group(horizontal = True):
                dpg.add_text("To VRP (x, y, z):")
                dpg.add_input_text(hint = "1, 1, 1", width = 100, tag = "to_vrp")
            dpg.add_spacer(height = 5)
            dpg.add_button(label = "Fly", width = 80)
            dpg.add_spacer(height = 10)

    def create_canvas(self):
        canvas_menu = dpg.add_tree_node(label = "Canvas", parent = self.root, selectable = True)
        with dpg.group(parent = canvas_menu):
            with dpg.drawlist(width = 1920, height = 500, tag = "Canvas"):
                dpg.draw_rectangle((100, 100), (200, 200), color = (255, 0, 0, 255), fill = (200, 0, 0, 150))

    def create_status(self):
        with dpg.window(label = "Error", modal = True, show = False, tag = "status", width = 100, height = 100):
            self.status_text = dpg.add_text("")

    def show_status(self, s):
        dpg.set_value(self.status_text, s)
        dpg.show_item("status")

    def create_theme(self):
        prim_color = (66, 165, 245)
        light_bg = (33, 33, 33)
        darker_bg = (55, 55, 55)
        text_color = (220, 220, 220)

        with dpg.theme() as global_theme:
           # Window Theme
            with dpg.theme_component(dpg.mvWindowAppItem):
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, light_bg, category = dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Border, darker_bg, category = dpg.mvThemeCat_Core)
                # dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 5, category = dpg.mvThemeCat_Core)

            # Button Theme
            with dpg.theme_component(dpg.mvButton):
                dpg.add_theme_color(dpg.mvThemeCol_Button, prim_color, category = dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (81, 150, 245), category = dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (52, 115, 220), category = dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255), category = dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 2, category = dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 5, 5, category = dpg.mvThemeCat_Core)

            # Float Input Theme
            with dpg.theme_component(dpg.mvInputFloat):
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (235, 240, 255), category = dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Text, text_color, category = dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 2, category = dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 5, 3, category = dpg.mvThemeCat_Core)

            # Int Input Theme
            with dpg.theme_component(dpg.mvInputInt):
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (235, 240, 255), category = dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Text, text_color, category = dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 2, category = dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 5, 3, category = dpg.mvThemeCat_Core)

            # Text Input Theme
            with dpg.theme_component(dpg.mvInputText):
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (235, 240, 255), category = dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Text, text_color, category = dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 2, category = dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 5, 3, category = dpg.mvThemeCat_Core)

            # Text Input Disabled Theme
            with dpg.theme_component(dpg.mvInputText, enabled_state = False):
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (30, 30, 35), category = dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, (235, 240, 255), category = dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Text, text_color, category = dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 2, category = dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 5, 3, category = dpg.mvThemeCat_Core)

            # Combobox Theme
            with dpg.theme_component(dpg.mvCombo):
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 2, category = dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 5, 3, category = dpg.mvThemeCat_Core)

            # Radio Button Theme
            with dpg.theme_component(dpg.mvRadioButton):
                dpg.add_theme_color(dpg.mvThemeCol_Button, prim_color, category = dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, prim_color, category = dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (66, 165, 245), category = dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, prim_color, category = dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Text, text_color, category = dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 2, category = dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 5, 3, category = dpg.mvThemeCat_Core)
                
        dpg.bind_theme(global_theme)

    def enforce_bounds(self, sender, min, max):
        current_value = dpg.get_value(sender)
        if current_value < min:
            dpg.set_value(sender, min)
        elif current_value > max:
            dpg.set_value(sender, max)

tf_gui()