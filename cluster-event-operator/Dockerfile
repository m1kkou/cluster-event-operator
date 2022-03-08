FROM python:3.9.6-alpine3.13 as dev

WORKDIR /work

COPY /src/requirements.txt /work/
RUN pip install -r /work/requirements.txt 

# FROM dev as runtime

# WORKDIR /app
# COPY /src/requirements.txt /app/
# RUN pip install -r /app/requirements.txt 

# COPY /src/app.py /app/app.py
# COPY /data/data.txt /app/data/data.txt

# RUN touch /app/data/data.txt

# ENV FLASK_APP=app.py 
# ENV PORT=5000

# ENTRYPOINT [ "flask", "run", "-h", "0.0.0", "-p", "5000" ]