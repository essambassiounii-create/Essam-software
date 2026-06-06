from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="الاسم")
    name_en = models.CharField(max_length=100, blank=True, verbose_name="الاسم (إنجليزي)")
    slug = models.SlugField(unique=True, verbose_name="الرابط")
    icon = models.CharField(max_length=100, default="fas fa-folder", verbose_name="أيقونة")

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"

    def __str__(self):
        return self.name


class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('desktop', 'برنامج سطح المكتب'),
        ('web', 'تطبيق ويب'),
        ('mobile', 'تطبيق جوال'),
    ]

    name = models.CharField(max_length=200, verbose_name="اسم البرنامج")
    name_en = models.CharField(max_length=200, blank=True, verbose_name="اسم البرنامج (إنجليزي)")
    slug = models.SlugField(unique=True, verbose_name="الرابط")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="التصنيف")
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES, default='desktop', verbose_name="نوع البرنامج")
    short_description = models.TextField(max_length=300, verbose_name="وصف مختصر")
    short_description_en = models.TextField(max_length=300, blank=True, verbose_name="وصف مختصر (إنجليزي)")
    full_description = models.TextField(verbose_name="الوصف الكامل")
    full_description_en = models.TextField(blank=True, verbose_name="الوصف الكامل (إنجليزي)")
    features = models.TextField(verbose_name="المميزات (كل ميزة في سطر)", help_text="اكتب كل ميزة في سطر منفصل")
    features_en = models.TextField(blank=True, verbose_name="المميزات (إنجليزي)")
    image = models.ImageField(upload_to='products/', verbose_name="الصورة الرئيسية", blank=True, null=True)
    demo_url = models.URLField(blank=True, verbose_name="رابط النسخة التجريبية")
    download_url = models.URLField(blank=True, verbose_name="رابط التحميل")
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="السعر")
    price_label = models.CharField(max_length=100, blank=True, verbose_name="وصف السعر", help_text="مثال: مجاني / تواصل للسعر")
    is_featured = models.BooleanField(default=False, verbose_name="مميز")
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "برنامج"
        verbose_name_plural = "البرامج"
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def get_features_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]


class ProductScreenshot(models.Model):
    product = models.ForeignKey(Product, related_name='screenshots', on_delete=models.CASCADE, verbose_name="البرنامج")
    image = models.ImageField(upload_to='screenshots/', verbose_name="الصورة")
    caption = models.CharField(max_length=200, blank=True, verbose_name="وصف الصورة")
    order = models.PositiveIntegerField(default=0, verbose_name="الترتيب")

    class Meta:
        verbose_name = "صورة"
        verbose_name_plural = "الصور"
        ordering = ['order']

    def __str__(self):
        return f"صورة - {self.product.name}"
