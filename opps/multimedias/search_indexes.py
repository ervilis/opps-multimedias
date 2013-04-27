#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

from haystack.indexes import SearchIndex, CharField, DateTimeField
from haystack import site

from .models import Audio, Video


class AudioIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    date_available = DateTimeField(model_attr='date_available')
    date_update = DateTimeField(model_attr='date_update')

    def get_updated_field(self):
        return 'date_update'

    def index_queryset(self):
        return Audio.objects.filter(
            date_available__lte=datetime.now(),
            published=True)


class VideoIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    date_available = DateTimeField(model_attr='date_available')
    date_update = DateTimeField(model_attr='date_update')

    def get_updated_field(self):
        return 'date_update'

    def index_queryset(self):
        return Video.objects.filter(
            date_available__lte=datetime.now(),
            published=True)

site.register(Audio, AudioIndex)
site.register(Video, VideoIndex)