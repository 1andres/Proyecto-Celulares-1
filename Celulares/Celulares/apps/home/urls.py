from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('Celulares.apps.home.views',
	    url(r'^$','pagprincipal_view', name = 'vista_principal'),    
	    url(r'^about/$', 'about_view', name = 'vista_about'),
	    url(r'^contacto/$', 'contacto_view', name = 'vista_contacto'),
	    url(r'^login/$', 'login_view', name = 'vista_login'),
	    url(r'^logout/$', 'logout_view', name = 'vista_logout'),
	    url(r'^celulares/page/(?P<pagina>.*)/$','celulares_view', name = 'vista_celulares'),
		url(r'^celular/(?P<id_celular>.*)/$', 'single_celular_view', name = 'vista_celular'),	
	)	    