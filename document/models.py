from django.db import models
from django.utils.translation import gettext_lazy as _
from .constants import METHODS


# Create your models here.
class Document(models.Model):
    name = models.CharField(_('Name'), max_length=64)
    index = models.IntegerField(_('Index'), default=0)
    create_time = models.DateTimeField(_('Create Time'), auto_now_add=True)
    author = models.CharField(_('Author'), max_length=32, blank=True, default='')
    description = models.CharField(_('Description'), max_length=5120, blank=True, default='')

    class Meta:
        verbose_name = verbose_name_plural = _('Document')

    def __str__(self):
        return self.name


class Module(models.Model):
    document = models.ForeignKey(Document, verbose_name=_('Document'), related_name='modules', on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=64)
    index = models.IntegerField(_('Index'), default=0)
    create_time = models.DateTimeField(_('Create Time'), auto_now_add=True)
    author = models.CharField(_('Author'), max_length=32, blank=True, default='')
    description = models.CharField(_('Description'), max_length=5120, blank=True, default='')

    class Meta:
        verbose_name = verbose_name_plural = _('Module')

    def __str__(self):
        return self.name


class Api(models.Model):
    document = models.ForeignKey(Document, verbose_name=_('Document'), related_name='api_set', on_delete=models.CASCADE)
    module = models.ForeignKey(Module, verbose_name=_('Module'), related_name='api_set', on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=128, blank=True, default='')
    url = models.URLField(_('URL'))
    index = models.IntegerField(_('Index'), default=0)
    create_time = models.DateTimeField(_('Create Time'), auto_now_add=True)
    author = models.CharField(_('Author'), max_length=32, blank=True, default='')
    description = models.CharField(_('Description'), max_length=5120, blank=True, default='')

    class Meta:
        verbose_name = verbose_name_plural = _('Api')

    def __str__(self):
        return self.title or self.url


class ApiContent(models.Model):
    api = models.ForeignKey(Api, verbose_name=_('Api'), related_name='contents', on_delete=models.CASCADE)
    method = models.CharField(_('Method'), max_length=8, choices=METHODS)
    params = models.CharField(_('Params'), max_length=510, blank=True, default='')
    body = models.CharField(_('Body'), max_length=2048, blank=True, default='')
    response = models.CharField(_('Response'), max_length=2048, blank=True, default='')
    error_response = models.CharField(_('Error Response'), max_length=2048, blank=True, default='')

    class Meta:
        verbose_name = verbose_name_plural = _('Api Content')

    def __str__(self):
        return '{}: {}'.format(self.method, self.api.url)
