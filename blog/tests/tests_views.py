import pytest
from django.urls import reverse
from blog.models import Post

@pytest.mark.django_db
def test_post_list_view(client):
    Post.objects.create(title="Test Post", content="Test Content")
    response = client.get(reverse("post_list"))
    assert response.status_code == 200
    assert "Test Failure" in response.content.decode()
