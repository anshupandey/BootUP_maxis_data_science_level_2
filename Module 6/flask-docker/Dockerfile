# step 1 - mention the base operating system
FROM python:3.7


# creating a worksing directory with the name "app"
WORKDIR /app
# copying the files of current folder to the app folder inside the container
COPY . /app
#install the libraries and packages
RUN pip install -r requirements.txt
RUN ls
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["webapp.py"]

