FROM python:3.8.7-slim

# set work directory
WORKDIR /jmath

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# CMD ["python", "jmath.py"]
RUN ["chmod", "+x", "./main.sh"]
EXPOSE 1007
CMD ["./main.sh"]