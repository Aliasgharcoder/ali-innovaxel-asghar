import random, string
from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .serializers import ShortURLSerializer

def generate_unique_shortcode(length=6):
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if not ShortURL.objects.filter(short_code=code).exists():
            return code

class ShortenURLView(APIView):
    def post(self, request):
        serializer = ShortURLSerializer(data=request.data)
        if serializer.is_valid():
            original_url = serializer.validated_data['original_url']
            short_code = generate_unique_shortcode()
            short_url_obj = ShortURL.objects.create(original_url=original_url, short_code=short_code)
            response_serializer = ShortURLSerializer(short_url_obj)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RedirectURLView(APIView):
    def get(self, request, short_code):
        url_obj = get_object_or_404(ShortURL, short_code=short_code)
        url_obj.access_count += 1
        url_obj.save()
        return redirect(url_obj.original_url)
class URLStatsView(APIView):
    def get(self, request, short_code):
        url_obj = get_object_or_404(ShortURL, short_code=short_code)
        data = {
            "original_url": url_obj.original_url,
            "short_code": url_obj.short_code,
            "created_at": url_obj.created_at,
            "access_count": url_obj.access_count,
        }
        return Response(data, status=status.HTTP_200_OK)
class DeleteURLView(APIView):
    def delete(self, request, short_code):
        url_obj = get_object_or_404(ShortURL, short_code=short_code)
        url_obj.delete()
        return Response({"message": "Short URL deleted"}, status=status.HTTP_204_NO_CONTENT)
class UpdateURLView(APIView):
    def put(self, request, short_code):
        url_obj = get_object_or_404(ShortURL, short_code=short_code)
        new_url = request.data.get("original_url")
        if new_url:
            url_obj.original_url = new_url
            url_obj.save()
            return Response(ShortURLSerializer(url_obj).data)
        return Response({"error": "New URL required"}, status=status.HTTP_400_BAD_REQUEST)
