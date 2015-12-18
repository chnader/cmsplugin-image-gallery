from image_gallery.models import *

__author__ = 'nader'

from modeltranslation.translator import translator, TranslationOptions


class GalleryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )
translator.register(Gallery, GalleryTranslationOptions)


class GalleryCategoryTranslationOptions(TranslationOptions):
    fields = ('name', )
translator.register(GalleryCategory, GalleryCategoryTranslationOptions)