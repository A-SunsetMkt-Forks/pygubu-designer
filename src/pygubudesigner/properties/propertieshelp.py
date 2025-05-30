# translator marker
from pygubudesigner.i18n import translator as _

tooltip_help = {
    "class": _("Object class name."),
    "id": _("Object unique identifier."),
    "accelerator": _(
        "Specifies a string to display at the right side of the menu entry."
    ),
    "activerelief": _(
        "Specifies the relief to use when displaying the element that is active, if any."
    ),
    "activestyle": _(
        "Specifies the style in which to draw the active element."
    ),
    "activebackground": _(
        "Specifies background color to use when drawing active elements."
    ),
    "activeborderwidth": _(
        "Specifies a non-negative value indicating the width of the 3-D border drawn around active elements."
    ),
    "activeforeground": _(
        "Specifies foreground color to use when drawing active elements."
    ),
    "after": None,
    "anchor": _(
        "Specifies how the information in the widget is positioned relative to the inner margins."
    ),
    "aspect": _(
        "Specifies a non-negative integer value indicating desired aspect ratio for the text. The aspect ratio is specified as 100*width/height. 100 means the text should be as wide as it is tall, 200 means the text should be twice as wide as it is tall, 50 means the text should be twice as tall as it is wide, and so on."
    ),
    "autoseparators": _(
        "Specifies a boolean that says whether separators are automatically inserted in the undo stack. Only meaningful when the undo option is true."
    ),
    "background-tk": _(
        "Specifies the normal background color to use when displaying the widget."
    ),
    "background-ttk": _(
        "The widget's background color. If unspecified, the theme default is used."
    ),
    "backgroundimage": _(
        "This specifies an image to display on the frame's background within the border of the frame."
    ),
    "borderwidth": _(
        "Specifies a non-negative value indicating the width of the 3-D border to draw around the outside of the widget."
    ),
    "bigincrement": _(
        'Some interactions with the scale cause its value to change by "large" increments; this option specifies the size of the large increments.'
    ),
    "bitmap": _("Specifies a bitmap to display in the widget."),
    "blockcursor": _(
        "Specifies a boolean that says whether the blinking insertion cursor should be drawn as a character-sized rectangular block."
    ),
    "buttonbackground": _(
        "The widget's background color. If unspecified, the theme default is used."
    ),
    "buttonbackground-tk.Spinbox": _(
        "The background color to be used for the spin buttons."
    ),
    "buttoncursor": _("The cursor to be used when over the spin buttons."),
    "buttondownrelief": _("The relief to be used for the upper spin button."),
    "buttonuprelief": _("The relief to be used for the lower spin button."),
    "class_": _(
        "Specifies the window class. The class is used when querying the option database for the window's other options, to determine the default bindtags for the window, and to select the widget's default layout and style."
    ),
    "closeenough": _(
        "Specifies a floating-point value indicating how close the mouse cursor must be to an item before it is considered to be “inside” the item. Defaults to 1.0."
    ),
    "column_anchor": _(
        "Specifies how the text in this column should be aligned with respect to the cell."
    ),
    "columnbreak": _(
        "When this option is False, the entry appears below the previous entry. When this option is True, the entry appears at the top of a new column in the menu. This option is ignored on Aqua/macOS, where menus are always a single column."
    ),
    "command": None,
    "command-pygubu": _(
        "In pygubu-designer, a python function name used as the callback for the widget command property."
    ),
    "compound-tk": _(
        "Specifies if the widget should display text and bitmaps/images at the same time, and if so, where the bitmap/image should be placed relative to the text."
    ),
    "compound-ttk": _(
        "Specifies how to display the image relative to the text, in the case both text and image are present."
    ),
    "confine": _(
        "Specifies a boolean value that indicates whether or not it should be allowable to set the canvas's view outside the region defined by the scrollRegion argument."
    ),
    "container": _(
        "If true, it means that this window will be used as a container in which some other application will be embedded. The window should not have any children of its own in this application."
    ),
    "cursor": _("Specifies the mouse cursor to be used for the widget."),
    "default": _(
        "In a dialog box, one button may be designated the “default” button. active indicates that this is currently the default button; normal means that it may become the default button, and disabled means that it is not defaultable."
    ),
    "digits": _(
        "An integer specifying how many significant digits should be retained when converting the value of the scale to a string."
    ),
    "direction": _(
        "Specifies where the menu is to be popped up relative to the menubutton."
    ),
    "disabledbackground": _(
        "Specifies the background color to use when the widget is disabled."
    ),
    "disabledforeground": _(
        "Specifies foreground color to use when drawing a disabled element."
    ),
    "elementborderwidth": _(
        "Specifies the width of borders drawn around the internal elements of the scrollbar (the two arrows and the slider)."
    ),
    "endline": _(
        "Specifies an integer line index representing the line of the underlying textual data store that should be just after the last line contained in the widget. This allows a text widget to reflect only a portion of a larger piece of text."
    ),
    "exportselection": _(
        "Specifies whether or not a selection in the widget should be linked to the X selection."
    ),
    "font": _("Specifies the font to use when drawing text inside the widget."),
    "foreground-tk": _(
        "Specifies the normal foreground color to use when displaying the widget."
    ),
    "foreground-ttk": _(
        "The widget's foreground color. If unspecified, the theme default is used."
    ),
    "format": _(
        "Specifies an alternate format to use when setting the string value when using the from and to range. This must be a format specifier of the form %<pad>.<pad>f, as it will format a floating-point number."
    ),
    "from_": _(
        "A floating-point value specifying the lowest value for the widget."
    ),
    "handlepad": _(
        "When sash handles are drawn, specifies the distance from the top or left end of the sash (depending on the orientation of the widget) at which to draw the handle."
    ),
    "handlesize": _(
        "Specifies the side length of a sash handle. Handles are always drawn as squares."
    ),
    "heading_anchor": _("Specifies how the heading text should be aligned."),
    "height": _("Specifies the desired height for the widget."),
    "height-tk.Button": _(
        "Specifies a desired height for the button. If an image or bitmap is being displayed in the button then the value is in screen units; for text it is in lines of text."
    ),
    "height-tk.Text": _(
        "Specifies the desired height for the window, in units of characters in the font given by the font option."
    ),
    "height-tk.Menubutton": _(
        "Specifies a desired height for the menubutton. If an image or bitmap is being displayed in the menubutton then the value is in screen units; for text it is in lines of text."
    ),
    "height-ttk.Treeview": _(
        "Specifies the number of rows which should be visible."
    ),
    "height-ttk.Combobox": _(
        "Specifies the height of the pop-down listbox, in rows."
    ),
    "hidemargin": _(
        "Specifies whether the standard margins should be drawn for this menu entry. This is useful when creating palette with images in them."
    ),
    "highlightbackground": _(
        "Specifies the color to display in the traversal highlight region when the widget does not have the input focus."
    ),
    "highlightcolor": _(
        "Specifies the color to use for the traversal highlight rectangle that is drawn around the widget when it has the input focus."
    ),
    "highlightthickness": _(
        "Specifies a non-negative value indicating the width of the highlight rectangle to draw around the outside of the widget when it has the input focus."
    ),
    "image-tk": _("Specifies an image to display in the widget"),
    "image-ttk": _(
        "Specifies an image to display. This is a list of 1 or more elements. The first element is the default image name."
    ),
    "image-ttk.Treeview.Column": _(
        "Specifies an image to display to the right of the column heading."
    ),
    "inactiveselectbackground": _(
        "Specifies the colour to use for the selection (the sel tag) when the window does not have the input focus."
    ),
    "increment": _("A floating-point value specifying the increment."),
    "indicatoron": _("Specifies whether or not the indicator should be drawn."),
    "insertbackground": _(
        "Specifies the color to use as background in the area covered by the insertion cursor."
    ),
    "insertborderwidth": _(
        "Specifies a non-negative value indicating the width of the 3-D border to draw around the insertion cursor."
    ),
    "insertofftime": _(
        "Specifies a non-negative integer value indicating the number of milliseconds the insertion cursor should remain “off” in each blink cycle."
    ),
    "insertontime": _(
        "Specifies a non-negative integer value indicating the number of milliseconds the insertion cursor should remain “on” in each blink cycle."
    ),
    "insertunfocussed": _(
        "Specifies how to display the insertion cursor when the widget does not have the focus."
    ),
    "insertwidth": _(
        "Specifies a value indicating the total width of the insertion cursor."
    ),
    "invalidcommand": None,
    "jump": _(
        "For widgets with a slider that can be dragged to adjust a value, such as scrollbars, this option determines when notifications are made about changes in the value.If the value is false, updates are made continuously as the slider is dragged. If the value is true, updates are delayed until the mouse button is released to end the drag; at that point a single notification is made."
    ),
    "justify": _(
        "If there are multiple lines of text, specifies how the lines are laid out relative to one another."
    ),
    "justify-ttk.Entry": _(
        "Specifies how the text is aligned within the entry widget."
    ),
    "label": _("A string to display as a label for the scale."),
    "labelanchor": _(
        "Specifies where to place the label. The default value is theme-dependent."
    ),
    "length": _(
        "Specifies the desired long dimension of the scale in screen units."
    ),
    "listvariable": _(
        "A variable name to be used as source of items for the Listbox"
    ),
    "maximum": _(
        "A floating point number specifying the maximum value. Defaults to 100."
    ),
    "maxundo": _(
        "Specifies the maximum number of compound undo actions on the undo stack. A zero or a negative value imply an unlimited undo stack."
    ),
    "minsize": _(
        "Specifies that the size of the window cannot be made less than n. This constraint only affects the size of the widget in the paned dimension"
    ),
    "minwidth": _(
        "The minimum width of the column in pixels. The treeview widget will not make the column any smaller than minwidth when the widget is resized or the user drags a column separator."
    ),
    "mode": None,
    "offrelief": _(
        "Specifies the relief for the checkbutton when the indicator is not drawn and the checkbutton is off. The default value is “raised”."
    ),
    "offvalue": _(
        "The value to store in the associated variable when the widget is deselected. Defaults to 0."
    ),
    "onvalue": _(
        "The value to store in the associated variable when the widget is selected. Defaults to 1."
    ),
    "opaqueresize": _(
        "Specifies whether panes should be resized as a sash is moved (true), or if resizing should be deferred until the sash is placed (false). In the latter case, a “ghost” version of the sash is displayed during the resizing to show where the panes will be resized to when releasing the mouse button. This “ghost” version of the sash is the proxy."
    ),
    "orient": _(
        "For widgets that can lay themselves out with either a horizontal or vertical orientation, this option specifies which orientation should be used."
    ),
    "overrelief": _(
        "Specifies an alternative relief for the button, to be used when the mouse cursor is over the widget."
    ),
    "padding": _(
        "Specifies the internal padding for the widget. The padding is a list of up to four length specifications left top right bottom."
    ),
    "padx": _(
        "Specifies a non-negative value indicating how much extra space to request for the widget in the X-direction."
    ),
    "pady": _(
        "Specifies a non-negative value indicating how much extra space to request for the widget in the Y-direction."
    ),
    "placeholder": _(
        "Specifies a help text string to display if no text is otherwise displayed, that is when the widget is empty."
    ),
    "placeholderforeground": _(
        "Specifies the foreground color of the placeholder text."
    ),
    "postcommand": _(
        "In pygubu-designer, a python function name used as the callback for the widget postcommand property. The function is executed immediately before displaying the listbox. The postcommand callback may specify the values to display."
    ),
    "proxybackground": _("Background color to use when drawing the proxy."),
    "proxyborderwidth": _("Specifies the borderwidth of the proxy."),
    "proxyrelief": _(
        "Relief to use when drawing the proxy. May be any of the standard Tk relief values."
    ),
    "readonlybackground": _(
        "Specifies the background color to use when the entry is readonly."
    ),
    "relief": _("Specifies the 3-D effect desired for the widget border."),
    "repeatdelay": _(
        "Specifies the number of milliseconds a button or key must be held down before it begins to auto-repeat."
    ),
    "repeatinterval": _(
        "Used in conjunction with repeatdelay: once auto-repeat begins, this option determines the number of milliseconds between auto-repeats."
    ),
    "resolution": _("A real value specifying the resolution for the scale."),
    "sliderlength": _(
        "Specifies the size of the slider, measured in screen units along the slider's long dimension."
    ),
    "sliderrelief": _("Specifies the relief to use when drawing the slider."),
    "sashcursor": _("Mouse cursor to use when over a sash."),
    "sashpad": _(
        "Specifies the amount of padding to leave of each side of a sash."
    ),
    "sashrelief": _("Relief to use when drawing a sash."),
    "sashwidth": _("Specifies the width of each sash."),
    "selectbackground": _(
        "Specifies the background color to use when displaying selected items."
    ),
    "selectborderwidth": _(
        "Specifies a non-negative value indicating the width of the 3-D border to draw around selected items."
    ),
    "selectforeground": _(
        "Specifies the foreground color to use when displaying selected items."
    ),
    "scrollregion": _(
        "Specifies a list with four coordinates describing the left, top, right, and bottom coordinates of a rectangular region."
    ),
    "selectcolor": _(
        "Specifies a background color to use when the button is selected."
    ),
    "selectimage": _(
        "Specifies an image to display (in place of the image option) when the checkbutton is selected. This option is ignored unless the image option has been specified."
    ),
    "selectmode": _(
        "Controls how the built-in class bindings manage the selection."
    ),
    "setgrid": _(
        "Specifies a boolean value that determines whether this widget controls the resizing grid for its top-level window."
    ),
    "show": _(
        "If this option is specified, then the true contents of the entry are not displayed in the window. Instead, each character in the entry's value will be displayed as the first character in the value of this option."
    ),
    "show-ttk.Treeview": _("Specifies which elements of the tree to display."),
    "showhandle": _("Specifies whether sash handles should be shown."),
    "showvalue": _(
        "Specifies a boolean value indicating whether or not the current value of the scale is to be displayed."
    ),
    "spacing1": _(
        "Requests additional space above each text line in the widget, using any of the standard forms for screen distances.  If a line wraps, this option only applies to the first line on the display."
    ),
    "spacing2": _(
        "For lines that wrap (so that they cover more than one line on the display) this option specifies additional space to provide between the display lines that represent a single line of text."
    ),
    "spacing3": _(
        "Requests additional space below each text line in the widget, using any of the standard forms for screen distances. If a line wraps, this option only applies to the last line on the display."
    ),
    "startline": _(
        "Specifies an integer line index representing the first line of the underlying textual data store that should be contained in the widget. This allows a text widget to reflect only a portion of a larger piece of text."
    ),
    "state": _(
        "May be set to normal or disabled to control the disabled state bit."
    ),
    "state-tk.Checkbutton": _(
        "Specifies one of three states for the checkbutton: normal, active, or disabled."
    ),
    "state-tk.Canvas": _(
        "Modifies the default state of the canvas where state may be set to one of: normal, disabled, or hidden. Individual canvas objects all have their own state option which may override the default state."
    ),
    "sticky": _(
        "Specifies how the content window is positioned within the pane area."
    ),
    "stretch": _("Controls how extra space is allocated to each of the panes."),
    "stretch-ttk.Treeview": _(
        "Specifies whether or not the column width should be adjusted when the widget is resized or the user drags a column separator."
    ),
    "style": _("May be used to specify a custom widget style."),
    "tabs": _(
        "Specifies a set of tab stops for the window. The option's value consists of a list of screen distances giving the positions of the tab stops, each of which is a distance relative to the left edge of the widget (excluding borders, padding, etc)."
    ),
    "tabstyle": _(
        "Specifies how to interpret the relationship between tab stops on a line and tabs in the text of that line."
    ),
    "takefocus": _(
        "Determines whether the window accepts the focus during keyboard traversal."
    ),
    "tearoff": _(
        "Specifies whether or not the menu should include a tear-off entry at the top."
    ),
    "tearoffcommand": _(
        "Specifies a function callback to invoke whenever the menu is torn off."
    ),
    "text": _("Specifies a text string to be displayed inside the widget."),
    "textvariable": _(
        "Specifies the name of a variable whose value will be used in place of the text resource."
    ),
    "tile": _("This specifies how to draw the background image on the frame."),
    "tickinterval": _(
        "Must be a real value. Determines the spacing between numerical tick marks displayed below or to the left of the slider."
    ),
    "title-menu": "The string will be used to title the window created when this menu is torn off. If the title is NULL, then the window will have the title of the menubutton or the text of the cascade item from which this menu was invoked.",
    "to": _(
        "A floating-point value specifying the highest permissible value for the widget."
    ),
    "tristateimage": _(
        "Specifies an image to display (in place of the image option) when the checkbutton is in tri-state mode. This option is ignored unless the image option has been specified."
    ),
    "tristatevalue": _(
        "Specifies the value that causes the checkbutton to display the multi-value selection, also known as the tri-state mode. Defaults to “”."
    ),
    "troughcolor": _(
        "Specifies the color to use for the rectangular trough areas in widgets such as scrollbars and scales."
    ),
    "underline": _(
        "Specifies the integer index (0-based) of a character to underline in the text string."
    ),
    "undo": _(
        "Specifies a boolean that says whether the undo mechanism is active or not."
    ),
    "value": _("Specifies the current value of the widget."),
    "values": _(
        'Specifies the list of values to display in the drop-down listbox. In code you can pass any iterable. In Designer, a space separated list: value1 value2 "long value3"'
    ),
    "values-tk.OptionMenu": _(
        "Specifies the list of values to display in the menu. In code you can pass any iterable. In Designer, a coma separated list: value1,value2,long value3"
    ),
    "values-tk.Spinbox": _(
        "Must be a proper list value. If specified, the spinbox will use these values as to control its contents, starting with the first value. This option has precedence over the from and to range."
    ),
    "validate": _("Specifies the mode in which validation should operate."),
    "validatecommand": None,
    "variable": _(
        "The name of a variable whose value is linked to the widget."
    ),
    "weight": _(
        "An integer specifying the relative stretchability of the pane. When the paned window is resized, the extra space is added or subtracted to each pane proportionally to its weight."
    ),
    "width": _("Specifies the desired width for the widget."),
    "width-tk": _(
        "Specifies a desired width for the label. If an image or bitmap is being displayed in the label then the value is in screen units; for text it is in characters."
    ),
    "width-ttk": _(
        "If greater than zero, specifies how much space, in character widths, to allocate for the text label. If less than zero, specifies a minimum width."
    ),
    "width-tk.Label": _(
        "Specifies a desired width for the label. If an image or bitmap is being displayed in the label then the value is in screen units; for text it is in characters."
    ),
    "width-tk.Button": _(
        "Specifies a desired width for the button. If an image or bitmap is being displayed in the button then the value is in screen units. For a text button (no image or with compound none) then the width specifies how much space in characters to allocate for the text label. If the width is negative then this specifies a minimum width."
    ),
    "width-tk.Entry": _(
        "Specifies an integer value indicating the desired width of the entry window, in average-size characters of the widget's font."
    ),
    "width-tk.Spinbox": _(
        "Specifies an integer value indicating the desired width of the spinbox window, in average-size characters of the widget's font. If the value is less than or equal to zero, the widget picks a size just large enough to hold its current text."
    ),
    "width-tk.Message": _(
        "Specifies a dimension value (pixels) for the length of lines in the window. If this option has a value greater than zero then the aspect option is ignored and the width option determines the line length. If this option has a value less than or equal to zero, then the aspect option determines the line length."
    ),
    "width-tk.Menubutton": _(
        "Specifies a desired width for the menubutton. If an image or bitmap is being displayed in the menubutton then the value is in screen units; for text it is in characters. If this option is not specified, the menubutton's desired width is computed from the size of the image or bitmap or text being displayed in it."
    ),
    "width-tk.Text": _(
        "Specifies the desired width for the window in units of characters in the font given by the font option."
    ),
    "width-ttk.Label": _(
        "If greater than zero, specifies how much space, in character widths, to allocate for the text label. If less than zero, specifies a minimum width."
    ),
    "width-tk.Scrollbar": _(
        "Specifies the desired narrow dimension of the scrollbar window, not including 3-D border, if any. For vertical scrollbars this will be the width and for horizontal scrollbars this will be the height."
    ),
    "width-scale": _(
        "Specifies the desired narrow dimension of the scale in screen units.  For vertical scales this is the scale's width; for horizontal scales this is the scale's height."
    ),
    "width-ttk.Treeview.Column": _(
        "The width of the column in pixels. Default is 200 pixels."
    ),
    "wrap-ttk.Spinbox": _(
        "If on, the spinbox will wrap around the values of data in the widget."
    ),
    "wrap-tk.Text": _(
        "Specifies how to handle lines in the text that are too long to be displayed in a single line of the text's window."
    ),
    "wraplength": _("Specifies the maximum line length (in pixels)."),
    "xscrollcommand": None,
    "xscrollincrement": _(
        "Specifies an increment for horizontal scrolling, in any of the usual forms permitted for screen distances."
    ),
    "yscrollcommand": None,
    "yscrollincrement": _(
        "Specifies an increment for vertical scrolling, in any of the usual forms permitted for screen distances."
    ),
    #
    # Custom properties
    "geometry-custom": _(
        "Set the window geometry. Allowed string format: 'wxh'"
    ),
    "maxsize-toplevel": _("Set the maximum window size."),
    "minsize-toplevel": _("Set the minimum window size."),
    "overrideredirect-custom": _(
        "Sets the override redirect flag. If True, removes all window manager decorations from the window, so that it cannot be moved, resized, iconified, or closed."
    ),
    "title-toplevel": _("Sets the window title."),
    "tree_column-custom": _("If True, set this column as the tree column #0"),
    "visible-custom": _(
        "Determines whether or not the column is included in the displaycolumns list."
    ),
    "resizable-custom": _("Determines if the window can be resized."),
    "iconbitmap-custom": _("Sets bitmap for the iconified widget."),
    "iconphoto-custom": _("Sets the titlebar icon for this window."),
    "scrolltype-custom": _("Determines scroll type for the widget."),
    "usermosewheel": _("Enable scrolling using mousewheel"),
    #
    # Layout properties
    #
    "padx-layout": _(
        "Specifies how much horizontal external padding to leave on each side of the content."
    ),
    "pady-layout": _(
        "Specifies how much vertical external padding to leave on each side of the content."
    ),
    "ipadx-layout": _(
        "Specifies how much horizontal internal padding to leave on each side of the content."
    ),
    "ipady-layout": _(
        "Specifies how much vertical internal padding to leave on each side of the content."
    ),
    "propagate-layout": _("Enable/Disable Geometry Propagation"),
    "anchor-layout": _(
        "It specifies where to position each content in its parcel."
    ),
    "anchor-layout-place": _(
        "Specifies which point of window is to be positioned at the (x,y) location selected by the x, y, relx, and rely options."
    ),
    # pack properties
    "expand-pack": _(
        "Specifies whether the content should be expanded to consume extra space in their container."
    ),
    "fill-pack": _(
        "If a content's parcel is larger than its requested dimensions, this option may be used to stretch the content."
    ),
    "side-pack": _(
        "Specifies which side of the container the content will be packed against."
    ),
    "bordermode-pack": _(
        "Determines the degree to which borders within the container are used in determining the placement of the content."
    ),
    "height-place": _("Specifies the height for window in screen units"),
    "relheight-place": _(
        "Specifies the height for window. In this case the height is specified as a floating-point number relative to the height of the container: 0.5 means window will be half as high as the container, 1.0 means window will have the same height as the container, and so on. If both height and relheight are specified for a content, their values are summed."
    ),
    "relwidth-place": _(
        "Specifies the width for window. In this case the width is specified as a floating-point number relative to the width of the container: 0.5 means window will be half as wide as the container, 1.0 means window will have the same width as the container, and so on. If both width and relwidth are specified for a content, their values are summed."
    ),
    "relx-place": _(
        "Specifies the x-coordinate within the container window of the anchor point for window. In this case the location is specified in a relative fashion as a floating-point number: 0.0 corresponds to the left edge of the container and 1.0 corresponds to the right edge of the container."
    ),
    "rely-place": _(
        "Specifies the y-coordinate within the container window of the anchor point for window. In this case the value is specified in a relative fashion as a floating-point number: 0.0 corresponds to the top edge of the container and 1.0 corresponds to the bottom edge of the container."
    ),
    "width-place": _("Specifies the width for window in screen units."),
    "x-place": _(
        "Specifies the x-coordinate within the container window of the anchor point for window."
    ),
    "y-place": _(
        "Specifies the y-coordinate within the container window of the anchor point for window."
    ),
    #
    # grid packing properties
    "row-grid": _(
        "Insert the content so that it occupies the nth row in the grid."
    ),
    "column-grid": _(
        "Insert the window so that it occupies the nth column in the grid."
    ),
    "sticky-grid": _(
        "If a content's cell is larger than its requested dimensions, this option may be used to position (or stretch) the content within its cell."
    ),
    "rowspan-grid": _(
        "Insert the content so that it occupies n rows in the grid."
    ),
    "columnspan-grid": _(
        "Insert the window so that it occupies n columns in the grid."
    ),
    #
    # grid row and column properties (can be applied to each row or column)
    "minsize-grid": _(
        "Sets the minimum size, in screen units, that will be permitted for this row."
    ),
    "pad-grid": _(
        "Specifies the number of screen units that will be added to the largest window contained completely in that row when the grid geometry manager requests a size from the containing window."
    ),
    "weight-grid": _(
        "Sets the relative weight for apportioning any extra spaces among rows."
    ),
    "uniform-grid": _(
        "When a non-empty value is supplied, places the row in a uniform group with other rows that have the same value for uniform."
    ),
}


def help_for(pname):
    return tooltip_help[pname]
