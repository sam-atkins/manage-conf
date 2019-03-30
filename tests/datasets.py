import datetime


BOTO_PAYLOAD = {
    "Parameters": [
        {
            "Name": "/portal/dev/ALLOWED_HOSTS",
            "Type": "StringList",
            "Value": "\"['uglyurl.execute-api.us-east-1.amazonaws.com']\"",
            "Version": 5,
            "LastModifiedDate": datetime.datetime(2019, 3, 26, 16, 15, 45, 414000),
        },
        {
            "Name": "/portal/dev/SECRET_KEY",
            "Type": "SecureString",
            "Value": '"not-a-good-secret"',
            "Version": 2,
            "LastModifiedDate": datetime.datetime(2019, 3, 26, 14, 53, 25, 738000),
        },
        {
            "Name": "/portal/dev/STATICFILES_STORAGE",
            "Type": "String",
            "Value": '"S3-storage"',
            "Version": 2,
            "LastModifiedDate": datetime.datetime(2019, 3, 26, 14, 53, 39, 600000),
        },
    ],
    "ResponseMetadata": {
        "RequestId": "XXXXXXXXXX",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "XXXXXXXXXX",
            "content-type": "application/x-amz-json-1.1",
            "content-length": "1621",
            "date": "Sat, 30 Mar 2019 08:11:35 GMT",
        },
        "RetryAttempts": 0,
    },
}
