from rest_framework.serializers import (
    HyperlinkedIdentityField,
    HyperlinkedRelatedField,
    ModelSerializer,
    SerializerMethodField,
)

from .models import Course


class CourseSerializer(ModelSerializer):
    # blog_post_image = BlogPostImageSerializer(many=True, read_only=True)

    # blog_post_category = HyperlinkedRelatedField(
    #     view_name="store:category_item", lookup_field="slug", many=True, read_only=True
    # )

    detail_url = HyperlinkedIdentityField(view_name="course:course", lookup_field="slug")
    category_list = HyperlinkedIdentityField(view_name="store:category_item", lookup_field="category")

    category_name = SerializerMethodField(method_name="category")

    class Meta:
        model = Course
        fields = [
            "id",
            "detail_url",
            "category_list",
            "category_name",
            "image",
            "alt_text",
            # "blog_post_category",
            "title",
            "description",
            "slug",
            "created_at",
            "updated_at"
            # "blog_post_image",
        ]

    def category(self, obj):
        return obj.category.name
