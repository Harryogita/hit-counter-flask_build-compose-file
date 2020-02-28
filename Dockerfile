FROM python:latest
WORKDIR /mycode
COPY . /mycode
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN pip install -r requirements.txt
CMD ["flask", "run"]
