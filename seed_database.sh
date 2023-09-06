rm db.sqlite3
rm -rf ./makeupapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations makeupapi
python3 manage.py migrate makeupapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata makeup_skill
python3 manage.py loaddata profile
python3 manage.py loaddata product_type
python3 manage.py loaddata makeup_prefrences
python3 manage.py loaddata products
python3 manage.py loaddata profile_prefrences 
python3 manage.py loaddata tips
python3 manage.py loaddata wishlist
