from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Data
from .serializers import DataSerializer


class DataView(APIView):
    def get(self, request):
        infos = Data.objects.all()
        serializer = DataSerializer(infos, many=True)
        return Response({"infos": serializer.data})

