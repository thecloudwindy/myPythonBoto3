import boto3

def iam_client():
    client = boto3.client('iam')
    return client

def listUser():
    response = iam_client().list_users()
    return response

if __name__ == '__main__':
    result = listUser()
    for name in result['Users']:
        print(name['UserName'])
    