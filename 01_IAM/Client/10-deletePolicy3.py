import time
import boto3 
import json

import botocore 

def iam_client():
    client = boto3.client('iam')
    return client

def listCustomerPolicies():
    responseListCustomerPolicies = iam_client().list_policies(
        Scope = "Local",        
    )
    return responseListCustomerPolicies

def deletePolicy(arn):
    responseDeletePolicy = iam_client().delete_policy(
        PolicyArn=arn
    )
    return responseDeletePolicy

def dictToList():
    # Liệt kê các ARN của Policies sau đó ghi chúng vào file myArn
    result = listCustomerPolicies()
    for name in result['Policies']:
        with open("myArn", "+a") as file:
            file.write(name["Arn"] + "\n")
    
    time.sleep(5)

    # Đọc file arn và chuyển chúng sang dạng list
    with open("myArn", 'r') as file:
        lines = file.readlines()
    
    lines = [line.strip() for line in lines]
    return lines

if __name__ == "__main__":
    result = dictToList()
    #print(result)
    for arn in result:
        #while(True):
        #arn = input("Arn of Policy: ")
        try:
            print(deletePolicy(arn))
        except botocore.exceptions.ClientError as error:
            if error.response['Error']['Code'] == 'DeleteConflict':
                #print(f"Policy {arn} cannot be deleted because it is attached to entities.")
                with open("cannotDeleteArn",'+a') as file:
                    file.write(arn + "\n")
                    continue
            else:
                #print(f"An error occurred: {error}")
                with open("cannotDeleteArn2",'+a') as file:
                    file.write(arn + "\n")
                    continue

                