from django.urls import path
from . import views

urlpatterns = [
    path('', views.TemplateView.as_view(
        template_name='detailView/home.html'), name="blankhome"),
    path('home/', views.RedirectView.as_view(url='/'), name="home"),
    path('youtube/', views.RedirectView.as_view(pattern_name='youtube2'), name="youtube"),
    
    # path('youtube2/<int:pk>', views.NewYoutubeRedirectView.as_view(), name="youtube2"),
    # path('roll/<int:pk>', views.TemplateView.as_view(template_name='detailView/profile2.html'), name='mindex'),
    
    
    path('youtube2/<slug:post>', views.NewYoutubeRedirectView.as_view(), name="youtube2"),
    path('roll/<slug:post>', views.TemplateView.as_view(template_name='detailView/profile2.html'), name='mindex'),

    path('pupilslist/', views.ListPupils.as_view(), name='pupilsList'),
    path('pupilslist/<int:pk>', views.PupilsDetailView.as_view(), name='per_pupil'),
    path('fmView/', views.StdFormView.as_view(), name='formViewShow'),

    path('thankyou/', views.ThanksTemplateView.as_view(), name='thankyou'),
    path('createView/', views.CreateViewPupil.as_view(), name='createView'),
    path('singleDataView/<int:pk>', views.SigleDataDetail.as_view(), name='singleDataView'),
    path('DataUpdateView/<int:pk>', views.SingleDataUpdate.as_view(), name='DataUpdateView'),
    path('DataDeleteView/<int:pk>', views.SingleDataDel.as_view(), name='DataDeleteView'),
    path('deleteForm/', views.TemplateView.as_view(template_name='deleteView/delete.html'), name='deleteForm'),

    path('profile/', views.TemplateView.as_view(template_name='deleteView/registration.profile.html'), name='profile')



]
