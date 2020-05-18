from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from base.serializers import PostSerializer
from base.models import Post


class TestView(APIView):

    # permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        # post = qs.first()
        # serializer = PostSerializer(post)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
