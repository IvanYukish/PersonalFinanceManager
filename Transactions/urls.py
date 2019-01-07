from django.urls import path
from .views import list_transaction, create_transaction, delete_transaction, update_transaction,home_page

urlpatterns = [
    path('',home_page, name='home_page'),
    path('transaction', list_transaction, name='list_transaction'),
    path('newtransaction', create_transaction, name='create_transaction'),
    path('updatetr/<int:id>', update_transaction, name='update_transaction'),
    path('deletetr/<int:id>', delete_transaction, name='delete_transaction'),
]
