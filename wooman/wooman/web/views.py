from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ModelViewSet
from wooman.web.models import WomanModel
from wooman.web.permissions import CustomAuthenticated
from wooman.web.serializers import WomanSerializer


class WomenViewSet(ModelViewSet):
    serializer_class = WomanSerializer
    # permission_classes = [CustomAuthenticated]
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return WomanModel.objects.all()[:3]
        return WomanModel.objects.filter(pk=pk)
# class WomanAPIView(generics.ListCreateAPIView):
#     queryset = WomanModel.objects.all()
#     serializer_class = WomanSerializer


# class WomanView(APIView):

    # def get(self, request):
    #     woman = WomanModel.objects.all()
    #     serializer = WomanSerializer(woman, many=True)
    #     return Response({'get': serializer.data})
    #
    # def post(self, request):
    #     serializer = WomanSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'post': serializer.data})
    #
    # def put(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk', None)
    #     if not pk:
    #         return Response({'error': 'Method PUT not allowed'})
    #     try:
    #         instance = WomanModel.objects.get(pk=pk)
    #     except:
    #         return Response({'error': 'Method PUT not allowed'})
    #
    #     serializer = WomanSerializer(data=request.data, instance=instance)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({'put': serializer.data})
