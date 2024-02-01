from django.shortcuts import get_object_or_404, render, HttpResponse
from  . models import Contact, Product, Request, Category
# from  . models import Category
import logging
from django.contrib import messages
from django.core.paginator import Paginator


# Get an instance of a logger
logger = logging.getLogger(__name__)

from math import ceil
# Create your views here.


def search(request):
    query = request.GET['query']
    if len(query)>78:
        products = []
    else:
        productsName = Product.objects.filter(name__icontains=query)
        productsDesc = Product.objects.filter(desc__icontains=query)
        # productsCat = Product.objects.filter(category__icontains=query)
        products =  productsName.union(productsDesc)
       


    # if products.count() == 0:
    #     messages.error(request, "Please Search Correctly")
    context = {
        'products': products,
        'query' : query
    }    
    return render(request, 'search.html', context)







def index(request):
    products = Product.objects.all()
    # products = products.downloads + 1
    # products.save()
    context = {
        'products': products
    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject','')
        message = request.POST.get('message', '')

        if len(name)<2 or len(email)<3 or len(subject)<10 or len(message)<4:
            messages.error(request, "Please fill the form correctly.")
        else:
            contact = Contact(name=name, email=email, message=message, subject=subject)
            contact.save()
            messages.success(request, " Your message has been submited.")
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

# def books(request):
#     return render(request, "books.html")


def request_page(request):
    if request.method=="POST":
        name = request.POST.get('rname', '')
        email = request.POST.get('remail', '')
        message = request.POST.get('rmessage', '')

        if len(name)<2 or len(email)<3 or len(message)<4:
            messages.error(request, "Please fill the form correctly.")
        else:
            request_all = Request(name=name, email=email, message=message)
            request_all.save()
            messages.success(request, " Your message has been submited.")

    return render(request, "request.html")


# def science(request):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, 'c_science.html', context)

# def productView(request, myid):
#     # Fetch the product using the id
#     product = Product.objects.filter(id=myid)


#     return render(request, 'shop/prodView.html', {'product':product[0]})


# def history(request):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, 'history.html', context)

# def education(request):
#     products = Product.objects.all()
#     context = {
#         'products': products
#     }
#     return render(request, 'education.html', context)


def categories(request):
    categories = Category.objects.order_by('name')
    context = {
        'categories': categories
    }
    return render(request, 'category_list.html', context)

def category(request, category_id):
    category = get_object_or_404(Category, pk = category_id)
    ebooks = category.product_set.all()

    paginator = Paginator(ebooks, 12)
    try:
        page = request.GET['page']
    except:
        page = 1
    ebooks = paginator.get_page(page)
    context = {
		'category' : category,
		'ebooks' : ebooks
		}

    return render(request, 'category.html',context)

def ebooks(request):
    products = Product.objects.all()
    paginator = Paginator(products, 12)
    try:
        page = request.GET['page']
    except:
        page = 1
    ebooks = paginator.get_page(page)
    return render(request, 'ebooks.html', {
		'products': products,
		})

def ebook(request, book_id):
    products = get_object_or_404(products, pk = book_id)
    return render(request, 'productView.html', {
		'products' : products,
        
		})