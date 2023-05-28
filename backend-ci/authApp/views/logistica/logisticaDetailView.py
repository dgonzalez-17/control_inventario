from rest_framework import status, permissions, viewsets, views
from authApp.models.logistica import Logistic
from rest_framework.response import Response
from authApp.serializers.logisticaSerializer import LogisticSerializer

class LogisticDetailView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LogisticSerializer

    def get(self, request, *args, **kwargs): 
        logistic = Logistic.objects.all()
        serializer = self.serializer_class(instance=logistic,many=True)   
        return Response(serializer.data, status=status.HTTP_200_OK)
        
