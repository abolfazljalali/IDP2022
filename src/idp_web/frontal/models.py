# -*- coding: utf-8 -*-
"""Database Model Module 

This whole document represents the models of the frontal application.
The purpose of this app (frontal) is to create the whole database for
spectral images that are in nature related to medical information.
However, this model is generalised in the level that users can store
different images, and categorize them by assigning different **tags**
and information to each image.
"""

from django.db import models


class Image(models.Model):
    """
    Image class contains the general information of image plus its location
    in the local machine file system. Using this technique, we do not need to
    be concerned about the complexity of data handling and large volume files.


    ...

    Attributes
    ----------
    directory_path : str
        the directory path where the image is stored on the local machine's file system.
    file_name : str
        file name stored on the local machine's file system.
    file_type : int
        the container or file format code.

    Methods
    -------
        None
    """


    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    directory_path = models.CharField('Directory Path', max_length=2048)
    file_name = models.CharField('File Name', max_length=2048)
    file_type = models.IntegerField()

    def __str__(self):
        '''
            Returns the file_name property of the class as the string form.
        '''
        return f'{self.id}) {self.file_name}'


class Mask(models.Model):
    """
    Mask class contains the general information of mask files plus its location
    in the local machine file system. Using this technique, we do not need to
    be concerned about the complexity of data handling and large volume files.


    ...

    Attributes
    ----------
    directory_path : str
        the directory path where the image is stored on the local machine's file system.
    file_name : str
        file name stored on the local machine's file system.
    file_type : int
        the container or file format code.

    Methods
    -------
        None
    """

    class Meta:
        verbose_name = "Mask"
        verbose_name_plural = "Masks"

    directory_path = models.CharField('Directory Path', max_length=2048)
    file_name = models.CharField('File Name', max_length=2048)
    file_type = models.IntegerField()
    
    def __str__(self) -> str:
        return self.file_name


class Tag(models.Model):
    """
    Image class contains the general information of image plus its location
    in the local machine file system. Using this technique, we do not need to
    be concerned about the complexity of data handling and large volume files.


    ...

    Attributes
    ----------
    directory_path : str
        the directory path where the image is stored on the local machine's file system.
    file_name : str
        file name stored on the local machine's file system.
    file_type : int
        the container or file format code.

    Methods
    -------
        None
    """

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    name = models.CharField('Name', max_length=2048)
    name = models.CharField('Name', max_length=2048)
    description = models.CharField('Description', max_length=4096)
    def __str__(self) -> str:
        return f'{self.name}'


class Annotation(models.Model):
    """
    Image class contains the general information of image plus its location
    in the local machine file system. Using this technique, we do not need to
    be concerned about the complexity of data handling and large volume files.


    ...

    Attributes
    ----------
    directory_path : str
        the directory path where the image is stored on the local machine's file system.
    file_name : str
        file name stored on the local machine's file system.
    file_type : int
        the container or file format code.

    Methods
    -------
        None
    """
    class Meta:
        verbose_name = "Annotation"
        verbose_name_plural = "Annotations"

    name = models.CharField('Name', max_length=2048)
    description = models.CharField('Description', max_length=4096)
    

class Color(models.Model):
    """
    Image class contains the general information of image plus its location
    in the local machine file system. Using this technique, we do not need to
    be concerned about the complexity of data handling and large volume files.


    ...

    Attributes
    ----------
    directory_path : str
        the directory path where the image is stored on the local machine's file system.
    file_name : str
        file name stored on the local machine's file system.
    file_type : int
        the container or file format code.

    Methods
    -------
        None
    """
    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    name = models.CharField('Name', max_length=2048)
    value = models.CharField('Value', max_length=2048)
    description = models.CharField('Description', max_length=4096)


class Polygon(models.Model):
    """
    Image class contains the general information of image plus its location
    in the local machine file system. Using this technique, we do not need to
    be concerned about the complexity of data handling and large volume files.


    ...

    Attributes
    ----------
    directory_path : str
        the directory path where the image is stored on the local machine's file system.
    file_name : str
        file name stored on the local machine's file system.
    file_type : int
        the container or file format code.

    Methods
    -------
        None
    """
    class Meta:
        verbose_name = "Polygon"
        verbose_name_plural = "Polygons"

    points = models.CharField('Points', max_length=2048)
    description = models.CharField('Description', max_length=4096)


class Segment(models.Model):
    """
    Image class contains the general information of image plus its location
    in the local machine file system. Using this technique, we do not need to
    be concerned about the complexity of data handling and large volume files.


    ...

    Attributes
    ----------
    directory_path : str
        the directory path where the image is stored on the local machine's file system.
    file_name : str
        file name stored on the local machine's file system.
    file_type : int
        the container or file format code.

    Methods
    -------
        None
    """
    class Meta:
        verbose_name = "Segment"
        verbose_name_plural = "Segments"

    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    polygon = models.ForeignKey(Polygon, on_delete=models.CASCADE)
    annotation = models.ForeignKey(Annotation, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)


class ImageMask(models.Model):
    """
    Image class contains the general information of image plus its location
    in the local machine file system. Using this technique, we do not need to
    be concerned about the complexity of data handling and large volume files.


    ...

    Attributes
    ----------
    directory_path : str
        the directory path where the image is stored on the local machine's file system.
    file_name : str
        file name stored on the local machine's file system.
    file_type : int
        the container or file format code.

    Methods
    -------
        None
    """
    class Meta:
        verbose_name = "Image Mask"
        verbose_name_plural = "Image Masks"
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    mask = models.ForeignKey(Mask, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.mask.file_name} -> {self.image.file_name}'


class ImageTag(models.Model):
    """
    Image class contains the general information of image plus its location
    in the local machine file system. Using this technique, we do not need to
    be concerned about the complexity of data handling and large volume files.


    ...

    Attributes
    ----------
    directory_path : str
        the directory path where the image is stored on the local machine's file system.
    file_name : str
        file name stored on the local machine's file system.
    file_type : int
        the container or file format code.

    Methods
    -------
        None
    """
    class Meta:
        verbose_name = "Image Tag"
        verbose_name_plural = "Image Tags"

    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    value = models.CharField('Value', max_length=4096)
    def __str__(self) -> str:
        return f'[{self.image.file_name}] {self.tag.name}:{self.value}'


class SegmentTag(models.Model):
    """
    Image class contains the general information of image plus its location
    in the local machine file system. Using this technique, we do not need to
    be concerned about the complexity of data handling and large volume files.


    ...

    Attributes
    ----------
    directory_path : str
        the directory path where the image is stored on the local machine's file system.
    file_name : str
        file name stored on the local machine's file system.
    file_type : int
        the container or file format code.

    Methods
    -------
        None
    """
    class Meta:
        verbose_name = "Segment Tag"
        verbose_name_plural = "Segment Tags"

    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    value = models.CharField('Value', max_length=4096)


class ErrorResponse(models.Model):
    """
    Image class contains the general information of image plus its location
    in the local machine file system. Using this technique, we do not need to
    be concerned about the complexity of data handling and large volume files.


    ...

    Attributes
    ----------
    directory_path : str
        the directory path where the image is stored on the local machine's file system.
    file_name : str
        file name stored on the local machine's file system.
    file_type : int
        the container or file format code.

    Methods
    -------
        None
    """
    class Meta:
        managed = False
    
    error_message = models.TextField('Error Message')