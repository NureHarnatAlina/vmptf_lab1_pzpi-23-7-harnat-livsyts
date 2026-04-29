from django.test import TestCase

from .models import Category, Article, Comment


class CategoryArticleTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Технології',
            description='Статті про технології та програмування',
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Технології')

    def test_assign_article_to_category(self):
        article = Article.objects.create(
            title='Що нового у Django',
            content='Текст статті',
            category=self.category,
        )
        self.assertEqual(article.category, self.category)
        self.assertIn(article, self.category.articles.all())

    def test_category_unique_name(self):
        with self.assertRaises(Exception):
            Category.objects.create(name='Технології', description='Дублікат')


class CommentTests(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title='Тестова стаття',
            content='Текст',
        )

    def test_add_comment_to_article(self):
        comment = Comment.objects.create(
            article=self.article,
            author='Іван',
            text='Чудова стаття!',
        )
        self.assertEqual(comment.article, self.article)
        self.assertIn(comment, self.article.comments.all())
        self.assertIsNotNone(comment.created_at)

    def test_comment_cascade_on_article_delete(self):
        Comment.objects.create(article=self.article, author='Петро', text='ок')
        self.article.delete()
        self.assertEqual(Comment.objects.count(), 0)
