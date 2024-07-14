# Generated by Django 5.0.4 on 2024-06-23 01:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ngày tham gia'),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Hoạt động'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='Là quản trị viên'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Là nhân viên'),
        ),
        migrations.AlterField(
            model_name='account',
            name='is_superadmin',
            field=models.BooleanField(default=False, verbose_name='Là quản trị tối cao'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Lần đăng nhập cuối'),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Số điện thoại'),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=50, unique=True, verbose_name='Tên người dùng'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=100, verbose_name='Địa chỉ'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=100, verbose_name='Thành phố'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='district',
            field=models.CharField(blank=True, max_length=100, verbose_name='Quận/Huyện'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='userprofile', verbose_name='Ảnh đại diện'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Người dùng'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ward',
            field=models.CharField(blank=True, max_length=100, verbose_name='Phường/Xã'),
        ),
    ]
