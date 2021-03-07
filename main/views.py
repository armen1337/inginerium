from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .models import (HeroImageConf, TopHeroImageConf,
	Translate, Service, ColleagueImageConf)


def home(request):
	# Top hero (or slider) images
	top_hero_image_conf = TopHeroImageConf.objects.filter(enabled = True).first()
	try:
		top_hero_images = top_hero_image_conf.topheroimage_set.filter(enabled = True)
	except:
		top_hero_images = None

	# Below hero (or slider) images
	hero_image_conf = HeroImageConf.objects.filter(enabled = True).first()
	try:
		hero_images = hero_image_conf.heroimage_set.filter(enabled = True)
	except:
		hero_images = None

	# colleague images

	colleague_image_conf = ColleagueImageConf.objects.filter(enabled = True).first()
	try:
		colleague_images = colleague_image_conf.colleagueimage_set.all()
	except:
		colleague_images = None


	services = Service.objects.all().order_by('id')


	tdata = Translate.objects.first()


	context = {
		"hero_images": hero_images,
		"top_hero_images": top_hero_images,
		"colleagues": colleague_images,
		"tdata": tdata,
		"services": services
	}
	return render(request, "index.html", context)


def contact_us(request):
	if request.method == "POST":
		message = request.POST["message"]
		email = request.POST["email"]
		name = request.POST["name"]
		message = f"От: {name}\nEmail: {email}\n{message}"

		send_mail(
			"Test",
			message,
			email,
			[settings.EMAIL_HOST_USER],
		)

	return redirect("/")