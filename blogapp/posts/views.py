from django.shortcuts import render
from .models import Post,Author,Category
from marketing.models import Signup
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def index(request):
    featured = Post.objects.filter(featured =True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    print(latest)
    if request.method == 'POST':
        email =request.POST['email']
        new_signup = Signup()
        new_signup.email =email
        new_signup.save()
    context = {
        'object_list':featured , 
        'latest':latest,
    }
    return render(request,'index.html',context)

def blog(request):

    post_list = Post.objects.all()
    paginator = Paginator(post_list,4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    print(page)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
        
    except EmptyPage :
        paginated_queryset = paginator.page(paginator.num_pages)
    context ={ 'queryset' : paginated_queryset , 'page_request_var' : page_request_var,
     }

    return render(request,'blog.html',context)

def post(request):
    return render(request,'post.html',{})