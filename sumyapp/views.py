from django.shortcuts import render

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import MessageForm
from .models import Message

from django.db.models import Count

from django.contrib import messages

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if not request.user.is_authenticated():

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/inicio")
    return render(request, "login.html", {"form":form})



def logout_view(request):
    logout(request)
    return redirect("/")


def home(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	else:
		return HttpResponseRedirect('/inicio')


def principal(request):
	obj_all = Message.objects.all().order_by("-fecha_inicio")

	count = Message.objects.all().count()
	obj = Message.objects.filter(cod_valid=count - 1)
	obj_new = Message.objects.get(id=obj)


	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')

	context = {
	"obj_all" : obj_all,
	"obj_new": obj_new,
    }	
	return render(request, "index.html", context)


def create_message(request):
	count = Message.objects.all().count()
	all_events = Message.objects.all()

	get_event_types = Message.objects.only('user_asign')
	if request.GET:  
		event_arr = []
		if request.GET.get('user_asign') == "all":
			all_events = Message.objects.filter()
		else:   
			all_events = Message.objects.filter(user__icontains=request.GET.get('user'))


		for i in all_events:
				event_sub_arr = {}
				event_sub_arr['emisor'] = i.event_name
				event_sub_arr['emisor_nn'] = i.event_name
				start_date = date(i.fecha_inicio.date(), "%Y-%m-%d")
				end_date = date(i.fecha_fin.date(), "%Y-%m-%d")
				event_sub_arr['start'] = start_date
				event_sub_arr['end'] = end_date

				event_arr.append(event_sub_arr)
		return HttpResponse(json.dumps(event_arr))

	form = MessageForm(request.POST or None)
	if form.is_valid():

		create = form.save(commit=False)

		fecha_inicio_data =		request.POST['date_initial']
		create.fecha_inicio = fecha_inicio_data
		create.user_id  = request.user.id
		create.estado = "Enviado"
		create.cod_valid = count

		create.save()
		ide = create.id
		print(ide)

		messages.success(request, "Creado con exito!")
		return HttpResponseRedirect('/inicio')
	context = {
		"form": form,
		"all_events" : all_events,

	}
	return render(request, "calendar.html", context)


