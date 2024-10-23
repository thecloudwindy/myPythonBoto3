import boto3

def iam_client():
    client = boto3.client('iam')
    return client

def listCustomerPolicies():
    response = iam_client().list_policies(
        Scope = "Local", # Customer Policies ; "AWS " <=> AWS Policies; "All"        
    )
    return response

if __name__ == "__main__":
    #print(listCustomerPolicies())
    result = listCustomerPolicies()
    i = 1
    for name in result['Policies']:
        with open("arn", "+a") as file:
            file.write(name["Arn"] + "\n")
        # print(i, '-', "Policy Name: ", name["PolicyName"],"\n","\tARN: ", name["Arn"])
        # i += 1
