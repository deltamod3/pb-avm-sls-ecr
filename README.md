# House Price Prediction API

## Development

### Environment
1. Install Python 3.8 or higher.
2. Create a new virtual environment: `python -m venv venv`.
3. Activate the created environment: `source venv/bin/activate`.
4. Install dependencies: `pip install -r requirements.txt`.
5. Download .joblib files from [Google Drive](https://drive.google.com/drive/folders/1p35QKAUrN5EChakDWsr9mlwkGCP_WsNf?usp=share_link) and place them in the `models` directory.
6. Change directory to the app with `cd ./app`.
7. Run the Flask app from the app directory: `flask run`.
8. Send GET or POST queries with JSON body to `localhost:5000/`.

### Request Body Example

```json
{
    "type": "sale",
    "features.propertyType": "detachedHouse",
    "features.beds": 2,
    "features.baths": 0,
    "lat": 57.107,
    "lon": -2.239
}
```

### Response Body Example
Response will send back predicted price as well as received data.

```json
{
    "data": {
        "features.baths": 0,
        "features.beds": 2,
        "features.propertyType": "detachedHouse",
        "lat": 57.107,
        "lon": -2.239,
        "type": "sale"
    },
    "price": 256666.671875
}
```

## Deployment
We use the Serverless Framework to deploy the Docker container to Amazon Elastic Container Registry (ECR) and connect it to AWS Lambda.

### Prerequisites
1. Install Serverless Framework: Serverless Framework Installation Guide.
2. Install AWS CLI: AWS CLI Installation Guide.

### Update serverless.yml file
Before deploying, you need to update the serverless.yml file with your desired configuration. Make sure to specify the deployment stage, region, and other settings as needed.

### Deploy with Serverless Framework

To deploy your API, use the following command:

```bash
sls deploy
```
This command will package your application, create an AWS Lambda function, and configure it to run the Docker container from the ECR repository.

Once the deployment is successful, you will receive the API endpoint URL that you can use to access your House Price Prediction API.

### Reference
[- Deploy Python Lambda functions with container images](https://docs.aws.amazon.com/lambda/latest/dg/python-image.html#python-image-instructions)
[- Deploy Containerized Serverless Flask to AWS Lambda](https://medium.com/hoonio/deploy-containerized-serverless-flask-to-aws-lambda-c0eb87c1404d)
