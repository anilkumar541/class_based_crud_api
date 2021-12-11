from myapp import views
from django.urls import path


urlpatterns = [
    path("", views.CategoryListView.as_view(), name="category"),
    path("category/<int:pk>/", views.CategioryDetailView.as_view(), name="get_category_id"),
    path("create/", views.CategoryCreateView.as_view(), name="create_category"),
    path("update/<int:pk>/", views.CategoryUpdateView.as_view(), name="update_category"),
    path("delete/<int:pk>/", views.CategoryDeleteView.as_view(), name="delete_category")
]
