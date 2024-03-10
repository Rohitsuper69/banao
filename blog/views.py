from django.shortcuts import render, redirect
from users.models import CustomUser
from .forms import BlogForm
from .models import Blog
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def dashboard_view(request):
    try:
        data = CustomUser.objects.filter(user=request.user).values()
        context={
            'user': request.user,
            'is_patient':data[0]["is_patient"],
            'is_doctor':data[0]["is_doctor"],
            'address':data[0]["address_line1"],
            'city':data[0]["city"],
            'state':data[0]["state"],
            'pincode':data[0]["pincode"],
            'img':data[0]["profile_picture"]
        }
    except: 
        context={}
    return render(request, 'dashboard.html',context)

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user  # Assuming you have authentication in place
            blog.save()
            # return redirect('blog_detail', blog_id=blog.id)  # Redirect to the blog detail page
            return redirect("dashboard")
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})

def view_blog(request):
    categories = Blog.objects.values_list('Category', flat=True).distinct()
    categorized_blogs = {}
    for category in categories:
        categorized_blogs[category] = Blog.objects.filter(Category=category)
    return render(request, 'view_blog.html', {'categorized_blogs': categorized_blogs})

def viewmy_blog(request):
    blogs = Blog.objects.filter(user=request.user)
    # for blog in blogs:
    #     if len(blog.Summary.split()) > 15:
    #         blog.Summary = ' '.join(blog.Summary.split()[:15]) + ' ...'
    context={
        'blogs': blogs
    }
    return render(request, 'viewmy_blog.html',context)