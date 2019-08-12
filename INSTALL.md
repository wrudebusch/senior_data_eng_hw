William Rudebusch 
Aug 12, 2019

# Install Steps

## Git
Step 1: have git setup, then in a new folder use
git clone https://github.com/Hinge/senior_data_eng_hw.git

## Docker
Step 2: install Docker and stop postgres if its running 
sudo service postgresql stop

Step 3: While in the same path of Dockerfile: 
`sudo docker build -t postgresdocker:11 .`
Note: the -t option is a tag, so maybe call it something relevant to the image you're making

Step 4: run the Docker image and make a containe:
In our case, we don't need a postgres username+password to be set, so we do this:
`sudo docker run -d -p 5432:5432 --name my-postgres postgresdocker:11`

Step 5: And then we connect to the container
`sudo docker exec -it my-postgres bash`

Step 6: (testing, you can skip this) while inside the container, we connect to the Postgres server using psql:
`psql -U postgres`

Step 7: (testing, you can skip this) list databases 
```\l 
\q
```

Step 8: (testing, you can skip this) in a diff terminal connect to postgres and see that if its ok:
```psql -h localhost -p 5432 -U postgres -W  
\l
```

## Python

Step 9: innstall pandas, psycopg2, and sqlalchamey if you don't already have them
`python3 -m pip install --user pandas sqlalchemy psycopg2`

Step 10: run the script I wrote
`python3 csv_to_postgres.py`

## SQL
Step 11: test to see if if worked:
```psql -h localhost -p 5432 -U postgres -W
\c postgres
\dt
```

Have fun using SQL!