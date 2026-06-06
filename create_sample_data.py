import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'essam_software.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import Service
from products.models import Category, Product

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@essam-software.com', 'admin123')
    print("Created superuser: admin / admin123")

# Create services
services_data = [
    {
        'title': 'تطوير برامج سطح المكتب',
        'icon': 'fas fa-desktop',
        'description': 'نطور برامج احترافية لسطح المكتب تعمل على Windows وأنظمة أخرى. من أنظمة إدارة المخازن والمبيعات إلى برامج المحاسبة والفواتير.',
        'order': 1,
    },
    {
        'title': 'تطوير تطبيقات الويب',
        'icon': 'fas fa-globe',
        'description': 'نبني مواقع ومنصات ويب متكاملة وسريعة. مواقع الشركات، منصات التجارة الإلكترونية، لوحات التحكم والأنظمة الإدارية.',
        'order': 2,
    },
    {
        'title': 'تطوير تطبيقات الجوال',
        'icon': 'fas fa-mobile-alt',
        'description': 'تطبيقات جوال احترافية لنظامي Android وiOS. تصميم عصري وأداء عالي وتجربة مستخدم رائعة لضمان نجاح تطبيقك.',
        'order': 3,
    },
    {
        'title': 'الدعم الفني والصيانة',
        'icon': 'fas fa-headset',
        'description': 'دعم فني متواصل على مدار الساعة. تحديثات دورية وصيانة مستمرة للبرامج لضمان أعلى مستوى من الأداء والاستمرارية.',
        'order': 4,
    },
    {
        'title': 'تخصيص الأنظمة',
        'icon': 'fas fa-cogs',
        'description': 'تعديل وتطوير الأنظمة البرمجية الموجودة لتتناسب مع احتياجاتك الخاصة. إضافة مميزات جديدة وتحسين الأداء.',
        'order': 5,
    },
    {
        'title': 'التدريب والتأهيل',
        'icon': 'fas fa-chalkboard-teacher',
        'description': 'ندرّب فريق عملك على استخدام البرامج والأنظمة بكفاءة. ورش عمل تفصيلية ودليل مستخدم شامل لكل نظام.',
        'order': 6,
    },
]

for sdata in services_data:
    obj, created = Service.objects.get_or_create(title=sdata['title'], defaults=sdata)
    if created:
        print(f"Created service: {sdata['title']}")

# Create categories
cats = [
    {'name': 'أنظمة إدارة', 'name_en': 'Management Systems', 'slug': 'management', 'icon': 'fas fa-sitemap'},
    {'name': 'مواقع ويب', 'name_en': 'Web Applications', 'slug': 'web', 'icon': 'fas fa-globe'},
    {'name': 'تطبيقات جوال', 'name_en': 'Mobile Apps', 'slug': 'mobile', 'icon': 'fas fa-mobile-alt'},
]
category_objs = {}
for cdata in cats:
    obj, created = Category.objects.get_or_create(slug=cdata['slug'], defaults=cdata)
    category_objs[cdata['slug']] = obj
    if created:
        print(f"Created category: {cdata['name']}")

# Create sample products
products_data = [
    {
        'name': 'نظام إدارة المخازن',
        'name_en': 'Inventory Management System',
        'slug': 'inventory-management',
        'category': category_objs['management'],
        'product_type': 'desktop',
        'short_description': 'نظام احترافي متكامل لإدارة المخازن والمستودعات. يتيح تتبع البضائع، إدارة الموردين، طباعة التقارير والإحصائيات بشكل سهل وفعّال.',
        'full_description': 'نظام إدارة المخازن من Essam Software هو حل متكامل يساعدك على إدارة مخزنك بكفاءة عالية. يوفر النظام واجهة سهلة الاستخدام مع ميزات متقدمة لتتبع المنتجات، إدارة الموردين، والتقارير التفصيلية. مثالي للشركات الصغيرة والمتوسطة التي تبحث عن حل موثوق وسريع.',
        'features': 'إضافة وتعديل وحذف المنتجات بسهولة\nإدارة الموردين والعملاء\nتقارير المخزون والحركة\nتنبيهات النفاد والحد الأدنى\nطباعة الفواتير وأوامر الشراء\nباركود وQR code\nتعدد المستخدمين وصلاحيات\nنسخ احتياطي تلقائي',
        'price': 1500,
        'is_featured': True,
        'is_active': True,
    },
    {
        'name': 'نظام نقطة البيع (POS)',
        'name_en': 'Point of Sale System',
        'slug': 'pos-system',
        'category': category_objs['management'],
        'product_type': 'desktop',
        'short_description': 'نظام POS احترافي لإدارة المبيعات والفواتير. سريع وموثوق يدعم باركود، فئات المنتجات، ودعم المدفوعات المتعددة.',
        'full_description': 'نظام نقطة البيع المتكامل مصمم خصيصاً للمحلات التجارية والمطاعم وجميع نقاط البيع بالتجزئة. يوفر واجهة سريعة وسهلة لتسجيل المبيعات وطباعة الفواتير وإدارة الكاشير مع إمكانية تعدد الفروع.',
        'features': 'واجهة لمسية سهلة الاستخدام\nدعم الباركود والQR\nإدارة الكاشير والوردية\nتقارير المبيعات اليومية\nإدارة فئات المنتجات\nدعم الخصومات والعروض\nتعدد وسائل الدفع\nطباعة الفواتير الحرارية',
        'price_label': 'ابتداءً من 800 ر.س',
        'is_featured': True,
        'is_active': True,
    },
    {
        'name': 'موقع شركة احترافي',
        'name_en': 'Professional Company Website',
        'slug': 'company-website',
        'category': category_objs['web'],
        'product_type': 'web',
        'short_description': 'موقع ويب احترافي لشركتك أو مشروعك التجاري. تصميم عصري متجاوب مع محرك بحث مُحسَّن وسرعة تحميل فائقة.',
        'full_description': 'نبني مواقع ويب احترافية تعكس هوية شركتك وتجذب العملاء. كل موقع مُصمَّم بعناية فائقة ليكون سريع التحميل ومحسَّن لمحركات البحث ومتجاوب مع جميع الأجهزة.',
        'features': 'تصميم مخصص بالكامل\nمتجاوب مع جميع الأجهزة\nمحسَّن لمحركات البحث\nسرعة تحميل عالية\nلوحة تحكم سهلة\nدعم اللغة العربية RTL\nشهادة SSL مجانية\nربط بالسوشيال ميديا',
        'price_label': 'تواصل للسعر',
        'is_featured': False,
        'is_active': True,
    },
]

for pdata in products_data:
    obj, created = Product.objects.get_or_create(slug=pdata['slug'], defaults=pdata)
    if created:
        print(f"Created product: {pdata['name']}")

print("\n✅ Sample data created successfully!")
print("🔑 Admin credentials: admin / admin123")
print("🌐 Visit: http://localhost:5000")
print("⚙️  Admin: http://localhost:5000/admin")
