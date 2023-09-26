from django.http import Http404
from django.shortcuts import render, redirect
from Dvisual_app.models import *
from rest_framework.views import APIView
from report.serializers import *
from rest_framework.response import Response
from rest_framework import status
from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils import querying, flatten_dict_column
import PyPDF2
from minio import Minio
from urllib.parse import quote
import io
import os
from django.conf import settings
import random as r
# from report.tableau import TableauConnector
minio_client = Minio ("18.217.196.203:9000",
                    "kBSeUX6rAW9Fj8LdohLi",
                    "TNoS9XNLbXOv1LQTcH7Lsi9DXivlWN0oF4ApaKFT",
                    secure=False)
link_1=[]

class TableauConnector:
    
    def __init__(self, config):
        self.config = config
        self.conn = None
        self.pdf_url=None
        self.s=None

    def connect_to_tableau_server(self):
        # Establish a connection to Tableau Server
        self.conn = TableauServerConnection(self.config, env='tableau_online')
        self.conn.sign_in()
        print("Signed in Successfully")

    def get_workbook_views(self, workbook_name):
        # Retrieve the views associated with a given workbook
        views_df = querying.get_views_dataframe(self.conn)
        views_df = flatten_dict_column(views_df, keys=["name", "id"], col_name="workbook")
        relevant_views_df = views_df[views_df["workbook_name"] == workbook_name]
        return relevant_views_df['id'].tolist()

    def download_workbook_as_pdf(self, workbook_name):
        # Set parameters for PDF export
        pdf_params = {
            "pdf_orientation": "orientation=Landscape",
            "pdf_layout": "type=A4"
        }
        pdf_writer = PyPDF2.PdfWriter()

        view_ids = self.get_workbook_views(workbook_name)

        # Iterate through the view IDs
        for view_id in view_ids:
            # Query the PDF content for each view
            view_pdf = self.conn.query_view_pdf(view_id=view_id, parameter_dict=pdf_params)
            pdf_content = io.BytesIO(view_pdf.content)
            pdf_reader = PyPDF2.PdfReader(pdf_content)

            # Append each page of the PDF to the writer
            for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                pdf_writer.add_page(page)

        # Save the combined PDF file
        pdf_bytes = io.BytesIO()
        pdf_writer.write(pdf_bytes)
        pdf_bytes.seek(0)

        #creating random file name for minio 
        link="workbook_"
        m=r.randint(10,1000)
        s=str(link)+str(m)


        minio_client.put_object("d-visual",f"{s}.pdf", pdf_bytes, len(pdf_bytes.getvalue()))
        

        pdf=f"http://18.217.196.203:9000/d-visual/{s}.pdf"
        generated_link = d_link(link_1=pdf)
        generated_link.save()
        # generated_link_1 = dvisual_report(link=pdf)
        # generated_link_1.save()

        link_1.append(pdf)
        # print(pdf_url)
        print("Tableau workbook as a PDF file is downloaded successfully")


class Report_Api(APIView):
    
    def get_object(self, pk):
            try:
                return dvisual_report.objects.get(pk=pk)
            except dvisual_report.DoesNotExist:
                raise Http404
    def get(self, request, pk=None, format=None):
        if pk:
                data = self.get_object(pk)
                var_serializer = Dvisual_Report_Serializer(data)
                return Response([var_serializer.data])
        else:
                data = dvisual_report.objects.all()
                var_serializer = Dvisual_Report_Serializer(data, many=True)
                return Response(var_serializer.data)


    def post(self, request, format=None):
        data = request.data
        # dvisual_report_data={"r_link":link_1[-1]}
        # combined_data = {**data, **dvisual_report_data}
        # var_serializer = Dvisual_Report_Serializer(data=combined_data)
         
        var_serializer = Dvisual_Report_Serializer(data=data)

        

        var_serializer.is_valid(raise_exception=True)

        # var_serializer.save()
        # workbook_name=request.data.get['workbook_name']
        workbook_name=var_serializer.data['workbook_name']
        print(workbook_name)
        id=request.data.get('dvisual_config_detail_id')
        data = dvisual_config_detail.objects.get(id=id)
        sources = data.conn_str
        #print(sources)

        server = sources['server']
        api_version = sources['api_version']
        personal_access_token_name = sources['personal_access_token_name']
        personal_access_token_secret = sources['personal_access_token_secret']
        site_name = sources['site_name']
        site_url = sources['site_url']

        # Configuration details for Tableau Server
        config = {
            'tableau_online': { 
                'server': server,
                'api_version': api_version,
                'personal_access_token_name': personal_access_token_name,
                'personal_access_token_secret': personal_access_token_secret,
                'site_name': site_name,
                'site_url': site_url
            }
        }
   
        try:
            # import pdb
            # pdb.set_trace()
            # Instantiate the TableauConnector class
            tableau_connector = TableauConnector(config)
            

            # Connect to Tableau Server
            tableau_connector.connect_to_tableau_server()
            # Download the specified workbook as a PDF
            tableau_connector.download_workbook_as_pdf(workbook_name)
            # data['link'] = link_1[-1]
            # print(data)

            dvisual_report_data={"r_link":link_1[-1]}
            combined_data = {**data, **dvisual_report_data}
            var_serializer = Dvisual_Report_Serializer(data=combined_data)
            var_serializer.is_valid(raise_exception=True)
            var_serializer.save()

            response_data=link_1[-1]
            print(response_data)

            
            return Response({'message': 'Tableau workbook as a PDF file is downloaded successfully','file_url':link_1[-1]},
                             status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    


    def put(self, request, pk=None, format=None):
        var_update_conn_details = dvisual_report.objects.get(pk=pk)
        var_serializer = Dvisual_Report_Serializer(instance=var_update_conn_details,data=request.data, partial=True)
        var_serializer.is_valid(raise_exception=True)
        var_serializer.save()
        response = Response()
        response.data = {
            'message': 'Report Updated Successfully',
            'data': var_serializer.data
        }
        return response
    def delete(self, request, pk, format=None):
        var_delete_conn_details =  dvisual_report.objects.get(pk=pk)
        var_delete_conn_details.delete()
        return Response({
            'message': 'Report Deleted Successfully'
        })
    
