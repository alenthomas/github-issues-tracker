# github-issues-tracker
A django app to give the status of all open issues in a repository 

**github-issues-tracker** uses [github api](https://developer.github.com/v3/) to fetch the issues in a public repository.
It executes till all open issues are fetched or the api limit exceeds.

The live application is hosted on heroku. [here](https://mysterious-shelf-80881.herokuapp.com/)

If given more time, we could
  1. add better exception handling
  2. improve UI/UX
  3. add github auth token to increase the api query limit
  4. add unit tests and functional tests if it is a long term project
  
## running locally
  1. make a virtualenv with python>=3.5
  2. ` pip install -r requirements.txt `
  3. ` python manage.py runserver `
  4. open your localhost http://127.0.0.1:8000
