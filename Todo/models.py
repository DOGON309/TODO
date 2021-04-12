from django.db import models

class TodoModel(models.Model):
	SELECT = (('高', '高'),('中', '中'), ('低', '低'))
	content = models.CharField(max_length = 100)
	select = models.CharField(max_length = 1, choices = SELECT)
	up_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content

	class Meta:
		ordering = ('-up_date',)