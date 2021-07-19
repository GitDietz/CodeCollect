import django_filters

from .models import Code, Appfeature

class CodeFilter(django_filters.FilterSet):
    class Meta:
        model = Code
        fields = {
            'extract': ['icontains', ],
            'code': ['icontains', ],
            'tags__tag' : ['icontains', ],
        }


class FeatureFilter(django_filters.FilterSet):
    class Meta:
        model = Appfeature
        fields = {
            'description': ['icontains', ],
            'last_bug': ['icontains', ],
        }
