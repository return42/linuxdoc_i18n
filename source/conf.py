project = 'Test Project'

extensions = [
    'linuxdoc.rstFlatTable', # https://return42.github.io/linuxdoc/linuxdoc-howto/table-markup.html#flat-table
    'linuxdoc.rstKernelDoc',    # Implementation of the 'kernel-doc' reST-directive.
    'linuxdoc.kernel_include',  # Implementation of the 'kernel-include' reST-directive.
    'linuxdoc.manKernelDoc',    # Implementation of the 'kernel-doc-man' builder
    'linuxdoc.cdomain',         # Replacement for the sphinx c-domain.
    'linuxdoc.kfigure',         # Sphinx extension which implements scalable image handling.
]

html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = []

language = 'en'
