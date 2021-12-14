# /usr/bin/bash
set -e
OLD_PWD=$PWD
cd `dirname $0`

unittest(){
    pipenv run python -m unittest discover -s ./tests/ -t .
}

coverage(){
    pipenv run coverage run -m unittest discover -s ./tests/ -t .
    pipenv run coverage xml
}

coverage

cd $OLD_PWD