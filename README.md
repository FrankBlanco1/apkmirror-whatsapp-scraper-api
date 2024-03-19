# Description

This is a simple api, with a single endpoint for show the whatsapp versions for android devices available in apkmirror webpage 

## Install dependencies

To run the project you must be install all dependecies with the following command:

```console
foo@bar: pip install -r requirements.txt
```

**Hint:** We recommend to use a python enviroment

## How to run on localhost

Once you have the dependencies intalled, to setup the server you just need to run the following command

```console
foo@bar: uvicorn main:app --reload
```

Then the project will be running on:

<http:localhost:8000>

and the docs will be running on:

<http:localhost:8000/docs>
