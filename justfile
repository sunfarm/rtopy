
install:
    Rscript -e "install.packages('readr', repos='http://cran.rstudio.com/')"

run:
    rscript script.r
    pipenv run python script.py
    pipenv run python cli.py compare