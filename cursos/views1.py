from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializers import CrusoSerializer, AvaliacaoSerializer


class CursoApiView(APIView):
    """
    API De Cursos da Geek
    """
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CrusoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CrusoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"id": serializer.data['id'], "curso": serializer.data['titulo']}, status=status.HTTP_201_CREATED)

class AvaliacaoApiView(APIView):
    """
    API De Avaliacoes da Geek
    """
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serialize = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serialize.data)

    def post(self, request):
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
