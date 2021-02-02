from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

from PIL import Image


class Photo(models.Model):
    def validate_image_size(self):
        filesize = self.size
        size_limit = 5.0
        if filesize > size_limit * 1024 * 1024:
            raise ValidationError("Максимальный размер фотографии %sMB" % str(size_limit))

    def validate_image_format(self):
        allowed_format = ['jpg', 'png', 'jpeg']
        file_format = self.name.split('.')[1].lower()
        if file_format not in allowed_format:
            raise ValidationError('Неверный формат файла %s' % file_format)

    img = models.ImageField(verbose_name='Фотография',
                            validators=[validate_image_size, validate_image_format],
                            default=None,
                            upload_to='media')
    name = models.CharField(verbose_name='Название', max_length=15)
    user = models.ForeignKey(User, db_column="user", on_delete=models.CASCADE, verbose_name='Владелец')
    views = models.IntegerField(verbose_name='Количество просмотров', default=0)
    date_add = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img_preview = Image.open(self.img.path)

        if img_preview.height > 150 or img_preview.weight > 150:
            output_size = (150, 150)
            img_preview.thumbnail(output_size)
            path_resize = img_preview.filename.split('.')[0] + '_resize.' + img_preview.filename.split('.')[1]
            img_preview.save(path_resize)


    class Meta:
        unique_together = ['name', 'user']

    def __str__(self):
        return self.name

