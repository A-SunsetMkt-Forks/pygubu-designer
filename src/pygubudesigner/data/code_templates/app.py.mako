<%inherit file="base.py.mako"/>
<%block name="project_paths" filter="trim">
PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "${project_name}"
</%block>

<%block name="class_definition" filter="trim">
class ${class_name}:
%if with_i18n_support and has_ttk_styles:
    def __init__(self, master=None, translator=None):
        self.builder = builder = pygubu.Builder(
            translator=translator,
            on_first_object=${ttk_styles_module}.setup_ttk_styles)
%elif with_i18n_support:
    def __init__(self, master=None, translator=None):
        self.builder = builder = pygubu.Builder(translator)
%elif has_ttk_styles:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder(
            on_first_object=${ttk_styles_module}.setup_ttk_styles)
%else:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
%endif
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow:${widget_base_class} = builder.get_object("${main_widget}", master)
%if set_main_menu:
        # Main menu
        _main_menu = builder.get_object("${main_menu_id}", self.mainwindow)
        self.mainwindow.configure(menu=_main_menu)
%endif
    %if tkvariables:

        %for var in tkvariables:
        self.${var}:${tkvariablehints[var]} = None
        %endfor
        builder.import_variables(self)

    %endif
        builder.connect_callbacks(self)

    def center(self, event):
        """ `winfo_width` / `winfo_height` at this point return set `geometry` size. """
        x_min = max(self.main_w,
            self.mainwindow.wm_minsize()[0],
            self.mainwindow.winfo_width(),
            self.mainwindow.winfo_reqwidth())
        y_min = max(self.main_h,
            self.mainwindow.wm_minsize()[1],
            self.mainwindow.winfo_height(),
            self.mainwindow.winfo_reqheight())
        x = self.mainwindow.winfo_screenwidth() - x_min
        y = self.mainwindow.winfo_screenheight() - y_min
        self.mainwindow.geometry(f"{x_min}x{y_min}+{x // 2}+{y // 2}")
        self.mainwindow.unbind("<Map>", self.center_map)

    def run(self, center=False):
        if center:
            """ If `width` and `height` are set for the main widget,
            this is the only time TK returns them. """
            self.main_w = self.mainwindow.winfo_reqwidth()
            self.main_h = self.mainwindow.winfo_reqheight()
            self.center_map = self.mainwindow.bind("<Map>", self.center)
        self.mainwindow.mainloop()

${callbacks}\
</%block>
