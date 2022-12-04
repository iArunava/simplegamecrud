# Game CRUD

 Simple example python flask crud app for storing games.
 
# Screenshots


![image](screenshots.png)  
 
 
# Get Started

```
git clone https://github.com/iarunava/simplegamecrud.git
cd example-flask-crud/
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
export FLASK_APP=gamecrud.py
flask db init
flask db migrate -m "game table"
flask db upgrade
flask run
```
