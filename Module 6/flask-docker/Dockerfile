# step 1 - mention the base operating system
FROM python3.7:latest


# creating a worksing directory with the name "app"
WORKDIR /app
# copying the files of current folder to the app folder inside the container
COPY . /app
#install the libraries and packages
RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["webapp.py"]

