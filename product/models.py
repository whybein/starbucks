from django.db import models


class MainCategory(models.Model):
    name       = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'maincategories'


class SubCategory(models.Model):
    name         = models.CharField(max_length = 100)
    main_cate_id = models.ForeignKey('MainCategory', on_delete = models.SET_NULL, null=True)
    created_at   = models.DateTimeField(auto_now_add = True)
    updated_at   = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'subcategories'


class Theme(models.Model):
    name       = models.CharField(max_length = 100)
    begin_at   = models.DateTimeField(auto_now = False)
    end_at     = models.DateTimeField(auto_now = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'themes'


class Size(models.Model):
    size       = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'sizes'


class Product(models.Model):
    main_category_id = models.ForeignKey(MainCategory, on_delete = models.SET_NULL, null=True)
    sub_category_id  = models.ForeignKey(SubCategory, on_delete = models.SET_NULL, null=True)
    name             = models.CharField(max_length = 100)
    name_en          = models.CharField(max_length = 100, null=True)
    desc             = models.CharField(max_length = 100)
    desc_detail      = models.TextField(null=True)
    size             = models.ManyToManyField(Size, through='SizeInfo')
    theme_id         = models.ForeignKey(Theme, on_delete = models.SET_NULL, null=True)
    alergy           = models.CharField(max_length = 100, null=True)
    nutrition1       = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
    nutrition2       = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
    nutrition3       = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
    nutrition4       = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
    nutrition5       = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
    nutrition6       = models.DecimalField(max_digits = 4, decimal_places = 1, null=True)
    img_main         = models.URLField(null=True)
    img_thumb        = models.URLField(null=True)
    begin_at         = models.DateTimeField(auto_now = False, null=True)
    end_at           = models.DateTimeField(auto_now = False, null=True)
    created_at       = models.DateTimeField(auto_now_add = True)
    updated_at       = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'products'


class SizeInfo(models.Model):
    size       = models.ForeignKey(Size, on_delete = models.SET_NULL, null=True)
    product    = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)
    price      = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


    class Meta:
        db_table = 'sizeinfoes'
