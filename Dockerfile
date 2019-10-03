FROM python:3.7

COPY . /iss-api

WORKDIR /iss-api

RUN python -m pip install pipenv
RUN pipenv install --system

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]