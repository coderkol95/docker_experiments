FROM python:3.8-slim-buster
COPY . .
RUN pip install -r requirements.txt
RUN python3 src/data.py
RUN python3 src/train.py
CMD python3 -m flask run --host=0.0.0.0