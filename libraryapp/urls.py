
from django.urls import path
from libraryapp.views import *


urlpatterns = [
  path('BookDetails/',BookDetails.as_view(),name="BookDetails"),
  path('UserDetails/<int:book_id>/',UserDetails.as_view(),name="UserDetails"),
  path('BookBorrow/',BookBorrow.as_view(),name="BookBorrow"),
]