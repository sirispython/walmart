After getting the source code from github repository,

1. Make sure python 3 is installed
2. The rest of the dependencies like Flask,Virtual environment, Flask API and gunicorn will be installed 
automatically by running step 3
3. Run the following to start the web application through docker from the root folder(in this case walmart)-
docker-compose -f docker-compose.prod.yml up -d --build
4. The following step will indicate whether the web application was started successfully -
docker-compose -f docker-compose.prod.yml logs -f

The output of the above command should be something like -

sirishas-MBP:walmartwebapp sg$ docker-compose -f docker-compose.prod.yml logs -f
Attaching to walmartwebapp_web_1
web_1  | [2020-08-28 22:26:34 +0000] [1] [INFO] Starting gunicorn 20.0.4
web_1  | [2020-08-28 22:26:34 +0000] [1] [INFO] Listening at: http://0.0.0.0:8080 (1)
web_1  | [2020-08-28 22:26:34 +0000] [1] [INFO] Using worker: sync
web_1  | [2020-08-28 22:26:34 +0000] [8] [INFO] Booting worker with pid: 8

5. Now you should see the text "Hello!" when you type at the command prompt 

curl http://localhost:8080 

sirishas-MBP:walmartwebapp sg$ curl http://localhost:8080
Hello!sirishas-MBP:walmartwebapp

6. When you type  curl http://localhost:8080/healthz on the command prompt you should see the following -
(the prompt will be specific to your environment) 

sirishas-MBP:walmartwebapp sg$ curl http://localhost:8080/healthz
{"status": 200, "version": "0.0.1", "uptime": "up since 2020-08-28 22:26:34"}
sirishas-MBP:walmartwebapp sg$ 

7.To stop the web application, do the following -
docker-compose -f docker-compose.prod.yml down
