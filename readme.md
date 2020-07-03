# Project Title

Invoice manager on Django

## Note:

The project is made strictly as per the guidelines and each and every functionality is fulfilled.

## Getting Started

Note: Instead of deploying the app to cloud, the dockerized version of this django-app is created so that it can be easily scaled.

The web-app and database is containerized or micro-serviced for scalability.

You can find dockerized version in 'finalone-dockerized'.

### Prerequisites for dockerized

What things you need to install 

```
# install docker
# install docker-compose
# pull the dockerized version
```

```
# And finally run

docker-compose up
```

### Prerequisites for normal

If you want to check non-dockerized version, simply run django-app in conventional method.

First

```
pip install -r requirements.txt

```
then

```
python manage.py runserver

```

## Understanding the work-flow

This is workflow of our system.

![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)


## Answers to the assigment questions:

1) Minimum CPU/Memory/Storage requirements.

```
CPU: cpu requirement will be least as this app is simple and in a sense,primitive,as no heavy lifting is going on.

Memory: This app will require memory for storing the pdf files. Locally it is hosted on directory,on cloud,it can be stored on storage services like AWS S3 which are little-to-one cost.

```

2) Potential Security Threats.

```
Other than token authentication, no severe threats are there.
Even if one is successful to get token,token will expire soon.
And also,manager cannot delete the invoice only agent can.

For more robust security,the manager can access through link only.

```

3) How many agents can handle system at a time.

```
If we are using the conventional cloud hosted system without a load balancer and scaling system,
the app might be slow as it is intensive CRUD oriented.

But if we host the dockerized version on cluster,
it is practically infinite scaling.

Thus,every person on earth can access the system and work with it seamlessly.

Only problem is it will be costly.
```
## Built With

* Docker
* Django
* Postgresql

## note:

The dockerized version is not hosted on cluster as it is costly.

## Contributing

Shivam Patel