echo "BUILD START"
python3.9 -m pip install -r requirements.txt
python manage.py collecstatic --noinput --clear
echo "BUIILD END"