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
    product_id       = models.IntegerField
    main_category_id = models.ForeignKey(MainCategory, on_delete = models.SET_NULL, null=True)
    sub_category_id  = models.ForeignKey(SubCategory, on_delete = models.SET_NULL, null=True)
    name             = models.CharField(max_length = 100)
    name_en          = models.CharField(max_length = 100)
    desc             = models.CharField(max_length = 100)
    desc_detail      = models.TextField
    size_id          = models.ForeignKey(Size, on_delete = models.SET_NULL, null=True)
    theme_id         = models.ForeignKey(Theme, on_delete = models.SET_NULL, null=True)
    alergy           = models.CharField(max_length = 100)
    nutrition1       = models.DecimalField(max_digits = 4, decimal_places = 1)
    nutrition2       = models.DecimalField(max_digits = 4, decimal_places = 1)
    nutrition3       = models.DecimalField(max_digits = 4, decimal_places = 1)
    nutrition4       = models.DecimalField(max_digits = 4, decimal_places = 1)
    nutrition5       = models.DecimalField(max_digits = 4, decimal_places = 1)
    nutrition6       = models.DecimalField(max_digits = 4, decimal_places = 1)
    img_main         = models.URLField
    img_thumb        = models.URLField
    begin_at         = models.DateTimeField(auto_now = False)
    end_at           = models.DateTimeField(auto_now = False)
    created_at       = models.DateTimeField(auto_now_add = True)
    updated_at       = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'products'
