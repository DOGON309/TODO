from django.db import models
from django.contrib.auth.models import User

class TodoModel(models.Model):
	SELECT = (('高', '高'),('中', '中'), ('低', '低'))
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_owner')
	content = models.CharField(max_length = 100)
	select = models.CharField(max_length = 1, choices = SELECT)
	up_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content

	class Meta:
		ordering = ('-up_date',)