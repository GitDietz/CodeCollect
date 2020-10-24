import pathlib
from django.conf import settings as conf_settings
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.http import FileResponse
from django.shortcuts import render, redirect

from .email import send_email
from .filter import CodeFilter
from .forms import ContactForm
from .models import Services, Reference, Article, Category, Tag, Feature, Skill, Code, Process


def get_base_context():
    service_list = Services.objects.top_five()
    company = Reference.objects.get(primary=1)
    co_name = company.company
    co_addr = company.address
    co_country = company.country
    co_phone = company.phone
    co_email = company.email
    print(co_name)
    return {'service_list': service_list,
            'co_name': co_name,
            'co_addr': co_addr,
            'co_country': co_country,
            'co_phone': co_phone,
            'co_email': co_email,
            }


def get_direct_query_dict(sql_query):
    """
    build of a queryset by using a direct query for data set structures that are complex for the ORM
    right now it only creates a dict
    """
    with connection.cursor() as cursor:
        # sql = ("select C.id, C.extract, string_agg(T.tag, ',') as Tags from lcore_code as C left join "
        #        "lcore_code_tags as CT on C.id = CT.code_id inner join lcore_tag as T on CT.tag_id = T.id "
        #         "group by C.id order by C.id;")
        # print(sql)
        cursor.execute(sql_query)
        columns = [col[0] for col in cursor.description]
        out_qs = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    print(out_qs)
    return out_qs


def base(request):
    template = "base.html"
    context = {}
    return render(request, template, context)


def blog(request):
    template = "blog.html"
    active_articles = Article.objects.visible()
    recent_articles = Article.objects.recent_five()
    active_tags = Tag.objects.active()  # change to used
    with connection.cursor() as cursor:
        sql = ("Select C.name, count(C.name) as cat_count from lcore_article_category as JJ inner join"
               " lcore_category C on JJ.category_id = C.id group by name;")
        print(sql)
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        category_count = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    local_context = {
        'articles': active_articles,
        'recent_articles': recent_articles,
        'active_tags': active_tags,
        'category_count': category_count
    }

    context = {**get_base_context(), **local_context}
    print(context)
    return render(request, template, context)


def home(request):
    template = "home.html"
    services = Services.objects.all()[:6]
    local_context = {
        'services': services,
    }

    context = {**get_base_context(), **local_context}
    print(context)
    return render(request, template, context)


def pdf(request):
    root = pathlib.Path(conf_settings.MEDIA_ROOT)
    file_path = pathlib.Path.joinpath(root, 'blog_image', 'Email_processing.pdf')
    print(f'{file_path}')
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')


def show_pdf(request, pk):
    root = pathlib.Path(conf_settings.MEDIA_ROOT)
    try:
        article = Article.objects.get(pk=pk)
        filename = str(article.article_file)
    except:
        return redirect('lcore:blog')
    if filename == '':
        return redirect('lcore:blog')
    file_path = pathlib.Path.joinpath(root, filename)
    print(f'{file_path}')
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')


def services(request):
    template = "services.html"
    services = Services.objects.all()[:6]
    features = Feature.objects.active()[:8]
    local_context = {
        'services': services,
        'features': features,
    }

    context = {**get_base_context(), **local_context}
    return render(request, template, context)


def about(request):
    template = "about.html"
    services = Services.objects.all()[:6]
    features = Feature.objects.active()[:8]
    skill = Skill.objects.active()
    local_context = {
        'services': services,
        'features': features,
        'skill': skill,
    }

    context = {**get_base_context(), **local_context}
    return render(request, template, context)


def contact(request):
    """ process the form to sedn the email for enquiry """
    form = ContactForm()

    template_name = 'contact_page.html'

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            body = f'Enquiry from {data.get("full_name")}, regarding {data.get("content")}'
            email_kwargs = {'email': data.get('email'),
                            'subject': data.get('subject'),
                            'content': body,
                            }
            send_result, sender = send_email(**email_kwargs)
            if send_result != 0:
                messages.error(request, f"Your email could not be sent, please email us direct on {sender}")
            else:
                messages.success(request, "Your email was successfully sent")

            # TODO: setup messages to update this form as sent or failed

        # else:
        #     return redirect('home')

    local_context = {
        'form': form,
    }
    context = {**get_base_context(), **local_context}
    return render(request, template_name, context)

########################## Code related #############################

def code_list(request):
    """

    """
    get_dict = request.POST.copy()
    if not get_dict:
        get_dict = request.GET.copy()
        print('GET method tested')
    try:
        del get_dict['page']
    except KeyError:
        print('No page indicator on GET')

    codelist = Code.objects.all().order_by('extract').prefetch_related('tags').all()
    code_filtered = CodeFilter(get_dict, queryset=codelist)
    code_qs = code_filtered.qs
    page = request.GET.get('page', 1)
    paginator = Paginator(code_qs, 10)
    try:
        code_page = paginator.page(page)
    except PageNotAnInteger:
        code_page = paginator.page(1)
    except EmptyPage:
        code_page = paginator.page(paginator.num_pages)

    template = 'code_list.html'
    local_context = {
        'object_list': code_page,
        'filter_form': code_filtered,
        'notice': 'Some sort of notice',
    }

    context = {**get_base_context(), **local_context}
    return render(request, template, context)


def test(request):
    """
    just to test the build of a queryset
    """
    # related_qs = Code.objects.all()

    with connection.cursor() as cursor:
        sql = ("select C.id, C.extract, string_agg(T.tag, ',') as Tags from lcore_code as C left join "
               "lcore_code_tags as CT on C.id = CT.code_id inner join lcore_tag as T on CT.tag_id = T.id "
                "group by C.id order by C.id;")
        print(sql)
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        related_qs = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    print(related_qs)
    return redirect('lcore:code_list')


def experiments(request):
    sub_query = "select C.id, C.extract, string_agg(T.tag, ',') as Tags from lcore_code as C left join " \
                "lcore_code_tags as CT on C.id = CT.code_id inner join lcore_tag as T on CT.tag_id = T.id " \
                "group by C.id order by C.id;"
    new_query = "select C.id, string_agg(T.tag, ',') as Tags from lcore_code as C left join " \
                "lcore_code_tags as CT on C.id = CT.code_id inner join lcore_tag as T on CT.tag_id = T.id " \
                "group by C.id order by C.id;"
    # codelist = get_direct_query_dict()
    # codelist = Code.objects.all().order_by('extract').extra(select={ 'TagList': new_query},) not working
    # codelist = Code.objects.raw(sub_query) # yields the raw queryset type which does not work here
    # codelist = Code.objects.all()
    # code_ids = list(code_qs.values_list('id', flat=True))
    filter_query = new_query.replace("group","where C.id in (" +  ",".join(map(str,code_ids)) + ") group")
    tag_list = get_direct_query_dict(filter_query)

    #'tag_list': tag_list
    return None    

