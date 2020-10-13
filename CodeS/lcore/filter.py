import django_filters

from .models import Code

class CodeFilter(django_filters.FilterSet):
    class Meta:
        model = Code
        fields = {
            'extract': ['icontains', ],
            'code': ['icontains', ],
            'tags__tag' : ['icontains', ],
        }

