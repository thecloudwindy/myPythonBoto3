import boto3

def iam_client():
    client = boto3.client('iam')
    return client

def attachPolicyUser():
    response = iam_client().attach_user_policy(
        UserName = 'newTestUser',
        PolicyArn ='arn:aws:iam::994823578500:policy/demoPolicy01'
    )
    return response

if __name__ == "__main__":
    print(attachPolicyUser())