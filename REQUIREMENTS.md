Technical Exercise (2.5h)

The following exercises will help us to understand your way of thinking from the architecture level as well as your Python coding skills. The exercise will be reviewed live, so we expect you to have the environment ready to show it working and answering any questions that may arise, even making changes to the code! The live review will simulate a common scenario where you interact with team members solving and commenting on any issues that may arise. This will give the opportunity to see how it would be to be working together, this is the time when your soft skills will be evaluated.
To help you understand better, here are some important concepts that are illustrated in the sample payload that is accompanying the test:
-Extracted flight sensor data: timeseries of the sensor values extracted during a complete flight (climb, cruise, descend). Those are stored in LATITUDE, LONGITUDE and ALTITUDE keys of the json
-Flight route: list of given waypoints from one airport to another. Those are stored in the key lastOfp. Fpl represent the flight plan (succession of waypoints), and every waypoint is stored in the waypoints key by successive order

0.Reading and understanding the Exercise (0.5h)

1.Architecture (descriptive) (1h)
a.Design an API that enables to...
i.store existing flight routes (with direction, time, fuel consumption) given an airline and aircraft a date
ii.return most used flight routes given two airports for (optionally) a given an airline, aircraft or a data range
iii.Return the most efficient route given two airports given the best time or best fuel consumption or a combination of both given time constraints
iv.return a proposed route given an existing flight route returning the proposed savings of the new route.
v.Will the API design change if the computation of the proposed route exceeds 10 seconds of computation?
b.Design the database
i.which pattern to use to efficiently store and compute the proposed route including airports information, waypoints positions and their recurrency usage
ii.take into consideration to later support efficient queries like finding for an airline and an aircraft the...
1.shortest route
2.fuel efficiency route
3.most used route
c.Scalability / maintainability
i.How to make it scalable so that the system can scale to more than 10.000 queries every minute? What would you propose to do to scale taking into consideration the algorithm takes approximately 10 seconds using a single CPU to compute a result?
ii.How to make it maintainable enough so that new routes and new waypoints can be added and removed in the system so that it becomes an evolving system and improves over time rather than a static one?
iii.Design the key aspects for the product development CI and CD, what will they include?

2.Coding Skills (working code) (1h)
a.Implement proposed database and show a working code
b.Implement proposed API
c.Implement the integration with the database
d.Tabular Data: Given an extracted flight sensor data in CSV
i.Load it
ii.Explore it (give relevant insights)
iii.Clean it

3.Bonus
This serves as an additional opportunity to show your value, either by showing a working code or by explaining in enough detail any of the following topics.
a.Setup in as a git repository
b.Design the algorithm for computing the best scenario
c.Design the algorithm to detect shortcuts
d.Scale and automate data cleaning
e.Include tests
f.Include documentation
g.Containerization of the API solution
h.Helm to deploy to K8s
i.How to scale a cluster wise the application (vertical, horizontal)?
j.Improvements or enhancements to current code

# ---------------------------- Summary --------------------------------------

# Features:

- postgres db setup
- redis + celery for async work
- endpoints for managing flight routes and waypoints
- endpoint for analysing the sensor data CSV (async, pandas)
- JWT auth
- docker-compose with services: app, postgres, celery, celery beat
- pre-commit tool
- makefile
- package management - poetry
- added documentation

# Remarks:

- JSON file data is inconsistent (fields missing for 1st waypoint)
- input data is missing in order to be able to build the implementation in the specified time; investigation is needed in order to understand the requirements; for instance aeronautics terminology:
  - EET - estimated elapsed time
  - OFP - Operational flight
  - DCT - The direct route between two points following a great circle distance path
- building the requested algorithms require more effort
- TO DO:
  - add tests
  - return routes (most used and most efficient)
  - add helm
