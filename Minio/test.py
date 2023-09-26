from minio import Minio

source={"url":"18.217.196.203:9000",

               "minio_access_key":"kBSeUX6rAW9Fj8LdohLi",

                "minio_secret_key":"TNoS9XNLbXOv1LQTcH7Lsi9DXivlWN0oF4ApaKFT",

                "api":"s3v4",

                "path":"auto"}

minio_client = Minio(source['url'],
                     access_key=source["minio_access_key"],
                     secret_key=source["minio_secret_key"],
                     secure=False)

print('connected')

