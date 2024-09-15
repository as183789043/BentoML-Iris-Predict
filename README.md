
![未命名設計](https://github.com/user-attachments/assets/d2f47d4e-2fa2-4c34-b416-89591a2b9722)

### This repository demonstrates how to rapidly package and deploy machine learning models using BentoML. It provides a step-by-step guide for:

Model Packaging: Efficiently save and manage machine learning models with BentoML.
Service Creation: Define and deploy RESTful APIs for model inference.
Containerization: Use BentoML to package your model and service into a container for seamless deployment.
Explore practical examples, learn best practices, and get started with BentoML for streamlined model deployment.


### Build Environment in your local 

### Build Web Page 
```bash
git clone https://github.com/as183789043/BentoML-Iris-Predict.git
cd BentoML-Iris-Predict
pip install -r requirements.txt
python train.py
bentoml serve  service:IrisPredict
```

### Enter Web Page (Chrome or Edge)
```
[localhost:3000](http://localhost:3000)
```
### You will see something like this
![image](https://github.com/user-attachments/assets/54f838a8-4cd0-4af8-9732-7e27eb4e97c5)

## Build Container image 
### you need to have a bentofile.yaml
```yanl
service: "service:IrisPredict"
labels:
  owner: <you can input anything>
  project: Iris_Predict
models:
  - "clf:latest" # A string model tag
  - tag: "clf:latest"
include:
  - "*.py"
python:
  requirements_txt: "./requirements.txt"
```

## Build model to bentoml 
```
bentoml build
bentoml list
bentoml containerize iris_predict:latest
```

### you will get image in docker desktop
![image](https://github.com/user-attachments/assets/ef1a6015-4008-471c-97f5-0c80d94296d4)


## Run image
```
docker run --rm -p 3000:3000 iris_predict:<version>
```




