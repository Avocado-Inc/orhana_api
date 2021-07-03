from inventory.models import Category
from inventory.models import SubCategory

category_data = [
    {
        "name": "Home Decor",
    },
]
sub_category_data = [
    [
        {
            "name": "Curtains",
        },
    ],
]

for i, category in enumerate(category_data):
    category_db, created = Category.objects.get_or_create(**category)
    print(f"CATEGORY - {category_db}, CREATED: {created}")
    for sub_category in sub_category_data[i]:
        sub_category.setdefault("category", category_db)
        print(sub_category)
        sub_category_db, created = SubCategory.objects.get_or_create(**sub_category)
        print(f"SUB CATEGORY - {sub_category_db}, CREATED: {created}")
