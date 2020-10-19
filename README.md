![TravisBuild](https://travis-ci.org/ris-tlp/iss-api.svg?branch=master)

# iss-api  
A simple RESTful API service that scrapes NORAD's Two Line Element (TLE) data sets, parses it using `PyOrbital` and returns a JSON object containing the current latitude/longitude of the Internation Space Station.

## Instructions  
`python3 -m pip install pipenv` to use pipenv to further install dependencies.  
`pipenv --three` to create a Python 3.x virtual environment.  
`pipenv install` to install dependencies.  
`./bootstrap.sh` to export environment variables and start the app at host 0.0.0.0  

## Sample output  
`curl http://0.0.0.0:5000/` returns a JSON Object:  
```
{
  "Latitude": 51.799, 
  "Longitude": 164.088
}
```
# Pull Request
