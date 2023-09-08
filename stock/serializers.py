from rest_framework.serializers import ModelSerializer 
from rest_framework import serializers

from .models import(
    Category,
    Brand,
    Product,
    Firm,
    Purchases,
    Sales,
    
)

class CategorySerializer(ModelSerializer):
    product_count=serializers.SerializerMethodField()

    class Meta:
        model=Category
        fields=(
            "id",
            "name",
            "product_count",      
            )

    def get_product_count(self,obj):
        return obj.products.count()
        # return Product.objects.filter(categor_id=obj_id).count()
          
class FirmSerializer(ModelSerializer):
    class Meta:
        model=Firm
        fields=("__all__") 

class BrandSerializer(ModelSerializer):
    class Meta:
        model=Brand
        fields=("__all__")

class ProductSerializer(ModelSerializer):
    category=serializers.StringRelatedField()
    category_id=serializers.IntegerField()
    brand=serializers.StringRelatedField()
    brand_id=serializers.IntegerField()

    class Meta:
        model=Product
        fields=(
            "category",
            "category_id",
            "brand",
            "brand_id",
            "name",
            "stock",
            ) 


class CategoryProductSerializer(ModelSerializer):
    product_count=serializers.SerializerMethodField()
    products=ProductSerializer(many=True)
    class Meta:
        model=Category
        fields=(
            "id",
            "name",
            "product_count",  
            "products",    
            )

    def get_product_count(self,obj):
        return obj.products.count()
        # return Product.objects.filter(categor_id=obj_id).count()


class PurchasesSerializer(ModelSerializer):
    user=serializers.SlugRelatedField
    firm=serializers.StringRelatedField()
    firm_id=serializers.IntegerField()
    brand=serializers.StringRelatedField()
    brand_id=serializers.IntegerField()
    product=serializers.StringRelatedField()
    product_id=serializers.IntegerField()
    
    class Meta:
        model=Purchases
        fields=(
            "user",
            "firm",
            "firm_id",
            "brand",
            "brand_id",   
            "product",
            "product_id",
            "quantity",
            "price",
            "price_total",
            )
        read_only_fields=('price_total',)

    # def get_product_count(self,obj):
    #     return obj.products.count()
        # return Product.objects.filter(categor_id=obj_id).count()
    

 # normalde null daha mantıklı moels.SET_NULL
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    # firm=models.ForeignKey(Firm,on_delete=models.CASCADE,related_name='purchases')
    # brand=models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='b_purchases')
    # product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='p_purchases')
    # quantity=models.SmallIntegerField()
    # price=models.DecimalField(max_digits=8,validators=[MinValueValidator(0)],decimal_places=2)
    # price_total=models.DecimalField(blank=True, max_digits=8,validators=[MinValueValidator(0)],decimal_places=2)
