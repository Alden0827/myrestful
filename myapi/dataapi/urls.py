from django.urls import path
from .views import SummaryDataView, SensitiveDataView, ConfidentialDataView, DataEntryListCreateView,DataEntryDetailView

urlpatterns = [
    path('data/summary/', SummaryDataView.as_view(), name='summary'),  # Public
    path('data/sensitive/', SensitiveDataView.as_view(), name='sensitive'),  # Restricted Origin
    path('data/confidential/', ConfidentialDataView.as_view(), name='confidential'),  # Requires Token

    # CRUD API endpoints
    path('data/', DataEntryListCreateView.as_view(), name='data-list-create'),  # List & Create
    path('data/<int:pk>/', DataEntryDetailView.as_view(), name='data-detail'),  # Retrieve, Update, Delete

]