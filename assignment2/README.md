# Assignment 1
Ran using Python 3.10.9

See `requirements.txt` for required modules. To install all the requirements, run

```sh
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## RESTful API and Flask webserver
Start the API and webserver with this command:
```sh
python server.py
```

Access the API with
```sh
curl http://127.0.0.1:5000/api
```
for a GET request and

```sh
curl -H "Content-Type: text/plain" -X POST -d@input.txt http://127.0.0.1:5000/api
```
for a POST request.

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) for the webserver.

## Streamlit application
Start the application with this command:
```sh
streamlit run visual.py
```
Visit [http://localhost:8501](http://localhost:8501) for the application.
