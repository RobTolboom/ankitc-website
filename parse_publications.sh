# #!/usr/bin/env bash

set -e

curl -H "Authorization: token ${GH_BIB_TOKEN}" \
    -o content/diag.bib \
    -s \
    -L https://github.com/RobTolboom/ankitc-website/master/content/diag.bib

curl -H "Authorization: token ${GH_BIB_TOKEN}" \
    -o content/fullstrings.bib \
    -s \
    -L https://github.com/RobTolboom/ankitc-website/master/content/fullstrings.bib

python ./bibliography/bibparser.py
