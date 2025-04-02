from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework import generics, permissions

# from django.http import JsonResponse
# from django.conf import settings
# from .models import DataEntry
# from .serializers import DataEntrySerializer

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import DataEntry
from .serializers import DataEntrySerializer

# ✅ Public API: No Token Required
class SummaryDataView(APIView):
    permission_classes = [AllowAny]  # Open to everyone

    def get(self, request):
        data = DataEntry.objects.all()[:10]  # Limit data to 10 entries
        serializer = DataEntrySerializer(data, many=True)
        return Response(serializer.data)

# ✅ Restricted API: Only accessible from allowed origins
class SensitiveDataView(APIView):
    def get(self, request):
        allowed_origins = settings.CORS_ALLOWED_ORIGINS
        if request.META.get('HTTP_ORIGIN') not in allowed_origins:
            return JsonResponse({"error": "Forbidden"}, status=403)

        data = DataEntry.objects.all()
        serializer = DataEntrySerializer(data, many=True)
        return Response(serializer.data)

# ✅ Secure API: Requires a Token to Access
class ConfidentialDataView(APIView):
    authentication_classes = [JWTAuthentication]  # Uses JWT tokens
    permission_classes = [IsAuthenticated]  # Only for authenticated users

    def get(self, request):
        data = DataEntry.objects.all()
        serializer = DataEntrySerializer(data, many=True)
        return Response(serializer.data)

# ✅ List & Create Data Entries
class DataEntryListCreateView(generics.ListCreateAPIView):
    queryset = DataEntry.objects.all()
    serializer_class = DataEntrySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]  # Requires a token

# ✅ Retrieve, Update, & Delete a Single Data Entry
class DataEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataEntry.objects.all()
    serializer_class = DataEntrySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]  # Requires a token