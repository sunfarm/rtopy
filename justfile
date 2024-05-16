
install:
    Rscript -e "install.packages('readr', repos='http://cran.rstudio.com/')"

run:
    pipenv run python cli.py inputs
    rscript script.r
    pipenv run python script.py
    pipenv run python cli.py compare