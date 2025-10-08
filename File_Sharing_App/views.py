
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serilizer import UploadedFileSerializer

class FileUploadView(APIView):
    def post(self, request):
        serializer = UploadedFileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": 200,
                "message": "File uploaded successfully!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response({
            "status": 400,
            "message": "File upload failed!",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
