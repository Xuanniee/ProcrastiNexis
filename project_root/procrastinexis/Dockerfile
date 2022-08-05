# Instructions to create a Docker Image for Development of Pomodoro Timer Apps

# Basing our Container on a Standard Image of Python3
FROM python:3
# Setting up Working Directory
COPY . /usr/src/app
WORKDIR /usr/src/app
# Install Requirements for Container
RUN pip install -r requirements.txt
# Command to run server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

