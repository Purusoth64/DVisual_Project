# from minio import Minio
# # import pandas as pd
# from io import BytesIO
# source={
#     "minio_endpoint":"localhost:9000",
#     "minio_access_key":"SPDURAI64",
#     "minio_secret_key":"durai_secret_key",
#     "minio_bucket":"durai",
#     "csv_filename":"gender.csv"
# }

# try:
#     minio_client = Minio(source['minio_endpoint'],
#                     access_key=source["minio_access_key"],
#                     secret_key=source["minio_secret_key"],
#                     secure=False)

#     # csv_data = minio_client.get_object(source["minio_bucket"],source["csv_filename"])
#     # print('Minio server Connected Sucessfully')
#     # df=pd.read_csv(csv_data)
#     # print(df)

#     with open("D:\Combined_views.pdf", "rb") as pdf_file:
#         pdf_data = pdf_file.read()
#     minio_client.put_object("durai","workbook.pdf", BytesIO(pdf_data), len(pdf_data))
#     print('connected to minio server')
#     print("pdf uploaded Sucessfully")
# except Exception as e:
#     print(e)


#-------------------------------------------------------------------------------------------------------
from pipes import quote
from minio import Minio
from io import BytesIO
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
import urllib.parse



class Remove_Duplicate(APIView):
    def post(self, request, *args, **kwargs):
        
        source={
            "minio_endpoint":"localhost:9000",
            "minio_access_key":"SPDURAI64",
            "minio_secret_key":"durai_secret_key",
            "minio_bucket":"durai",
            "csv_filename":"workbook.pdf"
        }
        # source={"url":"http://18.217.196.203:41345/api/v1/service-account-credentials",

        #        "minio_access_key":"kBSeUX6rAW9Fj8LdohLi",

        #         "minio_secret_Key":"TNoS9XNLbXOv1LQTcH7Lsi9DXivlWN0oF4ApaKFT",

        #         "api":"s3v4",

        #         "path":"auto"}

        minio_client = Minio(source['minio_endpoint'],
                     access_key=source["minio_access_key"],
                     secret_key=source["minio_secret_key"],
                     secure=False)
        pdf_file ='workbook.pdf'
        pdf_url = minio_client.presigned_get_object(source['minio_bucket'], pdf_file)
        preview_link = f'<iframe src="http://localhost:9000/durai/pdf.pdf" width="100%" height="600px"></iframe>'
        encoded_object_name = urllib.parse.quote("workbook with spaces.pdf")

        anchor= f'<a href="http://localhost:9000/durai/pdf.pdf">Link Text</a>'

        # Set the Content-Type header to display PDF in browser
        # response = Response()
        # response['Content-Type'] = 'application/pdf'
        # response['Content-Disposition'] = f'inline; filename="{pdf_file}"'
        # response['X-Accel-Redirect'] = pdf_url  # Use X-Accel-Redirect header to redirect to the PDF URL
        
        
        # pdf_data = minio_client.get_object(source['minio_bucket'], pdf_file).read()


        return Response({'file_url':'http://localhost:9000/testing/pdf.pdf'})


#----------------------------------------------------------------------------------------------
        ###   working to downloade the pdf file
        # pdf_file = 'workbook.pdf'
        # # expiration = 3600  # URL expiration time in seconds (1 hour in this example)
        # pdf_url = minio_client.presigned_get_object(source['minio_bucket'], pdf_file)#, expires=expiration)

        # return Response({'file_url': pdf_url})

        