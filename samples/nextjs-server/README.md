# NextJS API ONNX Server

In this example the ONNX model is loaded during request time (which is not ideal btw) on the server side.

Start the server
```
npm install

npm run dev
```

Test the model through the API
```
$ curl -X GET "http://localhost:3000/api/classifier?r=255&g=128&b=0"

{"isOrange":true}
```
