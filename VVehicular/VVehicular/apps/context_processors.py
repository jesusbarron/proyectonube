import django

def my_processor(request):
	context = {"django_version":django.get_version(),

	}
	return context