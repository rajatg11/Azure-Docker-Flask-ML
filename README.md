# Azure-Docker-Flask-ML
Azure-Docker-Flask-ML

## Following are the steps to test it locally:
1.  Clone the Repo
2.  Open Command Prompt or Terminal
    1.  Go to the flask_app folder
    2.  Run Docker Build command - **docker build -t azure-deploy .**
    3.  Run Docker Run Command - **docker run -d -p 8080:5000 azure_deploy**
    4.  Open the Browser and hit this URL - http://localhost:8080
    5.  WebApp should open
        ![Localhost Webapp](/images/localhost_webapp.png)
## Following are the steps to deploy it on Azure:
1.  Clone the Repo
2.  Create the Azure Container Registry
    1.  Go to [Azure Portal](https://portal.azure.com)
    2.  Search for Container registries services
        ![container_registry](/images/container_registry.png)
    3.  Create a new container registry
        ![create_container_registry](/images/create_container_registry.png)
        1.  Choose Subscription details and resource group (it can also be created)
        2.  Registry Name should be unique - I chose **flaskazure.azurecr.io**
        3.  Location default - Central U.S.
        4.  SKU - Standard
        5.  Copy the username and password from the Access keys
        ![container_registry_key](/images/container_registry_key.png)
3.  Open Command Prompt or Terminal
    1.  Go to the flask_app folder
    2.  Run Docker Build command - **docker build -t flaskazure.azurecr.io/azure-deploy:latest .**
    3.  Run Command - **docker flaskazure.azurecr.io login**
        1.  Enter username as in Docker registry
        2.  Enter password as in Docker registry
    4.  Run Docker Push Command - **docker push flaskazure.azurecr.io/azure-deploy:latest**
    5.  We should see Docker image is deployed
     ![deployed_docker_repository](/images/deployed_docker_repository.png)
4.  Create a Webapp in Azure
    ![Web app Service](/images/app_services.png)
    1.  Choose your subscripion and Resource Group (it can also be created)
    3.  Create a unique name for webapp. I have created azure-ML-webapp
    4.  I need to choose whether I want to publish the app directly from the code or Docker Container. I will choose **Docker Conatiner**.
    5.  OS is Linux
    6.  region - Default is Central U.S and I will not change it for now.
    7.  **We should change Sku and Size if we don't want to be charged**. I will pick F1, which is free, under Development and Test.
    8.  Click on Next and Fill Docker Registry Details
    ![webapp_docker_details](/images/webapp_docker_details.png)
    9.  Click on Review and Create and then Create. A new deployment will be created.
5.  Copy the URL from the Webapp and hit in the browser. We should see the app.
    ![webapp_browser](/images/webapp_browser.png)
6.  Enter the Details for Prediction
    ![enter_details_for_prediction](/images/enter_details_for_prediction.png)
7.  See the Prediction
    ![prediction](/images/prediction.png)

## Following are the steps for CI-CD deployment on Azure:
1.  Make some changes in the code - I did changes in **Predict.html** and changed **Prediction Result** to **Prediction Result (Included CI-CD process)**
2.  Run Docker Build command - **docker build -t flaskazure.azurecr.io/azure-deploy:latest .**
3.  Run Docker Push Command - **docker push flaskazure.azurecr.io/azure-deploy:latest**
4.  Check the Logs and we will see new deployment
5.  Refresh the WebApp URL and Enter the Details again.
6.  See the Message- It is changed to **Prediction Result (Included CI-CD process)**
  ![prediction_CICD](/images/prediction_CICD.png)
