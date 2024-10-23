import boto3

def iam_client():
    client = boto3.client('iam')
    return client 

def createUser(userName):
    response = iam_client().create_user(
        UserName = userName,
        Tags = [
            {
                'Key' : 'Name',
                'Value' : userName
            }
        ]
    )

    return response

if __name__ == '__main__':
    userName = input("Enter the name of user: ")
    result = createUser(userName)
    print(result)