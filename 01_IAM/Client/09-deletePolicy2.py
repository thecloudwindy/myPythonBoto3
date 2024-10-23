import boto3
import botocore.errorfactory
import botocore.exceptions

def iam_client():
    client = boto3.client('iam')
    return client

def deletePolicy(arn):
    response = iam_client().delete_policy(
        PolicyArn=arn
    )
    return response

if __name__ == "__main__":
    flag = True
    while(flag):
        arn = input("Arn of Policy: ")
        try:
            print(deletePolicy(arn))
        except botocore.exceptions.ClientError as error:
            if error.response['Error']['Code'] == 'DeleteConflict':
                print(f"Policy {arn} cannot be deleted because it is attached to entities.")
            else:
                print(f"An error occurred: {error}")
        ask = input("Continue?(Y|N) ")
        if ask == "N" or ask == "No":
            flag = False
