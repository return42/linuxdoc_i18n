# Install steps

    python3 -m venv .venv
    source .venv/bin/activate
    pip install pip wheel setuptools
    pip install -r requirements.txt

    # and build (fr) HTML
    make -e SPHINXOPTS="-v -D language='fr'" html

    # open HTML in the browser
    xdg-open build/html/index.html

    # build (en) HTML and reload page in the browser
    make -e SPHINXOPTS="-v -D language='en'" html

# create POT locales/index.pot

    sphinx-build -M gettext -d "build/.doctrees" source source/locales

# create fr translation in locales/fr/LC_MESSAGES/index.po

    sphinx-intl update -l fr -d source/locales -p source/locales

# Uninstall steps

    deactivate
    rm -rf .venv build source/locales

# Translate fr

The ``:rspan:`` and ``:cspan:`` directives are *special* reST-roles.  These directives are used in the ListTableBuilder and [removed](https://github.com/return42/linuxdoc/blob/83274eeb441df8a93b341f12575f87e86313453e/linuxdoc/rstFlatTable.py#L331-L346) while the table is parsed.  These reST-roles must not be in the translation:

    #: ../index.rst:21
    msgid ":rspan:`1` :cspan:`1` field 2.2 - 3.3"
    msgstr "test (fr) field 2.2 - 3.3"

Most other [reStructuredText Interpreted Text Roles](https://docutils.sourceforge.io/docs/ref/rst/roles.html) should be translated *as-is*:

    #: ../index.rst:48
    msgid ":math:`a^2 + b^2 = c^2`"
    msgstr "test (fr) :math:`a^2 + b^2 = c^2`"
