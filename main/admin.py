from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (HeroImage, HeroImageConf, TopHeroImage,
	TopHeroImageConf, Translate, Service, ServiceImage)


admin.site.site_header = "Inginerium"
admin.site.site_title = "Inginerium"
admin.site.index_title = "Администрирование Inginerium"


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
	