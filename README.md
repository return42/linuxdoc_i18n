# Install steps

    python3 -m venv .venv
    source .venv/bin/activate
    pip install pip wheel setuptools
    pip install -r requirements.txt

    # create POT locales/index.pot
    sphinx-build -M gettext -d "build/doctrees" source source/locales

    # create fr translation in locales/fr/LC_MESSAGES/index.po
    sphinx-intl update -l fr -d source/locales -p source/locales

    # now edit translations in (see below) and build html
    make -e SPHINXOPTS="-v -D language='fr'" html

    xdg-open build/html/index.html

# Uninstall steps

    deactivate
    rm -rf .venv build source/locales

# Translate fr

```diff
diff --git a/source/locales/fr/LC_MESSAGES/index.po b/source/locales/fr/LC_MESSAGES/index.po
index 1984d32..4536408 100644
--- a/source/locales/fr/LC_MESSAGES/index.po
+++ b/source/locales/fr/LC_MESSAGES/index.po
@@ -64,7 +64,7 @@ msgstr ""
 
 #: ../index.rst:21
 msgid ":rspan:`1` :cspan:`1` field 2.2 - 3.3"
-msgstr ""
+msgstr "test (fr) field 2.2 - 3.3"
 
 #: ../index.rst:25
 msgid "column 3"
```
