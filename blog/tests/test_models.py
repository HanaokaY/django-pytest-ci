import pytest
from blog.models import Post

@pytest.mark.django_db
def test_create_post():
    post = Post.objects.create(title="Test Title", content="Test Content")
    assert post.title == "Test Title"
    assert post.content == "Test Failure"
