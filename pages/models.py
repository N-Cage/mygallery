from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

def upload_location(instance, filename, **kwargs):
    file_path = 'static_cdn/{author_id}/{title}-{filename}'.format(
        author_id=str(instance.author.id), title=str(instance.title), filename=filename
        )
    return file_path

class ImageCard(models.Model):
    title               = models.CharField(max_length=50, blank=False, null=False)
    image               = models.ImageField(upload_to=upload_location, blank=False, null=False)
    discription         = models.TextField(max_length=500, blank=False, null=False)
    date_published      = models.DateTimeField(auto_now_add=True, verbose_name='date pbulished')
    date_updated        = models.DateTimeField(auto_now=True, verbose_name='date updated')
    author              = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug                = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

@receiver(post_delete, sender=ImageCard)
def subimission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


def pre_save_image_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author.username + '-' + instance.title)

pre_save.connect(pre_save_image_receiver, sender=ImageCard)
