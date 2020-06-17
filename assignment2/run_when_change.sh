source venv/bin/activate
while inotifywait -q -e modify inject.py
do clear;
python3 inject.py
done
