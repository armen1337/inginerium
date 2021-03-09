from django.db import models


class HeroImageConf(models.Model):
	title = models.CharField(
			"Заголовок",
			null = True,
			blank = True,
			max_length = 100
		)
	enabled = models.BooleanField(default = False)

	def __str__(self):
		if self.title:
			return self.title
		return f"Безымянный {self.id}"

	class Meta:
		verbose_name = "Набор картинок слайдера"
		verbose_name_plural = "Наборы картинок слайдера"


class HeroImage(models.Model):
	hero_image_conf = models.ForeignKey(
			HeroImageConf,
			on_delete = models.SET_NULL,
			null = True
		)
	image = models.ImageField(
			"Картинка",
			upload_to = "hero_images/",
			null = True,
			blank = True
		)
	enabled = models.BooleanField(default = True)

	def __str__(self):
		return ""


class TopHeroImageConf(models.Model):
	title = models.CharField(
			"Заголовок",
			null = True,
			blank = True,
			max_length = 100
		)
	enabled = models.BooleanField(default = False)

	def __str__(self):
		if self.title:
			return self.title
		return f"Безымянный {self.id}"

	class Meta:
		verbose_name = "Набор верхних картинок слайдера"
		verbose_name_plural = "Наборы верхних картинок слайдера"


class TopHeroImage(models.Model):
	hero_image_conf = models.ForeignKey(
			TopHeroImageConf,
			on_delete = models.SET_NULL,
			null = True
		)
	image = models.ImageField(
			"Картинка",
			upload_to = "top_hero_images/",
			null = True,
			blank = True
		)
	enabled = models.BooleanField(default = True)

	title_am = models.CharField(
			"Заголовок (AM)",
			max_length = 255,
			null = True,
			blank = True
		)

	title_ru = models.CharField(
			"Заголовок (RU)",
			max_length = 255,
			null = True,
			blank = True
		)
	
	title_en = models.CharField(
			"Заголовок (EN)",
			max_length = 255,
			null = True,
			blank = True
		)

	content_am = models.TextField("Описание (AM)", null = True, blank = True)
	content_ru = models.TextField("Описание (RU)", null = True, blank = True)
	content_en = models.TextField("Описание (EN)", null = True, blank = True)


	def __str__(self):
		return ""


class ColleagueImageConf(models.Model):
	title = models.CharField(
			"Заголовок",
			null = True,
			blank = True,
			max_length = 100
		)
	enabled = models.BooleanField(default = False)

	def __str__(self):
		if self.title:
			return self.title
		return f"Безымянный {self.id}"

	class Meta:
		verbose_name = "Блок партнёра"
		verbose_name_plural = "Блоки партнёров"


class ColleagueImage(models.Model):
	colleague_image_conf = models.ForeignKey(
			ColleagueImageConf,
			on_delete = models.SET_NULL,
			null = True
		)
	image = models.ImageField(
			"Картинка",
			upload_to = "colleague_images/",
			null = True,
			blank = True
		)

	def __str__(self):
		return ""


class Service(models.Model):
	title_am = models.CharField(
			"Заголовок (AM)",
			max_length = 255,
			null = True,
			blank = True
		)

	title_ru = models.CharField(
			"Заголовок (RU)",
			max_length = 255,
			null = True,
			blank = True
		)

	title_en = models.CharField(
			"Заголовок (EN)",
			max_length = 255,
			null = True,
			blank = True
		)

	content_am = models.TextField("Описание (AM)", null = True, blank = True)
	content_ru = models.TextField("Описание (RU)", null = True, blank = True)
	content_en = models.TextField("Описание (EN)", null = True, blank = True)


	def __str__(self):
		return self.title_am


	class Meta:
		verbose_name = "Сервис"
		verbose_name_plural = "Сервисы"


class ServiceImage(models.Model):
	service = models.ForeignKey(
			Service,
			on_delete = models.SET_NULL,
			null = True
		)
	image = models.ImageField(
			"Картинка",
			upload_to = "service_images/",
			null = True,
			blank = True
		)

	def __str__(self):
		return ""

	class Meta:
		verbose_name = "Картинка сервиса"
		verbose_name_plural = "Картинки сервиса"


class Translate(models.Model):
	home_am = models.CharField("Главная (AM)", max_length = 255)
	home_ru = models.CharField("Главная (RU)", max_length = 255)
	home_en = models.CharField("Главная (EN)", max_length = 255)

	about_am = models.CharField("О нас (AM)", max_length = 255)
	about_ru = models.CharField("О нас (RU)", max_length = 255)
	about_en = models.CharField("О нас (EN)", max_length = 255)

	about2_am = models.CharField(
			"О нас (2) (AM)",
			null = True,
			max_length = 255
		)
	about2_ru = models.CharField(
			"О нас (2) (RU)",
			null = True,
			max_length = 255
		)
	about2_en = models.CharField(
			"О нас (2) (EN)",
			null = True,
			max_length = 255
		)

	about3_am = models.TextField("О нас (3) (AM)", null = True)
	about3_ru = models.TextField("О нас (3) (RU)", null = True)
	about3_en = models.TextField("О нас (3) (EN)", null = True)

	service_am = models.CharField("Сервисы (AM)", max_length = 255)
	service_ru = models.CharField("Сервисы (RU)", max_length = 255)
	service_en = models.CharField("Сервисы (EN)", max_length = 255)

	work_am = models.CharField("Работы (AM)", max_length = 255)
	work_ru = models.CharField("Работы (RU)", max_length = 255)
	work_en = models.CharField("Работы (EN)", max_length = 255)

	contact_am = models.CharField("Обратная связь (AM)", max_length = 255)
	contact_ru = models.CharField("Обратная связь (RU)", max_length = 255)
	contact_en = models.CharField("Обратная связь (EN)", max_length = 255)

	partners_am = models.CharField(
			"Партнёры (AM)",
			null = True,
			max_length = 255
		)
	partners_ru = models.CharField(
			"Партнёры (RU)",
			null = True,
			max_length = 255
		)
	partners_en = models.CharField(
			"Партнёры (EN)",
			null = True,
			max_length = 255
		)

	work_time_am = models.CharField(
			"Рабочее время (AM)",
			max_length = 255,
			null = True
		)
	work_time_ru = models.CharField(
			"Рабочее время (RU)",
			max_length = 255,
			null = True
		)
	work_time_en = models.CharField(
			"Рабочее время (EN)",
			max_length = 255,
			null = True
		)

	work_days1_am = models.CharField(
			"Рабочие дни (от - до) (AM)",
			max_length = 255,
			null = True
		)
	work_days1_ru = models.CharField(
			"Рабочие дни (от - до) (RU)",
			max_length = 255,
			null = True
		)
	work_days1_en = models.CharField(
			"Рабочие дни (от - до) (EN)",
			max_length = 255,
			null = True
		)

	work_days2_am = models.CharField(
			"Рабочие дни (от - до) (2) (AM)",
			max_length = 255,
			null = True
		)
	work_days2_ru = models.CharField(
			"Рабочие дни (от - до) (2) (RU)",
			max_length = 255,
			null = True
		)
	work_days2_en = models.CharField(
			"Рабочие дни (от - до) (2) (EN)",
			max_length = 255,
			null = True
		)

	contact_us_am = models.CharField(
			"Свяжитесь с нами (AM)",
			max_length = 255,
			null = True
		)
	contact_us_ru = models.CharField(
			"Свяжитесь с нами (RU)",
			max_length = 255,
			null = True
		)
	contact_us_en = models.CharField(
			"Свяжитесь с нами (EN)",
			max_length = 255,
			null = True
		)

	# messages

	text_success_am = models.CharField(
			"Ваше письмо отправлено (AM)",
			max_length = 255,
			null = True
		)
	text_success_ru = models.CharField(
			"Ваше письмо отправлено (RU)",
			max_length = 255,
			null = True
		)
	text_success_en = models.CharField(
			"Ваше письмо отправлено (EN)",
			max_length = 255,
			null = True
		)

	text_danger_am = models.TextField(
			"""Электронная почта должна быть действительной,
			а длина сообщения должна превышать 1 символ (AM)""",
			null = True
		)
	text_danger_ru = models.TextField(
			"""Электронная почта должна быть действительной,
			а длина сообщения должна превышать 1 символ (RU)""",
			null = True
		)
	text_danger_en = models.TextField(
			"""Электронная почта должна быть действительной,
			а длина сообщения должна превышать 1 символ (EN)""",
			null = True
		)

	# form placeholders

	name_am = models.CharField(
			"Имя и фамилия (AM)",
			max_length = 255,
			null = True
		)
	name_ru = models.CharField(
			"Имя и фамилия (RU)",
			max_length = 255,
			null = True
		)
	name_en = models.CharField(
			"Имя и фамилия (EN)",
			max_length = 255,
			null = True
		)

	email_am = models.CharField(
			"Электронная почта (AM)",
			max_length = 255,
			null = True
		)
	email_ru = models.CharField(
			"Электронная почта (RU)",
			max_length = 255,
			null = True
		)
	email_en = models.CharField(
			"Электронная почта (EN)",
			max_length = 255,
			null = True
		)

	message_am = models.CharField(
			"Ваше письмо (AM)",
			max_length = 255,
			null = True
		)
	message_ru = models.CharField(
			"Ваше письмо (RU)",
			max_length = 255,
			null = True
		)
	message_en = models.CharField(
			"Ваше письмо (EN)",
			max_length = 255,
			null = True
		)

	# form button

	submit_am = models.CharField(
			"Отправить (AM)",
			max_length = 255,
			null = True
		)
	submit_ru = models.CharField(
			"Отправить (RU)",
			max_length = 255,
			null = True
		)
	submit_en = models.CharField(
			"Отправить (EN)",
			max_length = 255,
			null = True
		)


	# address

	address_am = models.CharField(
			"Слово адрес (AM)",
			max_length = 255,
			null = True
		)
	address_ru = models.CharField(
			"Слово адрес (RU)",
			max_length = 255,
			null = True
		)
	address_en = models.CharField(
			"Слово адрес (EN)",
			max_length = 255,
			null = True
		)

	address1_am = models.CharField(
			"Адрес 1 (AM)",
			max_length = 255,
			null = True
		)
	address1_ru = models.CharField(
			"Адрес 1 (RU)",
			max_length = 255,
			null = True
		)
	address1_en = models.CharField(
			"Адрес 1 (EN)",
			max_length = 255,
			null = True
		)

	address2_am = models.CharField(
			"Адрес 2 (AM)",
			max_length = 255,
			null = True
		)
	address2_ru = models.CharField(
			"Адрес 2 (RU)",
			max_length = 255,
			null = True
		)
	address2_en = models.CharField(
			"Адрес 2 (EN)",
			max_length = 255,
			null = True
		)

	# numbers

	number_row1 = models.CharField(
			"Строка номера 1",
			max_length = 255,
			null = True
		)
	number_row2 = models.CharField(
			"Строка номера 2",
			max_length = 255,
			null = True
		)


	class Meta:
		verbose_name = "Перевод"
		verbose_name_plural = "Перевод"