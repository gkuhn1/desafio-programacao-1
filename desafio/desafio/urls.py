from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^sales/import/$', 'app.sales.views.import_sales',
        name='sales_import'),
)
