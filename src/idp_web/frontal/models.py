# -*- coding: utf-8 -*-
"""Database Model Module 

Notice the comment above the docstring specifying the encoding.
Docstrings do appear in the bytecode, so you can access this through
the ``__doc__`` attribute. This is also what you'll see if you call
help() on a module or any other Python object.
"""

from django.db import models


class Image(models.Model):
    """Image Model 

    Notice the comment above the docstring specifying the encoding.
    Docstrings do appear in the bytecode, so you can access this through
    the ``__doc__`` attribute. This is also what you'll see if you call
    help() on a module or any other Python object.
    """
    directory_path = models.CharField('Directory Path', max_length=2048)
    file_name = models.CharField('File Name', max_length=2048)
    file_type = models.IntegerField()

    def __str__(self):
        '''
            Returns the file_name property of the class as the string form.
        '''
        return f'{self.file_name}'


class Mask(models.Model):
    """Mask Model 

    Notice the comment above the docstring specifying the encoding.
    Docstrings do appear in the bytecode, so you can access this through
    the ``__doc__`` attribute. This is also what you'll see if you call
    help() on a module or any other Python object.
    """
    directory_path = models.CharField('Directory Path', max_length=2048)
    file_name = models.CharField('File Name', max_length=2048)
    file_type = models.IntegerField()


class Tag(models.Model):
    """Tag Model 

    Notice the comment above the docstring specifying the encoding.
    Docstrings do appear in the bytecode, so you can access this through
    the ``__doc__`` attribute. This is also what you'll see if you call
    help() on a module or any other Python object.
    """
    name = models.CharField('Name', max_length=2048)
    description = models.CharField('Description', max_length=4096)
    def __str__(self) -> str:
        return f'{self.name}'


class Annotation(models.Model):
    name = models.CharField('Name', max_length=2048)
    description = models.CharField('Description', max_length=4096)
    

class Color(models.Model):
    name = models.CharField('Name', max_length=2048)
    value = models.CharField('Value', max_length=2048)
    description = models.CharField('Description', max_length=4096)


class Polygon(models.Model):
    points = models.CharField('Points', max_length=2048)
    description = models.CharField('Description', max_length=4096)


class Segment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    polygon = models.ForeignKey(Polygon, on_delete=models.CASCADE)
    annotation = models.ForeignKey(Annotation, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)


class ImageMask(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    mask = models.ForeignKey(Mask, on_delete=models.CASCADE)


class ImageTag(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    value = models.CharField('Value', max_length=4096)
    def __str__(self) -> str:
        return f'{self.tag.name}:{self.value}'


class SegmentTag(models.Model):
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    value = models.CharField('Value', max_length=4096)

