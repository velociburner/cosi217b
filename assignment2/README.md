# Assignment 2
Ran using Python 3.10.9

See `requirements.txt` for required modules. To install all the requirements, run

```sh
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Flask webserver
Start the webserver with this command:
```sh
python server.py
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) for the webserver.

## Docker container
Build the Docker image with this command:
```sh
docker build -t ner-server .
```

Run the container with this command:
```sh
docker run --rm -p 5000:5000 -v $PWD/instance:/app/instance ner-server
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) on the host machine to access the webserver running in the container.
