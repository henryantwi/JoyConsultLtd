from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    name = models.CharField(
        verbose_name=_("title"),
        help_text=_("Required"),
        max_length=255,
    )
    price = models.DecimalField(
        verbose_name=_("Regular price"),
        help_text=_("Maximum 999.99"),
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(999.99)],
    )
    description = models.TextField()
    stock = models.IntegerField()
    image = models.ImageField(
        verbose_name=_("image"),
        help_text=_("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.name
