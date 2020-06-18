source venv/bin/activate
while inotifywait -q -e modify level6.py
do clear;
python3 level6.py
done
