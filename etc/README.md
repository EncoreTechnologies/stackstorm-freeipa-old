# How to generate new actions (easy way)

``` shell
# this will do the following:
#  - setup virtualenv
#  - install requirements.txt
#  - fetch the API spec
#  - genreate the actions from the API spec
make

# cleanup our temp directories freeipa/ and virtualenv/
make clean
```

# How to generate new actions (hard way)

``` shell
virtualenv virtualenv
source ./virtualenv/bin/activate
pip install -r requirements.txt

# clones the freeipa/ git repo, 
# finds the latest tag that starts with "release-"
# copies the API.txt file from that tag into spec/API-release-x.y.z.txt
./generate_actions.py fetch-spec

# reads an API spec file and generates action metadata files from it
# these generated action files are automatically put into ../actions
./generate_actions.py generate -s ./spec/API-release-x.y.z.txt

# cleanup the temp directories freeipa/ and virtualenv/
./generate_actions.py clean
```


