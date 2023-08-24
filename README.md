# opensafely_template

https://docs.opensafely.org/getting-started
   opensafely
   opensafely run run_all
   opensafely run run_all --force-run-dependencies
   opensafely unzip output
# opensafely run generate_study_population
# opensafely run describe
# retrieve each codelist listed in /codelists/codelists.txt from OpenCodelists. It will add (or update) the codelist .csv files to the codelists/ folder.
opensafely codelists update
# check if the codelist files are up-to-date with those listed in ./codelists/codelists.txt.
# If you have error messages about missing libraries, your Docker images may need upgrading. To pull the most recent Docker images to your machine, run:
opensafely pull

# launch the version of R packaged in the r docker image, and your files can be executed (we need to specify the command as R as the default is to run Rscript, which is non-interactive
opensafely exec r R
opensafely exec python ipython

# clean up any dangling images, containers and volumes
# https://docs.opensafely.org/opensafely-cli/#disk
opensafely clean




You can run this project via [Gitpod](https://gitpod.io) in a web browser by clicking on this badge: [![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-908a85?logo=gitpod)](https://gitpod.io/#https://github.com/JohnGavin/opensafely_template)

[View on OpenSAFELY](https://jobs.opensafely.org/repo/https%253A%252F%252Fgithub.com%252Fopensafely%252Fopensafely_template)

Details of the purpose and any published outputs from this project can be found at the link above.

The contents of this repository MUST NOT be considered an accurate or valid representation of the study or its purpose. 
This repository may reflect an incomplete or incorrect analysis with no further ongoing work.
The content has ONLY been made public to support the OpenSAFELY [open science and transparency principles](https://www.opensafely.org/about/#contributing-to-best-practice-around-open-science) and to support the sharing of re-usable code for other subsequent users.
No clinical, policy or safety conclusions must be drawn from the contents of this repository.

# About the OpenSAFELY framework

The OpenSAFELY framework is a Trusted Research Environment (TRE) for electronic
health records research in the NHS, with a focus on public accountability and
research quality.

Read more at [OpenSAFELY.org](https://opensafely.org).

# Licences
As standard, research projects have a MIT license. 
