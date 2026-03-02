# custom template tags and filters
from django import template

register = template.Library()


@register.filter
def get_subject_ids_for_tag(tag):
    if not tag:
        return ""
    return ",".join(str(subject.pk) for subject in tag.subjects.all())


@register.filter
def get_subject_slugs_for_tag(tag):
    if not tag:
        return ""

    return ",".join(str(subject.slug) for subject in tag.subjects.all())


@register.filter
def dict_get(d, key):
    # safely get a value from a dictionary, returns None if key not found
    return d.get(key)
