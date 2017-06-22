from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blogs', views.show_blogs, name='index1'),
    url(r'^submit', views.submit, name='submit'),
    url(r'^blogApp/investigate', views.investigate, name='investigate'),
    url(r'^blogApp/train_ticket', views.stores, name='train'),
    url(r'^blogApp/flight', views.flight, name='flight'),
    url(r'^images', views.show_images, name="show iamges"),
    url(r'^comments_upload/$', views.comments_upload, name="comments_upload"),
    url(r'^ajax_test/$', views.show_ajax_test_form, name="add"),
]