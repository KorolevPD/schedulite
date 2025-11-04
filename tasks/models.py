from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db import models


User = get_user_model()

class Tag(models.Model):
    """
    Tag model.

    ---------

    Represents a user-specific contextual category for organizing tasks
    (e.g., "Morning Routine", "Work", "Learning"). Each tag belongs to a user
    and includes an optional active schedule indicating when it is relevant.

    Attributes:
        user (User): The owner of the tag. Only this user can access or modify
        it.
        name (str): Unique name of the tag per user.
        description (str): Optional description providing additional context.
        active_days (JSON): Weekly schedule indicating when the tag is active.
            Example:
            {
                "mon": ["06:00", "10:00"],
                "tue": ["06:00", "10:00"],
                "sun": null
            }
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tags"
    )
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    active_days = models.JSONField(
        blank=True, null=True,
        help_text='{"mon": ["06:00", "10:00"],'
        '"tue": ["06:00", "10:00"], "sun": null}'
    )

    # def __str__(self):
    #     return self.name


class Task(models.Model):
    """
    Task model.

    ----------

    Represents a user-defined task with flexible scheduling and tagging.
    Each task belongs to a specific user and can be associated with multiple
    tags.
    Tasks can be finite (with a defined total duration) or infinite
    (habit-like), and may have unique execution times for each day of the week.

    Attributes:
        user (User): The owner of the task. Only this user can view or modify
        it.
        name (str): The title of the task.
        description (str): Optional detailed description.
        tags (ManyToMany[Tag]): Related tags representing contextual or
        time-based categories.
        start_date (date): The date when the task becomes active.
        duration_type (str): Defines whether the task is finite or infinite.
        total_hours (int, optional): Total duration in hours if the task is
        finite.
        repeat_monthly (bool): Indicates whether the task repeats monthly.
        days_of_week (JSON): Weekly schedule mapping days to execution times.
            Example:
            {
                "mon": "08:00",
                "wed": "09:30",
                "sun": null
            }
        created_at (datetime): Timestamp of creation.
        updated_at (datetime): Timestamp of the last modification.
    """

    INFINITE = 'infinite'
    FINITE = 'finite'

    DURATION_TYPE_CHOICES = [
        (INFINITE, 'Бесконечная'),
        (FINITE, 'Конечная'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='tasks')

    start_date = models.DateField(default=timezone.now)
    duration_type = models.CharField(
        max_length=10, choices=DURATION_TYPE_CHOICES, default=INFINITE
    )
    total_hours = models.PositiveIntegerField(
        null=True, blank=True,
        help_text="Указать, если задача конечная (в часах)"
    )

    repeat_monthly = models.BooleanField(default=False)
    days_of_week = models.JSONField(
        blank=True, null=True,
        help_text='Например: {"mon": "08:00", "wed": "09:30", "sun": null}'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name
