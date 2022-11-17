from django.test import TestCase
from . import models

# Create your tests here.


# Class for testing Image model
class ImageTestCase(TestCase):
    # Function to create a testing image
    def get_test_image(self):
        return models.Image.objects.create(directory_path="test", file_name="test", file_type=0)

    # Testing set up function
    def setUp(self):
        self.get_test_image()

    # Dry test
    def test_image_dry(self, image=None):
        if image is None:
            image = models.Image.objects.get(directory_path="test")
        self.assertEqual(image.directory_path, "test")
        self.assertEqual(image.file_name, "test")
        self.assertEqual(image.file_type, 0)
        self.assertEqual(str(image), image.file_name)

    # Variable type test
    def test_image_vartypes(self, image=None):
        if image is None:
            image = models.Image.objects.get(directory_path="test")
        self.assertIsInstance(image.directory_path, str)
        self.assertIsInstance(image.file_name, str)
        self.assertIsInstance(image.file_type, int)


# Class for testing Mask model
class MaskTestCase(TestCase):
    # Function to create a testing mask
    def get_test_mask(self):
        return models.Mask.objects.create(directory_path="test", file_name="test", file_type=0)

    # Testing set up function
    def setUp(self):
        self.get_test_mask()

    # Dry test
    def test_mask_dry(self, mask=None):
        if mask is None:
            mask = models.Mask.objects.get(directory_path="test")
        self.assertEqual(mask.directory_path, "test")
        self.assertEqual(mask.file_name, "test")
        self.assertEqual(mask.file_type, 0)

    # Variable type test
    def test_mask_vartypes(self, mask=None):
        if mask is None:
            mask = models.Mask.objects.get(directory_path="test")
        self.assertIsInstance(mask.directory_path, str)
        self.assertIsInstance(mask.file_name, str)
        self.assertIsInstance(mask.file_type, int)


# Class for testing Tag model
class TagTestCase(TestCase):
    # Function to create a testing tag
    def get_test_tag(self):
        return models.Tag.objects.create(name="test", description="test")

    # Testing set up function
    def setUp(self):
        self.get_test_tag()

    # Dry test
    def test_tag_dry(self, tag=None):
        if tag is None:
            tag = models.Tag.objects.get(name="test")
        self.assertEqual(tag.name, "test")
        self.assertEqual(tag.description, "test")
        self.assertEqual(str(tag), "test")

    # Variable type test
    def test_tag_vartypes(self, tag=None):
        if tag is None:
            tag = models.Tag.objects.get(name="test")
        self.assertIsInstance(tag.name, str)
        self.assertIsInstance(tag.description, str)


# Class for testing Annotation model
class AnnotationTestCase(TestCase):
    # Function to create a testing annotation
    def get_test_annotation(self):
        return models.Annotation.objects.create(name="test", description="test")

    # Testing set up function
    def setUp(self):
        self.get_test_annotation()

    # Dry test
    def test_annotation_dry(self, annotation=None):
        if annotation is None:
            annotation = models.Annotation.objects.get(name="test")
        self.assertEqual(annotation.name, "test")
        self.assertEqual(annotation.description, "test")

    # Variable type test
    def test_annotation_vartypes(self, annotation=None):
        if annotation is None:
            annotation = models.Annotation.objects.get(name="test")
        self.assertIsInstance(annotation.name, str)
        self.assertIsInstance(annotation.description, str)


# Class for testing Color model
class ColorTestCase(TestCase):
    # Function to create a testing color
    def get_test_color(self):
        return models.Color.objects.create(name="test", value="test", description="test")

    # Testing set up function
    def setUp(self):
        self.get_test_color()

    # Dry test
    def test_color_dry(self, color=None):
        if color is None:
            color = models.Color.objects.get(name="test")
        self.assertEqual(color.name, "test")
        self.assertEqual(color.name, "test")
        self.assertEqual(color.description, "test")

    # Variable type test
    def test_color_vartypes(self, color=None):
        if color is None:
            color = models.Color.objects.get(name="test")
        self.assertIsInstance(color.name, str)
        self.assertIsInstance(color.name, str)
        self.assertIsInstance(color.description, str)


# Class for testing Polygon model
class PolygonTestCase(TestCase):
    # Function to create a testing polygon
    def get_test_polygon(self):
        return models.Polygon.objects.create(points="test", description="test")

    # Testing set up function
    def setUp(self):
        self.get_test_polygon()

    # Dry test
    def test_polygon_dry(self, polygon=None):
        if polygon is None:
            polygon = models.Polygon.objects.get(points="test")
        self.assertEqual(polygon.points, "test")
        self.assertEqual(polygon.description, "test")

    # Variable type test
    def test_polygon_vartypes(self, polygon=None):
        if polygon is None:
            polygon = models.Polygon.objects.get(points="test")
        self.assertIsInstance(polygon.points, str)
        self.assertIsInstance(polygon.description, str)


# Class for testing Segment model
class SegmentTestCase(TestCase):
    # Creating test cases for foreign keys
    itc = ImageTestCase()
    ptc = PolygonTestCase()
    atc = AnnotationTestCase()
    ctc = ColorTestCase()

    # Image key
    image = None

    # Function to create test segment
    def get_test_segment(self):
        self.image = self.itc.get_test_image()
        polygon = self.ptc.get_test_polygon()
        annotation = self.atc.get_test_annotation()
        color = self.ctc.get_test_color()

        return models.Segment.objects.create(image=self.image, polygon=polygon, annotation=annotation, color=color)

    # Testing set up function
    def setUp(self):
        self.get_test_segment()

    # Dry test
    def test_segment_dry(self, segment=None):
        if segment is None:
            segment = models.Segment.objects.get(image=self.image)
        self.itc.test_image_dry(image=segment.image)
        self.ptc.test_polygon_dry(polygon=segment.polygon)
        self.atc.test_annotation_dry(annotation=segment.annotation)
        self.ctc.test_color_dry(color=segment.color)

    # Variable type test
    def test_segment_vartypes(self, segment=None):
        if segment is None:
            segment = models.Segment.objects.get(image=self.image)

        # Checking foreign key types
        self.assertIsInstance(segment.image, models.Image)
        self.assertIsInstance(segment.polygon, models.Polygon)
        self.assertIsInstance(segment.annotation, models.Annotation)
        self.assertIsInstance(segment.color, models.Color)

        # Checking types inside foreign keys
        self.itc.test_image_vartypes(image=segment.image)
        self.ptc.test_polygon_vartypes(polygon=segment.polygon)
        self.atc.test_annotation_vartypes(annotation=segment.annotation)
        self.ctc.test_color_vartypes(color=segment.color)


# Class for testing ImageMask model
class ImageMaskTestCase(TestCase):
    # Creating test cases for foreign keys
    itc = ImageTestCase()
    mtc = MaskTestCase()

    # Image key
    image = None

    # Function to create a testing image mask
    def get_test_imagemask(self):
        self.image = self.itc.get_test_image()
        mask = self.mtc.get_test_mask()

        return models.ImageMask.objects.create(image=self.image, mask=mask)

    # Testing set up function
    def setUp(self):
        self.get_test_imagemask()

    # Dry test
    def test_imagemask_dry(self, imagemask=None):
        if imagemask is None:
            imagemask = models.ImageMask.objects.get(image=self.image)
        self.itc.test_image_dry(imagemask.image)
        self.mtc.test_mask_dry(imagemask.mask)

    # Variable type test
    def test_imagemask_vartypes(self, imagemask=None):
        if imagemask is None:
            imagemask = models.ImageMask.objects.get(image=self.image)

        # Checking foreign key types
        self.assertIsInstance(imagemask.image, models.Image)
        self.assertIsInstance(imagemask.mask, models.Mask)

        # Checking types inside foreign keys
        self.itc.test_image_vartypes(imagemask.image)
        self.mtc.test_mask_vartypes(imagemask.mask)


# Class for testing ImageTag model
class ImageTagTestCase(TestCase):
    # Creating test cases for foreign keys
    itc = ImageTestCase()
    ttc = TagTestCase()

    # Image key
    image = None

    # Function to create a testing image tag
    def get_test_imagetag(self):
        self.image = self.itc.get_test_image()
        tag = self.ttc.get_test_tag()

        return models.ImageTag.objects.create(image=self.image, tag=tag, value="test")

    # Testing set up function
    def setUp(self):
        self.get_test_imagetag()

    # Dry test
    def test_imagetag_dry(self, imagetag=None):
        if imagetag is None:
            imagetag = models.ImageTag.objects.get(image=self.image)

        self.itc.test_image_dry(imagetag.image)
        self.ttc.test_tag_dry(imagetag.tag)

        self.assertEqual(imagetag.value, "test")
        self.assertEqual(str(imagetag), f'[{imagetag.image.file_name}] {imagetag.tag.name}:{imagetag.value}')

    # Variable type test
    def test_imagetag_vartypes(self, imagetag=None):
        if imagetag is None:
            imagetag = models.ImageTag.objects.get(image=self.image)

        # Checking foreign key types
        self.assertIsInstance(imagetag.image, models.Image)
        self.assertIsInstance(imagetag.tag, models.Tag)

        # Checking types inside foreign keys
        self.itc.test_image_vartypes(imagetag.image)
        self.ttc.test_tag_vartypes(imagetag.tag)

        self.assertIsInstance(imagetag.value, str)


# Class for testing SegmentTag model
class SegmentTagTestCase(TestCase):
    # Creating test cases for foreign keys
    stc = SegmentTestCase()
    ttc = TagTestCase()

    # Segment key
    segment = None

    # Function to create a testing segment tag
    def get_test_segmenttag(self):
        self.segment = self.stc.get_test_segment()
        tag = self.ttc.get_test_tag()

        return models.SegmentTag.objects.create(segment=self.segment, tag=tag, value="test")

    # Testing set up function
    def setUp(self):
        self.get_test_segmenttag()

    # Dry test
    def test_segmenttag_dry(self, segmenttag=None):
        if segmenttag is None:
            segmenttag = models.SegmentTag.objects.get(segment=self.segment)

        self.stc.test_segment_dry(segmenttag.segment)
        self.ttc.test_tag_dry(segmenttag.tag)

        self.assertEqual(segmenttag.value, "test")

    # Variable type test
    def test_segmenttag_vartypes(self, segmenttag=None):
        if segmenttag is None:
            segmenttag = models.SegmentTag.objects.get(segment=self.segment)

        # Checking foreign key types
        self.assertIsInstance(segmenttag.segment, models.Segment)
        self.assertIsInstance(segmenttag.tag, models.Tag)

        # Checking types inside foreign keys
        self.stc.test_segment_vartypes(segmenttag.segment)
        self.ttc.test_tag_vartypes(segmenttag.tag)

        self.assertIsInstance(segmenttag.value, str)
