import os
import sys
sys.path.insert(0, os.path.abspath("../egyptian"))  # Ensure your package can be imported

project = "Egyptian"
author = "Your Name"
release = "0.1"

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon"]

html_theme = "alabaster"
