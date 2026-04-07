from django.db import models
from apps.boards.models import Board


class Thread(models.Model):
    title = models.CharField(
        max_length=100,
        blank=True,
        help_text="Thread title"
    )
    
    content = models.TextField(
        help_text="More detailed content of the Thread"
    )
    
    anon_id = models.CharField(max_length=36, blank=True, db_index=True)
    
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='threads')

    image = models.ImageField(upload_to='threads/', blank=True, null=True) 

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Thread"
        verbose_name_plural = "Threads"

    def __str__(self):
        if self.title:
            title = (self.title[:20] + "...") if len(self.title) > 25 else self.title
        else:
            title = "Sem título"
        return f"{title} - {self.board}"