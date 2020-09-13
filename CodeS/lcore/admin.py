from django.contrib import admin

from .models import Services, Reference, Article, Category, Tag, Customer, Feature, Skill, Author, Code


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['caption', 'author', 'visible']

    class Meta:
        model = Article


admin.site.register(Article, ArticleAdmin)



class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Author


admin.site.register(Author, AuthorAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class CodeAdmin(admin.ModelAdmin):
    list_display = ['extract']

    class Meta:
        model = Code


admin.site.register(Code, CodeAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'sector']

    class Meta:
        model = Customer


admin.site.register(Customer, CustomerAdmin)


class FeatureAdmin(admin.ModelAdmin):
    list_display = ['feature', 'active']

    class Meta:
        model = Feature


admin.site.register(Feature, FeatureAdmin)


class RefAdmin(admin.ModelAdmin):
    list_display = ['company', 'primary']

    class Meta:
        model = Reference


admin.site.register(Reference, RefAdmin)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ['service', 'priority']

    class Meta:
        model = Services


admin.site.register(Services, ServicesAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'active']

    class Meta:
        model = Tag


admin.site.register(Tag, TagAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill', 'active']

    class Meta:
        model = Skill


admin.site.register(Skill, SkillAdmin)
