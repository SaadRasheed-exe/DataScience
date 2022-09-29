# Modules
Sometimes, when writing an application, the code can be too long for one file to handle. We would have to scroll up and down alot to review and make changes in alot of places. Python makes code management extremely easy with **modules**. These are simple python files with utility functions and classes that are to be used in our program. The folder structure looks something like...
```
📦App
 ┣ 📜helper.py
 ┗ 📜main.py
```
The *helper.py* script has functions and classes that are to be used in the program, whereas the *main.py* script will have the main worker thread of the program. To use the utilities of helper script, we can simply write...
```python
import helper
```
...at the start of our main script.

# Packages
But when the program is too large and has too many sub-routines, modules are not enough. This is when **packages** come into play. These are, simply put, a collection of modules and sub-packages. Related modules can be placed into the same packages. Folder structure looks something like...
```
📦Model
 ┣ 📂keras
 ┃ ┣ 📜layers.py
 ┃ ┣ 📜losses.py
 ┃ ┣ 📜metrics.py
 ┃ ┗ 📜__init__.py
 ┗ 📜main.py
```
Here, the *keras* folder is the package. The *__init__.py* file is necessary for python to figure out that this folder is a package. To import a specific module from within a package when can write:
```python
from keras import layers
```
This will import everything from the *layers.py* script.
