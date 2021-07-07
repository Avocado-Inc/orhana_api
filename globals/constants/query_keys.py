from enum import Enum


class ProductListingSortKey:
    class ENUM(str, Enum):
        CREATED_AT = "created_at"
        UPDATED_AT = "updated_at"
        MAX_SELLING_PRICE = "max_selling_price"


class SortDirection:
    class ENUM(str, Enum):
        ASC = "+"
        DESC = "-"
