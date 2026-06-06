from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان الخدمة")
    title_en = models.CharField(max_length=200, blank=True, verbose_name="Title (EN)")
    description = models.TextField(verbose_name="الوصف")
    description_en = models.TextField(blank=True, verbose_name="Description (EN)")
    icon = models.CharField(max_length=100, default="fas fa-cog", verbose_name="أيقونة FontAwesome")
    order = models.PositiveIntegerField(default=0, verbose_name="الترتيب")
    is_active = models.BooleanField(default=True, verbose_name="نشط")

    class Meta:
        verbose_name = "خدمة"
        verbose_name_plural = "الخدمات"
        ordering = ['order']

    def __str__(self):
        return self.title
