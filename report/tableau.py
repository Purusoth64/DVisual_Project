# from tableau_api_lib import TableauServerConnection
# from tableau_api_lib.utils import querying, flatten_dict_column
# import PyPDF2
# from minio import Minio
# import io
# import random as r

# minio_client = Minio ("18.217.196.203:9000",
#                     "kBSeUX6rAW9Fj8LdohLi",
#                     "TNoS9XNLbXOv1LQTcH7Lsi9DXivlWN0oF4ApaKFT",
#                     secure=False)
# link=[]
# class TableauConnector:
    
#     def __init__(self, config):
#         self.config = config
#         self.conn = None
#         self.pdf_url=None
#         self.s=None

#     def connect_to_tableau_server(self):
#         # Establish a connection to Tableau Server
#         self.conn = TableauServerConnection(self.config, env='tableau_online')
#         self.conn.sign_in()
#         print("Signed in Successfully")

#     def get_workbook_views(self, workbook_name):
#         # Retrieve the views associated with a given workbook
#         views_df = querying.get_views_dataframe(self.conn)
#         views_df = flatten_dict_column(views_df, keys=["name", "id"], col_name="workbook")
#         relevant_views_df = views_df[views_df["workbook_name"] == workbook_name]
#         return relevant_views_df['id'].tolist()

#     def download_workbook_as_pdf(self, workbook_name):
#         # Set parameters for PDF export
#         pdf_params = {
#             "pdf_orientation": "orientation=Landscape",
#             "pdf_layout": "type=A4"
#         }
#         pdf_writer = PyPDF2.PdfWriter()

#         view_ids = self.get_workbook_views(workbook_name)

#         # Iterate through the view IDs
#         for view_id in view_ids:
#             # Query the PDF content for each view
#             view_pdf = self.conn.query_view_pdf(view_id=view_id, parameter_dict=pdf_params)
#             pdf_content = io.BytesIO(view_pdf.content)
#             pdf_reader = PyPDF2.PdfReader(pdf_content)

#             # Append each page of the PDF to the writer
#             for page_number in range(len(pdf_reader.pages)):
#                 page = pdf_reader.pages[page_number]
#                 pdf_writer.add_page(page)

#         # Save the combined PDF file
#         pdf_bytes = io.BytesIO()
#         pdf_writer.write(pdf_bytes)
#         pdf_bytes.seek(0)

#         #creating random file name for minio 
#         link="workbook_"
#         m=r.randint(10,1000)
#         s=str(link)+str(m)


#         minio_client.put_object("d-visual",f"{s}.pdf", pdf_bytes, len(pdf_bytes.getvalue()))
    
#         pdf_url = minio_client.presigned_get_object("d-visual", f"{s}.pdf")
#         link.append(pdf_url)
#         print(pdf_url)
#         print("Tableau workbook as a PDF file is downloaded successfully")


#--------------------------------------
        # data = dvisual_config_detail.objects.filter(id=1).values('conn_str')
        # data_1 = dvisual_report_api.objects.get()
        # print(data_1)
        # print('this is data', data)
        # source = data[0]
        # # print('this is source', source)
        # sources = source['conn_str']
        # print(sources)
 #---------------------------------------------

#--------------------------------------------------------------------------------------------------------------
# request.session['response_data'] = response_data
        
# return Response(response_data, status=status.HTTP_201_CREATED)



# def get(self, request, *args, **kwargs):
#         # # Retrieve response_data from session or cache
        
                
#             response_data = request.session.get('response_data', {})
                
#             return Response({"response_data":response_data}, status=status.HTTP_200_OK)

