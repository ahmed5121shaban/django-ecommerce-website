from distutils.command.upload import upload
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.
PRODUCT_FLAG={
    ('new','new'),
    ('feature','feature'),
    ('sale','sale'),
    ('old','old'),
}

class Product(models.Model):
    name = models.CharField(_('Name'),max_length=100)
    sku = models.IntegerField(_('Sku'))
    suptitle = models.CharField(_('Subtitle'),max_length=300)
    desc = models.TextField(_('Description'),max_length=10000)
    flag = models.CharField(_('Flag'), max_length=10, choices=PRODUCT_FLAG)
    price = models.IntegerField(_('Price'),default=1)
    tags = TaggableManager()
    brand = models.ForeignKey('Brand',verbose_name=_('Brand'), related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    categury = models.ForeignKey('Category',verbose_name=_('Category'), related_name='product_category',on_delete=models.SET_NULL,null=True,blank=True)
    vedio = models.URLField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name


class ProductsImages(models.Model):
    product = models.ForeignKey(Product,verbose_name=_('Product'), related_name='product_images',on_delete=models.CASCADE)
    image = models.ImageField(_('Image'),upload_to='prodect-image/%y/%m/%d')

    def __str__(self) -> str:
        return str(self.product)


class Category(models.Model):
    name = models.CharField(_('Name'),max_length=100)
    image = models.ImageField(_('Image'),upload_to='category/%y/%m/%d')

    def __str__(self) -> str:
        return self.name


class Brand(models.Model):
    name = models.CharField(_('Name'),max_length=100)
    image = models.ImageField(_('Image'),upload_to='brand/%y/%m/%d')

    def __str__(self) -> str:
        return self.name


class ProductsReview(models.Model):
    user = models.ForeignKey(User, verbose_name=_('User_Review'), on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, verbose_name=_('Product'), on_delete=models.SET_NULL, null=True, blank=True)
    rate = models.IntegerField(verbose_name=_('Rate'))
    review = models.CharField(verbose_name=_('Review'), max_length=200)
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self) -> str:
        return str(self.user)