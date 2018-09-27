# Real Estate Site


This site is real estate site

# How to deploy on localhost
```bash
$ pip install -r requirements.txt
```
To init DB use 
```
(venv) $ flask db init
```
To upgrade DB description use
```
(venv) $ flask db upgrade
```
Export environment variable


```bash
$ export FLASK_APP=server.py
$ export SECRET_KEY='your secret key'
```

To fill db use:
```bash
$ python3 apply_data.py --path ads.json
```
For dedug mode use variable FLASK_DEBUG=1
```
$export FLASK_DEBUG=1
$ flask run
```

Then open the page [localhost:5000](http://localhost:5000) in browser.
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
