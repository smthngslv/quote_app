# Quote Web App

Team: Ivan Izmailov, Alexey Rakov \
Project chosen: A single screen web app to display a quote on clicking a “Get Quote” button

## 1) What purpose of this app?

If you need some quote for inspiration, you can use this app. Just click the button and get some random quote from our database.


## 2) Requirements
* [Python 3](https://python.org) (**Python 3.9** preffered)
* Python PIP
* Python Venv
* Any browser

## 3) Installation

1) Clone source code:
~~~
$ git clone https://github.com/smthngslv/quote_app.git
~~~

2) Go to the folder with source code:
~~~
$ cd <Path>
~~~
3) Set virtual environment and activate it:
~~~
$ python -m venv env
$ source env/bin/activate
~~~
4) Install requirements:
~~~
$ pip install -r requirements.txt
~~~
5) Start app by this command:
~~~
$ uvicorn qoute:app
~~~

### 4) Using of app

1) Click button "Get Quote"
2) Get inspiration from quote!
