from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from report.serializers import *
from Dvisual_app.models import *
from django.http.response import Http404
import pdb

class Get_Api(APIView):
    def get_object(self, pk):
        try:
            return d_link.objects.get(pk=pk)
        except d_link.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            # id=request.data.get('dvisual_report_id')
            # data = dvisual_config_detail.objects.get(id=id)
            # sources = data.conn_str

            data = self.get_object(pk)
            var_serializer = D_link_Serializer(data)
            return Response([var_serializer.data])
            
        else:
            data = d_link.objects.all()
            var_serializer = D_link_Serializer(data, many=True)
            return Response([var_serializer.data])
#-------------------------------------------------------------------------------------------------------
    def post(self, request, format=None):
        data = request.data
        link_1=["http://18.217.196.203:9000/d-visual/{s}.pdf"]
        dvisual_report_data={"r_link":link_1[-1]}
        combined_data = {**data, **dvisual_report_data}
        var_serializer = Dvisual_Report_Serializer(data=combined_data)

        var_serializer.is_valid(raise_exception=True)
        var_serializer.save()

        return Response('Link Stored Sucessfully')

        # pdb.set_trace()
        # workbook_name=var_serializer.data['workbook_name']
        # print(workbook_name)
        # id=request.data.get('dvisual_config_detail_id')
        # data = dvisual_config_detail.objects.get(id=id)
        # source = data.conn_str
    
        # print(source)
        # response = Response()
        
    #     response.data = {
    #         'message': 'Report Created Successfully',
    #         'data': var_serializer.data
    #     }
    #     return response
    

    # def post(self, request, format=None):
    #     try:
    #         # Get the 'id' from the request data (you need to send it with your POST request)
    #         id = request.data.get('')
            
    #         # Retrieve the config detail using the provided ID
    #         config = dvisual_config_detail.objects.get(id=id)
    #         source = config.conn_str
            
    #         return Response({'message': source})
    #     except dvisual_config_detail.DoesNotExist:
    #         return Response({'error': 'Config not found'}, status=404)


        






    # def post(self, request, pk=None, format=None):
    # # Get the 'id' from the request data
    #     try:

    #         if pk:
    #             data = dvisual_config_detail.objects.filter(id=pk).values('conn_str')
                
    #             if data:
    #                 source = data[0]
    #                 sources = source['conn_str']
    #                 print('conn_str:', sources)
    #                 return Response({'message': sources})
    #             else:
    #                 return Response({'message': 'No data found for the provided ID'})
    #         else:
    #             return Response('no data')
    
    #     except dvisual_report_api.DoesNotExist:
    #             raise Http404
