from django.shortcuts import render, get_object_or_404, redirect

from .models import Article, Category
from .forms import CategoryForm, ArticleForm, CommentForm


def article_list(request):
    articles = Article.objects.filter(published=True).select_related('category')
    categories = Category.objects.all()
    return render(request, 'blog/article_list.html', {
        'articles': articles,
        'categories': categories,
    })


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('blog:article_detail', article_id=article.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/article_detail.html', {
        'article': article,
        'comments': article.comments.all(),
        'form': form,
    })


def articles_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    articles = category.articles.filter(published=True)
    return render(request, 'blog/articles_by_category.html', {
        'category': category,
        'articles': articles,
    })


def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog:article_list')
    return render(request, 'blog/category_form.html', {'form': form})


def article_create(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog:article_list')
    return render(request, 'blog/article_form.html', {'form': form})
