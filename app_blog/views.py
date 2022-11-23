from django.shortcuts import render , HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from app_blog.models import blog, comment, likes
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from app_blog.forms import CommentForm
import uuid
# Create your views here.




class CreateBlog(LoginRequiredMixin, CreateView):
    model = blog
    template_name = 'app_blog/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image',)
    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))


class BlogList(ListView):
    context_object_name = 'blogs'
    model = blog
    template_name = 'app_blog/blogList.html'
    queryset=blog.objects.order_by('-publish_date')



@login_required
def blog_details(request,id):
    ablog=blog.objects.get(pk=id)
    comment_form=CommentForm()
    already_liked = likes.objects.filter(blogc=ablog, user= request.user)
    if already_liked:
        liked = True
    else:
        liked = False
    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            com=comment_form.save(commit=False)
            com.user=request.user
            com.blogc=ablog
            com.save()
            return HttpResponseRedirect(reverse('app_blog:blog_details',kwargs={'id':id}))
    return render(request,'app_blog/blog_details.html',context={'blog':ablog, 'comment_form':comment_form, 'liked':liked})


@login_required
def liked(request, pk):
    ablog = blog.objects.get(pk=pk)
    user = request.user
    already_liked = likes.objects.filter(blogc=ablog, user=user)
    if not already_liked:
        liked_post = likes(blogc=ablog, user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('app_blog:blog_details', kwargs={'id':ablog.id}))



@login_required
def unliked(request, pk):
    ablog = blog.objects.get(pk=pk)
    user = request.user
    already_liked = likes.objects.filter(blogc=ablog, user=user)
    already_liked.delete()

    return HttpResponseRedirect(reverse('app_blog:blog_details', kwargs={'id':ablog.id}))
