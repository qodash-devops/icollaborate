## Mission Statement
### General purpose:
Create an application to help find matching collaborators in github.
Trough github crawling and relationship modelling.
The user should be able to find and identify potential collaborators or projects related to a specific topic.
### Why:
It is indeed very hard and time consuming to find people in github that match your interests or projects you like to work on.
This project is trying to solve the following problems:
- Avoid redunancy in project creation and foster effort unification.
- Make it easy for developpers/entrepreneurs to build a team around the globe.
- Follow users that have similar interests.

## Getting started:
- ###Prerequisit:
  - recommended dev env: Linux with node and Python3.7.
  - Install Docker. [get docker](https://docs.docker.com/get-docker/)
  - Install docker-compose <br>
  `sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`                 
- ###Local dev env :              
    - Back End: 
        - github archive crawler: crawls [gharchive](https://www.gharchive.org/)[gharchive) and feeds graph database.<br>
        in \crawl folder `python crawler.py  start --spider=gharchive`
        - repos description and readme crawler:<br>
        in \crawl folder `python crawler.py  start --spider=repos`  
    - Database:<br>
        - neo4j deployement: in /backend folder `docker-compose up -d neo4j`
        - Nodes (Repos,Actor) Relationships Contribution
    - Front End:<br> 
        -  deploy backend `docker-compose up -d datacrawler #deploy back end and crawl data` <br>
        - run the js app locally `cd UI && npm run serve`
    
## Roadmap:
- #### Github crawler (scrapy/python):
Github.com crawler using scrapy framework.
- #### Backend (node/neo4j):
Database to model the relationships between contributors and repos.
With an api to model it.
The api would model it. 
- #### UI (Vue.js)
Main use case is to search repos and contributors by topic.

- ### NLU and topic modeling.
Finding projects/issues/contributors that would best match a certain topic/subject.
- Learn the right distance metric between repos. (From description, README.md)
- Learn the right distance metric between Actors(contributors) according to their contributions.
 
 ### Contributors welcome.
[contribution guidelines ](https://github.com/qodash-devops/icollaborate/blob/master/CONTRIBUTING.md)
- This is just the beginning of something great!
- If you like the mission and can contribute in any form (code/issues/doc) please reach out.   
