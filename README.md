<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">City Details Portal</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/rohitswarke/city-details.svg)](https://github.com/rohitswarke/city-details/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/rohitswarke/city-details.svg)](https://github.com/rohitswarke/city-details/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> This project is to create a simple UI portal where user can put few letters of the city name and get all matching records for the given city name. The project demonstrates use of FastAPI with MongoDB. 
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Prerequisites and installation](#installation)
- [Test case execution and coverage report](#test_cases)
- [Running the project](#run)
- [Usage](#usage)
- [Built Using](#built_using)
- [Deployments](#deployment)
- [UI Screenshots](#ui_screenshots)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

A UI and API end points which allows the user to enter a letter and get following details:
1. Number of cities beginning with that letter
2. City names beginning with that letter

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

## Prerequisites and installation <a name = "installation"></a>

1. Install Anaconda on your system.
    Follow instructions given on link: https://docs.anaconda.com/anaconda/install/index.html

2. Clone repository on your system

3. Setup Virtual Environment
  It is always a good practice if you create a separate python/conda environment for new project.
  The default environment, which ``conda`` itself is install into is called ``base``. To create another environment, use the ``conda create`` command.

  Note:- You can create python virtual environment as well, however I prefer conda and hence below instructions are for Conda environment setup.

  For instance, to create an environment you would run
  ```
  conda create -n city-details python=3.9
  ```
  This creates an environment called ``city-details`` with python version 3.9.
  We can now activate this environment, use
  ```
  # On newer versions of conda (v4.6 or later)
  conda activate city-details

  # on older versions of conda
  source activate city-details
  ```

  Once you are in newly created environment, next step is to install the dependency packages from ``requirements.txt``
  ```
  pip install -r requirements.txt
  ```
  

Download sample dataset of world cities from below link:
[simplemaps.com](https://simplemaps.com/data/world-cities)

Download the ``worldcities.csv`` file from above link and keep it under data directory.
There is a script available data/load_csv.py to load this data in MongoDB.

```
cd city-details/data
python load_csv.py
```

Note :- You can skip above step if you have access of pre-loaded database.


### Place ``.env`` file in project directory. You can rename the existing .env-example file to .env as well.

Add MONGODB_URL in .env file.


## Test case execution <a name="test_cases"></a>

I'm using pytest framework to test the api calls. You just need to goto the projet directory and run pytest command.
```
cd city-details
pytest
```

### Coverage report

Run below pytest command alongwith --cov option to generate the coverage report
```
pytest --cov=city_details tests\ > coverage

----------- coverage: platform win32, python 3.9.6-final-0 -----------
Name                                                      Stmts   Miss  Cover
-----------------------------------------------------------------------------
city_details\__init__.py                                     39      2    95%
city_details\__main__.py                                      3      3     0%
city_details\__version__.py                                   2      0   100%
city_details\api\__init__.py                                  0      0   100%
city_details\api\api_v1\__init__.py                           0      0   100%
city_details\api\api_v1\api.py                                9      0   100%
city_details\api\api_v1\routes\__init__.py                    0      0   100%
city_details\api\api_v1\routes\all_request_router.py         27      0   100%
city_details\api\api_v1\routes\city_router.py                33      6    82%
city_details\api\api_v1\routes\health_checker_router.py      37      9    76%
city_details\api\api_v1\routes\ui_router.py                  34      8    76%
city_details\core\__init__.py                                 0      0   100%
city_details\core\config.py                                  29      6    79%
city_details\core\custom_logging.py                          42      2    95%
city_details\core\enhanced_json_encoder.py                   12      5    58%
city_details\core\errors.py                                  19      8    58%
city_details\core\interfaces.py                              11      1    91%
city_details\core\utils.py                                   33     18    45%
city_details\crud\__init__.py                                 0      0   100%
city_details\crud\city.py                                    17      0   100%
city_details\db\__init__.py                                   0      0   100%
city_details\db\mongodb.py                                    6      0   100%
city_details\db\mongodb_utils.py                             17      0   100%
city_details\models\__init__.py                               0      0   100%
city_details\models\city.py                                  23      0   100%
city_details\models\health.py                                13      0   100%
-----------------------------------------------------------------------------
TOTAL                                                       406     68    83%

====================================================================================================== 3 passed, 1 warning in 1.79s ======================================================================================================


```



## 🚀 Running the project <a name = "run"></a>

```
cd city-details
python -m city_details
```


## 🎈 Usage <a name="usage"></a>

Once the project is up and running, by default it accepts traffic from all hosts i.e. ``0.0.0.0`` and detault port is ``8086``

- Try to open the URL: [http://localhost:8086](http://localhost:8086)



## 🚀 Deployment <a name = "deployment"></a>

First create wheel bundle of the project using following command:
```
python setup.py bdist_wheel
```
Above command will generate a dist directory and a wheel file inside it.
This file contains entire build of this system (except .env and tests).
You can distribute this wheel file on any of the server and just install it in any environment:
```
pip install city_details-0.0.1-py3-none-any.whl
```
You need to put .env file on the system to start the project and connect to the MongoDB.

### To build docker image

The Dockerfile is also tested and is absolutely working fine.
Run below commands to build the image locally and then bin 8086 port of docker container to 80 port on your local.

```
cd city-details
docker build -t myapp:0.0.1 .
docker run -p 8086:80  myapp:0.0.1
```

## UI Screenshots <a name = "ui_screenshots"></a>

### Below screenshots are of application running on AWS Docker <br/>
### Backend MongoDB is currently running on a 3 node replica cluser on MongoDB Atlas.


![UI-1](https://github.com/rohitswarke/city-details/blob/main/static/portal_1.PNG?raw=true) <br/>
![UI-2](https://github.com/rohitswarke/city-details/blob/main/static/portal_3.PNG?raw=true) <br/>
![UI-4](https://github.com/rohitswarke/city-details/blob/main/static/portal_4.PNG?raw=true) <br/>



## ⛏️ Built Using <a name = "built_using"></a>

- [MongoDB](https://www.mongodb.com/) - Database
- [FastAPI](https://fastapi.tiangolo.com/) - Web Framework
- [Uvicorn](https://www.uvicorn.org/) - Lightening-fast ASGI server
- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - Templating engine

## ✍️ Authors <a name = "authors"></a>

- [@rohitswarke](https://github.com/rohitswarke) - Idea & Initial work

See also the list of [contributors](https://github.com/rohitswarke/city-details/graphs/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
