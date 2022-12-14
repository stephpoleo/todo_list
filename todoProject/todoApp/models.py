from django.db import models

# Create your models here.

class TodoModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    is_complete = models.BooleanField(null=True, blank=True)
    parent = models.ForeignKey(
        'TodoModel',
        related_name='children',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "todo"

    def __str__(self):
        if(self.parent_id == None):
            parent = 'Ninguno'
        else:
            parent = self.parent_id

        return "{} - {} - (Is Complete: {}) [{}]".format(self.id, self.name, self.is_complete, parent)

