"""CMS Plugins for the ``image_gallery`` app."""
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from image_gallery.models import GalleryPlugin
from . import app_settings


class CMSGalleryPlugin(CMSPluginBase):

    model = GalleryPlugin
    name = _('Filer Gallery')
    render_template = app_settings.TEMPLATE_CHOICES[0][0]

    def render(self, context, instance, placeholder):
        context.update({
            'gallery': instance.gallery,
            'images': instance.gallery.get_folder_images(),
            'placeholder': placeholder,
            'display_type': instance.display_type,
        })
        self.render_template = instance.template
        return context

plugin_pool.register_plugin(CMSGalleryPlugin)