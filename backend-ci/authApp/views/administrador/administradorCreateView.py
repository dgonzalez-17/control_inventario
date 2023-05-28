from rest_framework import status, views
from rest_framework.response import Response
from authApp.serializers.administradorSerializer import AdministratorSerializer
from authApp.models.administrador import Administrator


class AdministratorCreateView(views.APIView):
    def post(self, request,*args, **kwargs):
        serializer = AdministratorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
            