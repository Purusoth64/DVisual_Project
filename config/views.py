from rest_framework.views import APIView
from Dvisual_app.models import *
from rest_framework import status
from config.serializers import *
from rest_framework.response import Response



class Dvisual_Config_View(APIView):
    def get_user_by_pk(self, pk):
        try:
            return dvisual_config.objects.get(pk=pk)
        except:
            return Response({
                'error': 'does not exist'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):

        if pk:
            var_conn = self.get_user_by_pk(pk)
            var_serializer = dvisual_config_Serializer(var_conn)
            return Response([var_serializer.data])

        else:
            var_reg = dvisual_config.objects.all()
            var_serializer = dvisual_config_Serializer(var_reg, many=True)
            return Response(var_serializer.data)

    def post(self, request, format=None, pk=None ):
        data = request.data
        var_serializer = dvisual_config_Serializer(data=data)

        var_serializer.is_valid(raise_exception=True)

        var_serializer.save()

        response = Response()

        response.data = {
            'message': 'Dvisual_Config Created Successfully',
            'data': var_serializer.data
        }
        return response

    def put(self, request, pk=None, format=None):
        var_update_connection = dvisual_config.objects.get(pk=pk)
        var_serializer = dvisual_config_Serializer(instance=var_update_connection, data=request.data, partial=True)

        var_serializer.is_valid(raise_exception=True)

        var_serializer.save()

        response = Response()

        response.data = {
            'message': 'Dvisual_Config Updated Successfully',
            'data': var_serializer.data
        }

        return response


    def delete(self, request, pk, format=None):
        var_delete_connection = dvisual_config.objects.get(pk=pk)

        var_delete_connection.delete()

        return Response({
            'message': 'Dvisual_Config Deleted Successfully'
        })
