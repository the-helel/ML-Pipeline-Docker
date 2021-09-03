# Prediction Using ML Pipeline
# Steps to Run App

## 1. Download The model_weights.h5 and put it in main Directory where app.py is there

https://baitrainingdataset.blob.core.windows.net/interviewdata/model_architecture_and_weights.zip 

## 2. Download The Test Image Dataset

https://baitrainingdataset.blob.core.windows.net/interviewdata/test_images.zip 

# prerequisite :- You Should Have Docker Installed and Running in your System.

## 3. Build Docker Image from Docker File

docker build -t flaskapp .


# Make sure your port is forwarded or you have allowed the following port in firewall or inbound traffic

## 4. Run Docker Image and expose port 5000

docker run -dit -p 5000:5000 --name flask1 flaskapp

## 5. Access Your Website

   http://<ip>:5000
   
Now Upload Image and Your Prediction will be done

# Task 1 : Things to think about

## A. We can Use jenkins Or Openshift for training this model in Pipeline Or make the proper ML pipeline. And Monitor the pipeline and Training Using MlFlow by log_metric , log_param into experiment. We can also monitor using Prometheus and Grafana.

## B. As said earlier that we can use Jenkins and set a Pipeline to update class of model and building New Docker Image. Hence Along with Docker we will use Kubernetes So While Updating User will not face downtime of app

# Task 2 : Things to think about

## A. So as ssid, We can Scale Our Pipeline By Running Pipeline using Kubernetes and Manage multiple containers at the same time. If a container/pod Stops or Fails it will automatically launch new one and we can also scale number of containers/pods we need to run

## B. For Updatipn of pipeline, we just need to code and upload it to Github, Then Jenkins will automatically Triggered and run create new Docker Image and Run Kubernetes to scale new image on the go without experiencing any Downtime.



