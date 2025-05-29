from rest_framework.serializers import ModelSerializer , StringRelatedField
from .models import Author, Book


class AutherSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(ModelSerializer):
    author = StringRelatedField()
    class Meta:
        model = Book
        fields = "__all__"
        extra_kwargs = {
            "isbn": {
                "required": True,
                "error_messages": {
                    "required": "ISBN is required",
                },
            }
        }
