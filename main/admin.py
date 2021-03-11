from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django.utils.safestring import mark_safe

from .models import *


admin.site.site_header = "Inginerium"
admin.site.site_title = "Inginerium"
admin.site.index_title = "Администрирование Inginerium"


class ColleagueImageInline(admin.StackedInline):
	model = ColleagueImage
	extra = 1
	readonly_fields = ("get_image",)

	fields = ("image", "get_image")

	def get_image(self, obj):
		return mark_safe(f"""<img src="{obj.image.url}"
			width="400px">""")

	get_image.short_description = "Обзор"

	verbose_name = "Картинка партнёра"
	verbose_name_plural = "Картинки партнёров"


@admin.register(ColleagueImageConf)
class ColleagueImageConfAdmin(admin.ModelAdmin):
	model = ColleagueImageConf
	list_display = ("__str__", "enabled")
	list_editable = ("enabled",)

	save_on_top = True

	inlines = [ColleagueImageInline]

	fields = ("title", "enabled")


@admin.register(Translate)
class TranslateAdmin(admin.ModelAdmin):
	model = Translate

	save_on_top = True


class HeroImageInline(admin.StackedInline):
	model = HeroImage
	extra = 1
	readonly_fields = ("get_image",)

	fields = ("image", "get_image", "enabled")

	def get_image(self, obj):
		return mark_safe(f"""<img src="{obj.image.url}"
			width="400px">""")

	get_image.short_description = "Обзор"

	verbose_name = "Картинка слайдера"
	verbose_name_plural = "Картинки слайдера"


@admin.register(HeroImageConf)
class HeroImageConfAdmin(admin.ModelAdmin):
	model = HeroImageConf
	list_display = ("__str__", "enabled")
	list_editable = ("enabled",)

	save_on_top = True

	inlines = [HeroImageInline]

	fields = ("title", "enabled")


class TopHeroImageInline(admin.StackedInline):
	model = TopHeroImage
	extra = 0
	readonly_fields = ("get_image",)

	fields = (
			"image",
			"get_image",
			"enabled",
			"title_am",
			"content_am",
			"title_ru",
			"content_ru",
			"title_en",
			"content_en",
		)

	def get_image(self, obj):
		return mark_safe(f"""<img src="{obj.image.url}"
			width="400px">""")

	get_image.short_description = "Обзор"

	verbose_name = "Картинка слайдера"
	verbose_name_plural = "Картинки слайдера"


@admin.register(TopHeroImageConf)
class TopHeroImageConfAdmin(admin.ModelAdmin):
	model = TopHeroImageConf
	list_display = ("__str__", "enabled")
	list_editable = ("enabled",)

	save_on_top = True

	inlines = [TopHeroImageInline]

	fields = ("title", "enabled")


class ServiceImageInline(admin.StackedInline):
	model = ServiceImage
	extra = 1
	readonly_fields = ("get_image",)

	fields = ("image", "get_image")

	def get_image(self, obj):
		return mark_safe(f"""<img src="{obj.image.url}"
			width="400px">""")

	get_image.short_description = "Обзор"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	model = Service
	save_on_top = True

	inlines = [ServiceImageInline]

	formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':6, 'cols':60})},
    }
	