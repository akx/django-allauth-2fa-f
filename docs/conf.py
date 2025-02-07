# -- General configuration ------------------------------------------------
# Add any Sphinx extension module names here, as strings.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "django-allauth-2fa"
copyright = "2017, Víðir Valberg Guðmundsson, Percipient Networks"
author = "Víðir Valberg Guðmundsson, Percipient Networks"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "0.4.3"
# The full version, including alpha/beta/rc tags.
release = "0.4.3"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------
html_theme = "sphinx_rtd_theme"


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "django-allauth-2fadoc"


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

# Grouping the document tree into LaTeX files.
latex_documents = [
    (
        master_doc,
        "django-allauth-2fa.tex",
        "django-allauth-2fa Documentation",
        "Víðir Valberg Guðmundsson, Percipient Networks",
        "manual",
    ),
]


# -- Options for manual page output ---------------------------------------

man_pages = [
    (master_doc, "django-allauth-2fa", "django-allauth-2fa Documentation", [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    (
        master_doc,
        "django-allauth-2fa",
        "django-allauth-2fa Documentation",
        author,
        "django-allauth-2fa",
        "One line description of project.",
        "Miscellaneous",
    ),
]


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {"https://docs.python.org/": None}
