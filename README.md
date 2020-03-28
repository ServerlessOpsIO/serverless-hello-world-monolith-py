# serverless-hello-world-py

Serverless Hello World Python sample service

[![logo](diagram.png "Application diagram")](https://drive.google.com/file/d/1V_0zd3Xrfaf9VSIae6fweY6o49UZSkWo/view?usp=sharing)


```bash
.
├── LICENSE
├── Makefile
├── Pipfile
├── README.md
├── events
│   └── CreateItem-msg.json
├── pytest.ini
├── src
│   ├── common
│   │   ├── common
│   │   │   └── __init__.py
│   │   └── setup.py
│   └── handlers
│       ├── CreateItem
│       │   ├── __init__.py
│       │   ├── function.py
│       │   └── requirements.txt
│       ├── DeleteItem
│       │   ├── __init__.py
│       │   ├── function.py
│       │   └── requirements.txt
│       ├── RetrieveItem
│       │   ├── __init__.py
│       │   ├── function.py
│       │   └── requirements.txt
│       └── UpdateItem
│           ├── __init__.py
│           ├── function.py
│           └── requirements.txt
├── template.yaml
└── tests
    ├── conftest.py
    └── unit
        ├── __init__.py
        └── src
            ├── __init__.py
            └── handlers
                ├── __init__.py
                └── CreateItem
                    └── test_handler.py
```

## Requirements

* AWS CLI with Administrator permission
* [Python 3 installed](https://www.python.org/downloads/)
* [Pipenv installed](https://github.com/pypa/pipenv)
    - `pip install pipenv`
* [Docker installed](https://www.docker.com/community-edition)
* [SAM CLI installed](https://github.com/awslabs/aws-sam-cli)

## Setup process

### Local development

**Invoking function locally using a local sample payload**

```bash
sam local invoke CreateItem --event events/CreateItem-event.json
```

**Invoking function locally through local API Gateway**

```bash
sam local start-api
```

If the previous command ran successfully you should now be able to hit the following local endpoint to invoke your function `http://localhost:3000/hello`

**SAM CLI** is used to emulate both Lambda and API Gateway locally and uses our `template.yaml` to understand how to bootstrap this environment (runtime, where the source code is, etc.) - The following excerpt is what the CLI will read in order to initialize an API and its routes:

```yaml
...
Events:
  HelloWorld:
    Type: Api
    Properties:
      Path: /hello
      Method: get
```

## Packaging and deployment
To package and deploy this service run the command below.

```
$ make deploy
```

This will:
* Create an artifact deployment S3 bucket
* Bundle application dependencies
* Package the code and dependencies
* Upload code to S3.
* Deploy code via Cloudformation

## Fetch, tail, and filter Lambda function logs

To simplify troubleshooting, SAM CLI has a command called sam logs. sam logs lets you fetch logs generated by your Lambda function from the command line. In addition to printing the logs on the terminal, this command has several nifty features to help you quickly find the bug.

`NOTE`: This command works for all AWS Lambda functions; not just the ones you deploy using SAM.

```bash
sam logs -n CreateItem --stack-name serverless-hello-world-py --tail
```

You can find more information and examples about filtering Lambda function logs in the [SAM CLI Documentation](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-logging.html).

## Testing


Next, we install test dependencies and we run `pytest` against our `tests` folder to run our initial unit tests:

```bash
pip install pytest pytest-mock --user
python -m pytest tests/ -v
```

## Cleanup

In order to delete our Serverless Application recently deployed you can use the following AWS CLI Command:

```bash
aws cloudformation delete-stack --stack-name serverless-hello-world-py
```

