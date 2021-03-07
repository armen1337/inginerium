from django import template


register = template.Library()


@register.filter
def return_three(value):
	if len(value) < 4:
		return value
	return value[:3]


@register.filter
def return_last_three(value):
	if len(value) > 3:
		return value[3:]
	return None


@register.filter
def get_title_am(value, index):
	try:
		result = value[int(index - 1)].title_am
		if result:
			return result
		else:
			return ''
	except:
		return ''

@register.filter
def get_title_ru(value, index):
	try:
		result = value[int(index - 1)].title_ru
		if result:
			return result
		else:
			return ''
	except:
		return ''

@register.filter
def get_title_en(value, index):
	try:
		result = value[int(index - 1)].title_en
		if result:
			return result
		else:
			return ''
	except:
		return ''


@register.filter
def get_content_am(value, index):
	try:
		result = value[int(index - 1)].content_am
		if result:
			return result
		else:
			return ''
	except:
		return ''

@register.filter
def get_content_ru(value, index):
	try:
		result = value[int(index - 1)].content_ru
		if result:
			return result
		else:
			return ''
	except:
		return ''

@register.filter
def get_content_en(value, index):
	try:
		result = value[int(index - 1)].content_en
		if result:
			return result
		else:
			return ''
	except:
		return ''