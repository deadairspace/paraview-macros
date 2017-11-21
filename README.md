# paraview-macros
Macros for Paraview. Help preparing 2d maps.

# Installation note
After being added to Paraview (menu macros > add new macro...) and modified using the Paraview macro editor, the macro is not stored to the original file (see https://www.paraview.org/Wiki/Python_GUI_Tools). In order to put chages to git repository, use the "Save as..." command of the paraview macro editor.

Another way to install macros is to define the ``PV_MACRO_PATH`` variable, pointing to the ``macro`` folder of the local repository clone. In this way Paraview will directly refer (use and modify) to the files in the repo.
