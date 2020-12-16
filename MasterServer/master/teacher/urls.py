from django.urls import path

from . import views, search, detail

urlpatterns = [
    path('types', views.dispatcher),
    path('search', search.search_all),
    path('detail', search.get_detail),
    path('course_view.html', detail.viewHtml),
]