# Install steps

    pip install -r requirements.txt
    make gettext
    sphinx-intl update --language=fr
    make -e SPHINXOPTS="-D language='fr'" html
