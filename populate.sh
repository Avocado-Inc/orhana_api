#!/bin/bash


source env/bin/activate
python manage.py migrate

./manage.py shell < scripts/populate_category_sub_category.py
