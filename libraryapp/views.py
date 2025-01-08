from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Book section

class BookDetails(APIView):
    def post(self,request):
        serializer = BookSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Book added successfully","data":request.data})
        
        return Response({"message":"Error occured when uploading","error":serializer.errors})
    
    def get(self,request,book_id = None):
        if book_id:
            try:
                book = Book.objects.get(id=book_id)
                serializer = BookSerializers(book)
                return JsonResponse(serializer.data,safe=False)
            except Exception as e:
                return Response(
                    {"error": "Book not found"}
                )
        else:
            book = Book.objects.all()
            serializer = BookSerializers(book,many= True)
            return JsonResponse(serializer.data,safe=False)
        
    
        
    
    
class UserDetails(APIView):
    def post(self,request):
        serializer = UserSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User added successfully","data":request.data})
        
        return Response({"message":"Error occured when adding","error":serializer.errors})
    
    def get(self,request,book_id = None):
        if book_id:
            try:
                book = Book.objects.get(id=book_id)
                serializer = BookSerializers(book)
                return JsonResponse(serializer.data,safe=False)
            except Exception as e:
                return Response(
                    {"error": "Book not found"}
                )
        else:
            book = Book.objects.all()
            serializer = BookSerializers(book,many= True)
            return JsonResponse(serializer.data,safe=False)
        
        
class BookBorrow(APIView):
    def post(self, request):
        book= request.data.get('book')
        
        # Ensure that the book_id is present in the request data
        if not book:
            return Response({"message": "Book ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Try to fetch the book from the database
            book_data = Book.objects.get(id=book)
        except Book.DoesNotExist:
            # Return an error response if the book does not exist
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Check if there are available copies of the book
        book_length = book_data.available_copies
        if book_length <= 0:
            # Return a message if there are no available copies
            return Response({"message": "No available copies"}, status=status.HTTP_400_BAD_REQUEST)
        
        else:
            # Proceed with loan creation if copies are available
            load_serializer = LoanSerializers(data=request.data)
            if load_serializer.is_valid():
                load_serializer.save()  # Save the loan data
                # Return the serialized loan data on success
                book_data = Book.objects.get(id=book)
                book_data.available_copies =  book_data.available_copies-1
                book_data.save()
                return Response(load_serializer.data, status=status.HTTP_201_CREATED)
            
            # Return error message if serializer validation fails
            return Response({"message": "Error occurred when adding", "error": load_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
                    