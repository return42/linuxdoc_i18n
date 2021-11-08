# Install steps

    python3 -m venv .venv
    source .venv/bin/activate
    pip install pip wheel setuptools
    pip install -r requirements.txt

    # create POT locales/index.pot
    sphinx-build -M gettext -d "build/doctrees" source source/locales

    # create fr translation in locales/fr/LC_MESSAGES/index.po
    sphinx-intl update -l fr -d source/locales -p source/locales

    # now edit translations in (see below)
    # ...

    # and build (fr) HTML
    make -e SPHINXOPTS="-v -D language='fr'" html

    # open HTML in the browser
    xdg-open build/html/index.html

    # build (en) HTML and reload page in the browser
    make -e SPHINXOPTS="-v -D language='en'" html

# Uninstall steps

    deactivate
    rm -rf .venv build source/locales

# Translate fr

```diff
diff --git a/source/locales/fr/LC_MESSAGES/index.po b/source/locales/fr/LC_MESSAGES/index.po
index a90c243..4499529 100644
--- a/source/locales/fr/LC_MESSAGES/index.po
+++ b/source/locales/fr/LC_MESSAGES/index.po
@@ -64,7 +64,7 @@ msgstr ""
 
 #: ../index.rst:21
 msgid ":rspan:`1` :cspan:`1` field 2.2 - 3.3"
-msgstr ""
+msgstr "test (fr) field 2.2 - 3.3"
 
 #: ../index.rst:25
 msgid "column 3"
@@ -116,5 +116,5 @@ msgstr ""
 
 #: ../index.rst:48
 msgid ":math:`a^2 + b^2 = c^2`"
-msgstr ""
+msgstr "test (fr) :math:`a^2 + b^2 = c^2`"
```
