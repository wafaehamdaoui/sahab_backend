from django.shortcuts import get_object_or_404, render
from .models import Report, Image, Counter
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from rest_framework import generics
from .serializers import CounterSerializer, ReportSerializer, ImageSerializer, UserSerializer
# Create your views here.

class CounterList(generics.ListAPIView):
    serializer_class = CounterSerializer
    queryset = Counter.objects.all()

class CounterDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CounterSerializer
    queryset = Counter.objects.all()

class ImageList(generics.ListAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()

class ReportList(generics.ListAPIView):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()

class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()
 
class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # field = User.groups.name

class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
          
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)

def create_report(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        id = 1
        # Perform logic to create a report using the provided data
        # Return a JSON response with the created report data
        return JsonResponse({'report_id': id})
    
def take_screenshot(request):
    # Perform logic to take a screenshot and store it as an Image object
    # Return a JSON response indicating the success/failure of the operation
    return JsonResponse({'success': True}) 

def edit_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if request.method == 'POST':
        updated_data = request.POST.get('updatedData')
        # Perform logic to edit the report using updated_data
        # Return a JSON response with the updated report data
        return JsonResponse({'report_id': report.id})  

def delete_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if request.method == 'POST':
        # Perform logic to delete the report
        # Return a JSON response indicating the success/failure of the operation
        return JsonResponse({'success': True})
    
def delete_screenshot(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        # Perform logic to delete the screenshot
        # Return a JSON response indicating the success/failure of the operation
        return JsonResponse({'success': True})
    
def store_screenshot(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    if request.method == 'POST':
        # Perform logic to store the screenshot data
        # Return a JSON response indicating the success/failure of the operation
        return JsonResponse({'success': True})


