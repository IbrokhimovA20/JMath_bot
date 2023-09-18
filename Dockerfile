FROM python:3.8.7-slim

# set work directory
WORKDIR /jmath_bot

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN chown -R node /app/node_modules

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["python", "jmath.py"]