from django.contrib import admin

from .models import Profile, Departamento, Message


class ProfileModelAdmin(admin.ModelAdmin):
	list_display = [ "id", "user", "rut", "birthdate", "departamento", "inicio_cargo", ]
	list_display_links = ["user"]
	list_editable = ["departamento", "rut", ]
	list_filter = [ "departamento", "rut", ]

	search_fields = ["user", "rut", "departamento", ]
	class Meta:
		model = Profile

class DepartamentoModelAdmin(admin.ModelAdmin):
	list_display = ["id", "nombre", "descripcion",]
	list_editable = ["nombre", "descripcion",]
	list_filter = ["nombre",]

	search_fields = ["nombre",]
	class Meta:
		model = Departamento

class MessageModelAdmin(admin.ModelAdmin):
	list_display = ["id", "user", "emisor_nn", "emisor", "receptor", "fecha_inicio", "fecha_fin", "estado", "cod_valid",]
	list_editable = ["emisor_nn", "emisor", "receptor", ]
	list_filter = ["emisor_nn", "emisor", "receptor", "fecha_inicio", "fecha_fin", ]

	search_fields = ["receptor", "emisor",]
	class Meta:
		model = Message





admin.site.register(Profile, ProfileModelAdmin)
admin.site.register(Departamento, DepartamentoModelAdmin)
admin.site.register(Message, MessageModelAdmin)

