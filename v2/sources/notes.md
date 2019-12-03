Download a single package:
    pip download -b build/ --src src/ -d downloads/ --cache-dir cache/ --log log.txt cefpython3

    *The downloaded item may be simply installed using pip

        pip install ...whl

Install one file from folder:
    pip install --no-index --find-links=downloads cefpython3


Download installed list.

    pip freeze requirements.txt
    pip install pip download -b build/ --src src/ -d downloads/ --cache-dir cache/ -r requirements.txt
