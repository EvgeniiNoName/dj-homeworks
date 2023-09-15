import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_retrieve_course(api_client, course_factory):
    # Arrage
    course = course_factory()

    # Act
    response = api_client.get(f'/api/v1/courses/{course.id}/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == course.id
    assert data['name'] == course.name


@pytest.mark.django_db
def test_list_course(api_client, course_factory):
    # Arrage
    courses = course_factory(_quantity=5)

    # Act
    response = api_client.get('/api/v1/courses/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, course in enumerate(courses):
        assert data[i]['id'] == course.id
        assert data[i]['name'] == course.name


@pytest.mark.django_db
def test_filter_courses_by_id(api_client, course_factory):
    # Arrage
    courses = course_factory(_quantity=3)

    # Act
    id = courses[1].id
    response = api_client.get(f'/api/v1/courses/', {'id': id})

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == courses[1].id
    assert data[0]['name'] == courses[1].name


@pytest.mark.django_db
def test_filter_courses_by_name(api_client, course_factory):
    # Arrage
    course = course_factory(_quantity=3)
    name_course = course[1].name

    # Act
    response = api_client.get('/api/v1/courses/', {'name': name_course})

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == course[1].id
    assert data[0]['name'] == course[1].name


@pytest.mark.django_db
def test_create_course(api_client):
    # Arrange
    course_data = {
        'name': 'Math',
        'students': []
    }

    # Act
    response = api_client.post('/api/v1/courses/', course_data)

    # Assert
    assert response.status_code == 201
    assert Course.objects.count() == 1
    course = Course.objects.first()
    assert course.name == course_data['name']

@pytest.mark.django_db
def test_update_course(api_client, course_factory):
    # Arrange
    course = course_factory()
    update_course_data = {
        'name': 'Математика высшая',
        'students': []
    }

    # Act
    id = course.id
    response = api_client.put(f'/api/v1/courses/{id}/', update_course_data, format='json')

    # Assert
    assert response.status_code == 200
    course.refresh_from_db()
    assert course.name == update_course_data['name']

@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    # Arrange
    course = course_factory()

    # Act
    id = course.id
    response = api_client.delete(f'/api/v1/courses/{id}/')

    # Assert
    assert response.status_code == 204
