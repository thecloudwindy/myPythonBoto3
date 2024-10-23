import boto3
import json 

def iam_client():
    client = boto3.client('iam')
    return client

def createPolicy():
    with open("s3Policy.json", "r") as file:
        content = file.read()

    response = iam_client().create_policy(
        PolicyName = "demoPolicy01",
        PolicyDocument = content,
        Description = "Demo S3 Policy"
    )

    return response

if __name__ == "__main__":
    print(createPolicy())
