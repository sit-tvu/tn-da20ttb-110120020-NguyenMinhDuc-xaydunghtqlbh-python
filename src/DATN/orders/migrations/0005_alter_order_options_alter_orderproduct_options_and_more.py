# Generated by Django 5.0.4 on 2024-06-23 01:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_order_promotions'),
        ('store', '0011_alter_product_options_alter_reviewrating_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Đơn hàng', 'verbose_name_plural': 'Đơn hàng'},
        ),
        migrations.AlterModelOptions(
            name='orderproduct',
            options={'verbose_name': 'Sản phẩm đặt hàng', 'verbose_name_plural': 'Sản phẩm đặt hàng'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Thanh toán', 'verbose_name_plural': 'Thanh toán'},
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=50, verbose_name='Địa chỉ'),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=50, verbose_name='Thành phố'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo'),
        ),
        migrations.AlterField(
            model_name='order',
            name='district',
            field=models.CharField(max_length=50, verbose_name='Quận/Huyện'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='full_name',
            field=models.CharField(max_length=50, verbose_name='Họ và tên'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ip',
            field=models.CharField(blank=True, max_length=20, verbose_name='Địa chỉ IP'),
        ),
        migrations.AlterField(
            model_name='order',
            name='is_ordered',
            field=models.BooleanField(default=False, verbose_name='Đã đặt hàng'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_note',
            field=models.CharField(blank=True, max_length=100, verbose_name='Ghi chú đơn hàng'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(max_length=50, verbose_name='Số đơn hàng'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_total',
            field=models.FloatField(verbose_name='Tổng đơn hàng'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.payment', verbose_name='Thanh toán'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Số điện thoại'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ship',
            field=models.FloatField(verbose_name='Phí vận chuyển'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'Mới'), ('Accepted', 'Đã chấp nhận'), ('Completed', 'Hoàn thành'), ('Cancelled', 'Đã hủy')], default='New', max_length=10, verbose_name='Trạng thái'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Người dùng'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ward',
            field=models.CharField(max_length=50, verbose_name='Phường/Xã'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Đơn hàng'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='ordered',
            field=models.BooleanField(default=False, verbose_name='Đã đặt hàng'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.payment', verbose_name='Thanh toán'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Sản phẩm'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='product_price',
            field=models.FloatField(verbose_name='Giá sản phẩm'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='quantity',
            field=models.IntegerField(verbose_name='Số lượng'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Người dùng'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation', verbose_name='Biến thể'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='amount_paid',
            field=models.CharField(max_length=100, verbose_name='Số tiền đã thanh toán'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(max_length=100, verbose_name='Mã thanh toán'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(max_length=100, verbose_name='Phương thức thanh toán'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(max_length=100, verbose_name='Trạng thái'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Người dùng'),
        ),
    ]
