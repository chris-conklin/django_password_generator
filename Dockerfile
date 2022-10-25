FROM python:3

#Set the working directory
WORKDIR /opt/app-home

#copy all the files
COPY . .

RUN pip --disable-pip-version-check install -r requirements.txt
#Expose the required port
EXPOSE 8000

#Run the command
CMD ["python3", "manage.py", "runserver"]
