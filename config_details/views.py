from django.http import Http404
from Dvisual_app.models import dvisual_config_detail
from rest_framework.views import APIView
from config_details.serializers import *
from rest_framework.response import Response



class Dvisual_Config_Detail_View(APIView):
    def get_object(self, pk):
            try:
                return dvisual_config_detail.objects.get(pk=pk)
            except dvisual_config_detail.DoesNotExist:
                raise Http404
    def get(self, request, pk=None, format=None):
        # var_pipeline_det_id= connection_detail.objects.filter(id=3).values('con_str')
        # print(var_pipeline_det_id)
        # temp_pd_id=pipeline_det_id[0]
        if pk:
                data = self.get_object(pk)
                var_serializer = Dvisual_Config_Details_Serializer(data)
                return Response([var_serializer.data])

        else:
                data = dvisual_config_detail.objects.all()
                var_serializer = Dvisual_Config_Details_Serializer(data, many=True)

                return Response(var_serializer.data)

    def post(self, request, format=None):
        data = request.data
        var_serializer = Dvisual_Config_Details_Serializer(data=data)

        var_serializer.is_valid(raise_exception=True)

        var_serializer.save()

        response = Response()

        response.data = {
            'message': 'Dvisual_Config_detail Created Successfully',
            'data': var_serializer.data
        }
        return response

    def put(self, request, pk=None, format=None):
        var_update_conn_details = dvisual_config_detail.objects.get(pk=pk)
        var_serializer = Dvisual_Config_Details_Serializer(instance=var_update_conn_details,data=request.data, partial=True)
        var_serializer.is_valid(raise_exception=True)
        var_serializer.save()
        response = Response()
        response.data = {
            'message': 'Dvisual_Config_detail Updated Successfully',
            'data': var_serializer.data
        }
        return response

    def delete(self, request, pk, format=None):
        var_delete_conn_details =  dvisual_config_detail.objects.get(pk=pk)
        var_delete_conn_details.delete()
        return Response({
            'message': 'Dvisual_Config_detail Deleted Successfully'
        })


