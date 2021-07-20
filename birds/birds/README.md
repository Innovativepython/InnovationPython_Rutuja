It's a bird emergency.

1.  In the Models folder, there's a birds_nort_america.xml file, you need to convert this into a model and then into JSON for the views/birdtype.py service.
2.  The birdtype service already is served at http://127.0.0.1:8000/bird/v1/types but we need your new version to be served at http://127.0.0.1:8000/bird/v2/types to support redundancy for our birder community.
3.  We need a set of sample code that shows people how to consume our service.  We need a well documented addition to this read me to tell people how to use the service on a web page along with a sample file served at http://127.0.0.1:8000/birdsofnorthamerica
4.  Finally, we need a positive and a negative test case on at least one of your functions.