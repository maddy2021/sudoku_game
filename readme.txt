######################################################################################## Requirement : Python version > 3 , Internet to load cdn

1. Clone/download the project: git clone

2. Go to the folder directory where requirement.txt present and run following command in cmd.
> pip install -r requirement.txt

3.After installing requirement run following command in cmd.

3.1 Windows machine(For productuion use production)
> set FLASK_APP=sudoku-app
> set FLASK_ENV=development
> flask init-db
> flask run

3.2 Linux machine
> export FLASK_APP=sudoku-app
> export FLASK_ENV=development
> flask init-db
> flask run

4. Go the the Url and you are good to go with sudoku