from datetime import timedelta
from django.db import models
from django.urls import reverse
from django.utils import timezone


# ## Model Managers ## #
class ArticleManager(models.Manager):
    def all(self):
        qs = super(ArticleManager, self).all()
        return qs

    def published(self):
        qs = super(ArticleManager, self).filter(draft=False)
        return qs

    def visible(self):
        qs = super(ArticleManager, self).filter(draft=False).filter(visible=True)
        return qs

    def recent_five(self):
        qs = super(ArticleManager, self).filter(draft=False).filter(visible=True).order_by('-date_added')[:5]
        return qs


class AuthorManager(models.Manager):
    def all(self):
        qs = super(AuthorManager, self).all()
        return qs


class CategoryManager(models.Manager):
    def all(self):
        qs = super(CategoryManager, self).all()
        return qs

    def active(self):
        qs = super(CategoryManager, self).filter(active=True)
        return qs


class CodeManager(models.Manager):
    def all(self):
        qs = super(CodeManager, self).all()
        return qs

    def by_tag(self, tag):
        qs = super(CodeManager, self).filter(Tags=tag)
        return qs


class RefManager(models.Manager):
    def all(self):
        qs = super(RefManager, self).all()
        return qs

    def primary(self):
        qs = super(RefManager, self).order_by('primary')[:1]
        return qs


class ServicesManager(models.Manager):
    def all(self):
        qs = super(ServicesManager, self).all()
        return qs

    def top_five(self):
        qs = super(ServicesManager, self).order_by('priority')[:5]
        return qs


class TagManager(models.Manager):
    def all(self):
        qs = super(TagManager, self).all()
        return qs

    def active(self):
        qs = super(TagManager, self).filter(active=True)
        return qs


class CustomerManager(models.Manager):
    def all(self):
        qs = super(CustomerManager, self).all()
        return qs

    def active(self):
        qs = super(CustomerManager, self).filter(active=True)
        return qs


class FeatureManager(models.Manager):
    def all(self):
        qs = super(FeatureManager, self).all()
        return qs

    def active(self):
        qs = super(FeatureManager, self).filter(active=True)
        return qs


class SkillManager(models.Manager):
    def all(self):
        qs = super(SkillManager, self).all()
        return qs

    def active(self):
        qs = super(SkillManager, self).filter(active=True)
        return qs


class ProcessManager(models.Manager):
    def all(self):
        qs = super(ProcessManager, self).all()
        return qs

    def active(self):
        qs = super(ProcessManager, self).filter(active=True)
        return qs


# AppFeatureManager
class AppFeatureManager(models.Manager):
    def all(self):
        qs = super(AppFeatureManager, self).all()
        return qs

    def bugs(self):
        qs = super(AppFeatureManager, self).filter(bug=True)
        return qs

    def no_bugs(self):
        qs = super(AppFeatureManager, self).filter(bug=False)
        return qs

    def old_test(self):
        before_time = timezone.now() - timedelta(days=21)
        qs = super(AppFeatureManager, self).filter(last_test__lte=before_time)
        return qs


# ####################### Models ###################### #
class Author(models.Model):
    """
    The author identified for an article or code
    """
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=True)
    objects = AuthorManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.title()


class Tag(models.Model):
    """
    Holder of the technology items employed
    """
    tag = models.CharField(max_length=30, unique=True)
    active = models.BooleanField(default=True)
    objects = TagManager()

    def __str__(self):
        return self.tag.title()


class Category(models.Model):
    """
    Items of process, e.g. Process analysis, UI, Development
    """
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=True)
    objects = CategoryManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.title()


class Article(models.Model):
    """
    Short article
    setting project = True makes it a project description
    """

    author = models.CharField(max_length=100, unique=False)
    caption = models.CharField(max_length=50, unique=False)
    extract = models.CharField(max_length=300)
    story = models.TextField(blank=False)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    draft = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    image_file = models.FileField(upload_to='blog_image', blank=True, null=True)
    article_file = models.FileField(upload_to='blog_article', blank=True, null=True)
    project = models.BooleanField(default=False)
    objects = ArticleManager()

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.caption.title()


class Process(models.Model):
    """
    automtion project
    """
    process = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300, unique=False)
    active = models.BooleanField(default=True)
    objects = ProcessManager()

    class Meta:
        ordering = ['process']
        verbose_name_plural = 'Processes'

    def __str__(self):
        return self.process.title()


class Code(models.Model):
    """
    Code segment
    setting project = True makes it a project description
    """

    author = models.ManyToManyField(Author, blank=False)
    extract = models.CharField(max_length=300)
    code = models.TextField(blank=False)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    draft = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True)
    process = models.ManyToManyField(Process, blank=True)
    article_file = models.FileField(upload_to='blog_article', blank=True, null=True)
    objects = CodeManager()

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.extract.title()

    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={"id": self.id})


class Reference(models.Model):
    company = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    primary = models.IntegerField(null=False, unique=True)
    objects = RefManager()

    def __str__(self):
        return self.company.title()


class Services(models.Model):
    """
    Services offered by the unit
    """
    service = models.CharField(max_length=100, unique=True)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    priority = models.IntegerField(null=False, unique=True)
    image_file = models.FileField(upload_to='service_icon', blank=True, null=True)
    descrip = models.CharField(max_length=300, blank=True, null=True)
    objects = ServicesManager()

    class Meta:
        ordering = ['priority']
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.service.title()


class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    sector = models.CharField(max_length=50, unique=False, blank=True, null=True)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    image_file = models.FileField(upload_to='service_icon', blank=True, null=True)
    descrip = models.CharField(max_length=300, blank=True, null=True)
    active = models.BooleanField(default=True)
    objects = CustomerManager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.title() or self.sector.title()


class Feature(models.Model):
    """
    Features or benefits aimed for
    """
    feature = models.CharField(max_length=50, unique=True)
    image_file = models.FileField(upload_to='feature_icon', blank=True, null=True)
    descrip = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)
    objects = FeatureManager()

    class Meta:
        ordering = ['feature']

    def __str__(self):
        return self.feature.title()


class Skill(models.Model):
    """
    skills of the team
    """
    skill = models.CharField(max_length=50, unique=True)
    descrip = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)
    objects = SkillManager()

    class Meta:
        ordering = ['skill']

    def __str__(self):
        return self.skill.title()


# ####################### Application ###################### #
class Appfeature(models.Model):
    """
    Contains the features of the particular application
    This can be used for trcking and testing
    """
    description = models.CharField(max_length=200, blank=False, unique=True)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_test = models.DateTimeField(auto_now=False, auto_now_add=False)
    last_bug = models.CharField(max_length=200, blank=False, unique=False)
    bug = models.BooleanField(default=False)
    objects = AppFeatureManager()

    class Meta:
        ordering = ['bug', 'description']

    def __str__(self):
        return self.description.title()
