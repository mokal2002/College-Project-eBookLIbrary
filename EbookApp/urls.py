# from django.contrib import admin
# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="EbookAppHome"),
    path("search/", views.search, name="EbookAppSearch"),
    path("contact/", views.contact, name="Ebookcontact"),
    path("about/", views.about, name="Ebookabout"),
    path("request_page/", views.request_page, name="EbookRequestPage"),
    # path("science/", views.science, name="EbookScience"),
    # path("books/", views.books, name="Ebooks"),
    # path("history/", views.history, name="EbooksHistory"),
    # path("education/", views.education, name="EbooksEducation"),


    # path("products/<int:myid>", views.productView, name="ProductView"),
    path("categories/", views.categories, name="categories"),
    path("category/<int:category_id>", views.category, name="category"),
    path('ebooks/', views.ebooks, name='ebooks'),
    path('ebook/<int:book_id>', views.ebook, name='ebook'),
]