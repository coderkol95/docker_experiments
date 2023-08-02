FROM python:3.8
COPY . .
RUN pip install -r requirements.txt
RUN python3 src/data.py
RUN python3 src/train.py
EXPOSE 5001
CMD flask run