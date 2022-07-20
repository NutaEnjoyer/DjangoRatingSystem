from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Person(models.Model):
	name = models.CharField(max_length=100, verbose_name='Name')
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
	pub_date = models.DateTimeField(editable=False, auto_now_add=True, verbose_name='Date published')
	change_date = models.DateTimeField(auto_now=True, verbose_name='Date changed')
	is_scum = models.BooleanField(default=False, verbose_name='Scum')

	class Meta:
		verbose_name = 'Person'
		verbose_name_plural = 'Persons'
		ordering = ['-pub_date']

	def __str__(self):
		return self.name


class Mark(models.Model):
	from_person = models.ForeignKey(Person, related_name='from_person_mark', null=True, on_delete=models.SET_NULL, verbose_name='From person')
	to_person = models.ForeignKey(Person, related_name='to_person_mark', on_delete=models.CASCADE, verbose_name='To person')
	mark = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)], verbose_name='Mark')

	class Meta:
		verbose_name = 'Mark'
		verbose_name_plural = 'Marks'

	def __str__(self):
		return str(self.pk)


class Comment(models.Model):
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
	from_person = models.ForeignKey(Person, related_name='from_person_comment', null=True, on_delete=models.SET_NULL, verbose_name='From person')
	to_person = models.ForeignKey(Person, related_name='to_person_comment', on_delete=models.CASCADE, verbose_name='To person')
	text = models.TextField(max_length=1000, default=True, verbose_name='Positive')
	pub_date = models.DateTimeField(editable=False, auto_now_add=True, verbose_name='Date published')
	change_date = models.DateTimeField(auto_now=True, verbose_name='Date changed')

	class Meta:
		verbose_name = 'Comment'
		verbose_name_plural = 'Comments'

	def __str__(self):
		return self.text[:30] + '..'


class CommentMark(models.Model):
	from_person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL, verbose_name='From person')
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='Comment')
	is_positive = models.BooleanField(verbose_name='Positive')

	class Meta:
		verbose_name = 'CommentMark'
		verbose_name_plural = 'CommentMarks'

	def __str__(self):
		return str(self.pk)
