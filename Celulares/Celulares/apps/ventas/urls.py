from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('Celulares.apps.ventas.views',
		url(r'^add/celular/$','add_product_view',name = 'vista_agregar_producto'),
		url(r'^edit/celular/(?P<id_prod>.*)/$','edit_producto_view', name = 'vista_editar_producto'),
		
	)