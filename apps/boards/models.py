from django.db import models


class Board(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Board name (ex: Technology, Random)"
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        help_text="Short identifier (ex: tech, b)"
    )
    description = models.TextField(
        blank=True,
        help_text="Short board description"
    )
    is_nsfw = models.BooleanField(
        default=False,
        help_text="Defines wether the board is NSFW or not"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    def __str__(self):
        return f"/{self.slug}/ - {self.name}"