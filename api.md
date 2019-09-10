API
===

Some operations are available via a RESTful API.

List uploads
------------

`GET` to `/data_ingest/api/` for a list of all uploads.

Validate
--------

`POST` to `/data_ingest/api/validate/` to apply your app's validator
to a payload.  This will not insert the rows, but will provide 
error information.

This endpoint requires a token to authenticate.  Admin should be able to log into the admin page from a web browser
at `/admin/` and under "Authentication And Authorization" -> "Users", click on "+ Add" to add a user.
After a user has been added, they can obtain the token to authenticate.

### Obtain Token
`POST` to `/data_ingest/api/api-token-auth` to get the token for authentication.
```bash
curl -X POST \
-F username=<replace with what the admin gives you> \
-F password=<replace with what the admin gives you> \
https://usda-fns-ingestor.app.cloud.gov/data_ingest/api/api-token-auth/
```

You will get a JSON response back with the token:
```json
{"token": "<Token to use for authentication on validate API>"}
```

Use this token in the header as shown below.

### Validate JSON data
```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Token <Replace with your Token here>" \
-d @test_cases.json \
https://usda-fns-ingestor.app.cloud.gov/data_ingest/api/validate/
```

#### For local development
```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: Token <Replace with your Token here>" \
-d @test_cases.json http://localhost:8000/data_ingest/api/validate/
```

or, in Python,
```python
import requests
import json


url = 'https://usda-fns-ingestor.app.cloud.gov/data_ingest/api/validate/'
# or url = 'http://localhost:8000/data_ingest/api/validate/'

with open('test_cases.json') as infile:
    content = json.load(infile)
resp = requests.post(url,
                     json=content,
                     headers={
                        "Authorization": "Token <Replace with Token here in the form of environment variables, not raw text in the code>"
                     })
resp.json()
```

### Validate CSV data
```bash
curl -X POST \
-H "Content-Type: text/csv" \
-H "Authorization: Token <Replace with your Token here>" \
--data-binary @usda_cases.csv \
https://usda-fns-ingestor.app.cloud.gov/data_ingest/api/validate/
```

#### For local development
```bash
curl -X POST \
-H "Content-Type: text/csv" \
-H "Authorization: Token <Replace with your Token here>" \
--data-binary @usda_cases.csv \
http://localhost:8000/data_ingest/api/validate/
 ```

or, in Python,
```python
import requests

url = 'https://usda-fns-ingestor.app.cloud.gov/data_ingest/api/validate/'
# or url = 'http://localhost:8000/data_ingest/api/validate/'

with open('test_cases.csv') as infile:
    content = infile.read()
resp = requests.post(url,
                     data=content,
                     headers={
                        "Content-Type": "text/csv",
                        "Authorization": "Token <Replace with Token here in the form of environment variables, not raw text in the code>"
                    })
resp.json()
```
