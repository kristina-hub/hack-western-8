# Hack Western 8

## Table of Contents
- [About](#About)
- [Tentative Goals](#Tentative-Goals)
- [Anticipated Impact](#Anticipated-Impact)
- [Possible Action Plan](#Possible-Action-Plan)
- [Steps](#Steps)
- [Deliverables](#Deliverables)
- [Installation](#Installation)
- [Demo](#Demo)
- [Git Reference](#Git-Reference)
- [AWS Reference](#AWS-Reference)

## About
about...

## Tentative Goals
1. 
2. 
3. 

## Anticipated Impact
impact...

## Installation
```shell script
$ pip3 install -r requirements.txt
```

## Demo
Created using: https://ezgif.com/maker<br/><br/>
  ![](./static/img/demo.gif)

## How we used AWS
#### Run a website locally:
```shell script
$ touch application.py

from flask import Flask
application = Flask(__name__)
@application.route('/')
def hello_world():
	return 'Hello World'
	
$ export FLASK_APP="application.py"
$ flask run
```
Now runs locally: http://127.0.0.1:5000/<br/>

#### Link Flask to AWS Elastic Beanstalk: 
https://www.youtube.com/watch?v=4tDjVFbi31o <br/>
AWS -> Services -> Elastic beanstalk <br/>
Create New Application called syllabus-manager using Python <br/>
Create New Environment called syllabus-manager-env using Web Server Environment <br/>

#### Set up continuous deployment with GitHub using AWS Code Pipeline:
Services -> Developer Tools -> CodePipeline <br/>
Create Pipeline called syllabus-manager <br/>
GitHub version 2 -> Connect to Github <br/>
Connection name is connection -> Install a New App -> Choose repo name -> Skip build stage -> Deploy to AWS Elastic Beanstalk <br/>
```shell script
$ git pull
$ git add .
$ git commit -m "comment"
$ git push
```
This link is no longer local: http://hack-western-8-env.eba-a5injkhs.us-east-1.elasticbeanstalk.com/ <br/>

Note that it says "Not Secure" beside the link<br/>

#### Register an AWS Route 53 Domain and SSL/HTTPS: 
https://www.youtube.com/watch?v=BeOKTpFsuvk <br/>
Route 53 -> Registered domains -> Register domain -> hack-western-8.com -> check -> wait for hosted zone to be set up<br/>
Certificate manager -> Request a public certificate -> enter domain name "hack-western-8.com" and "*.hack-western-8.com" -> DNS validation -> Request<br/>

Elastic Beanstalk -> Environments -> hack-western-8-env -> Configuration -> Capacity -> enable load balancing<br/>
Load balancer -> Add listener -> Port 443 -> Protocol HTTPS -> SSL certificate, choose the one that was just made<br/>

Route 53 -> Hosted zones -> hack-western-8.com -> Create record -> A Route Traffic to IPv4 Address -> Alias -> Elastic Beanstalk Environment -> US East (N. Virginia) -> hack-western-8-env -> create records<br/>
Create another record but with alias www.<br/>

Now we can load the website using:<br/>
hack-western-8.com<br/>
www.hack-western-8.com<br/>
https://hack-western-8.com<br/>
https://www.hack-western-8.com<br/>

Note that there is a lock icon beside the link to indicate that we are using a SSL certificate and so we are secure<br/>