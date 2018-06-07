# usda-fns-ingestor

An experiment in ingesting data for the USDA's Food and Nutrition Service
using [django-data-ingest](https://github.com/18F/django-data-ingest).

Use [the webform](https://usda-fns-ingestor.app.cloud.gov/data_ingest) 
to interactively upload files and see
validation results, or the [API](api.md) to simply see the validation results.

## Deploying locally 

You'll need to install [Python](http://www.python.org/) and 
[PostgreSQL](https://www.postgresql.org/), then

    createdb usda_fns_ingestor
    cd usda_fns_ingestor 
    pip install -r requirements.txt 
    python manage.py runserver
    
It's best to do this after activating a 
[Python virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/#lower-level-virtualenv)
or using [Pipenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/): 

    pipenv install 
    pipenv shell
    
You can use other PostgreSQL configurations (database name, user, 
require a password, etc); just `export DATABASE_URL=<database url>`.
See [dj-database-url](https://github.com/kennethreitz/dj-database-url)

Then you can access the system at 
[http://localhost:8000/data_ingest/](http://localhost:8000/data_ingest/)

## Deploying to cloud.gov 

Once [logged into a cloud.gov workspace](https://cloud.gov/docs/apps/deployment/),
you can 

    cd usda_fns_ingestor
    cf create-service aws-rds shared-psql usda-fns-ingestor-db
    cf push

Other CloudFoundry platforms and Heroku should work similarly,
though different plans may be available (see `cf marketplace`)

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for additional information.

## Public domain

This project is in the worldwide [public domain](LICENSE.md). As stated in [CONTRIBUTING](CONTRIBUTING.md):

> This project is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/).
>
> All contributions to this project will be released under the CC0 dedication. By submitting a pull request, you are agreeing to comply with this waiver of copyright interest.
