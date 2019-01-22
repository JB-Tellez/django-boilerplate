from django.urls import path
from .views import (
    FooListView,
    FooDetailView,
    FooCreateView,
)

urlpatterns = [
    path('foo', FooListView.as_view(), name='foo_list'),
    path('foo/<int:id>', FooDetailView.as_view(), name='foo_detail'),
    path('foo/add', FooCreateView.as_view(), name='foo_add'),
]
