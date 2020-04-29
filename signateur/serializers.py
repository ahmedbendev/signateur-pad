from rest_framework import serializers
from .models import Signateur

class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class SignateurSerializer(serializers.ModelSerializer):
    img_data = Base64ImageField(max_length=None, use_url=True)

    class Meta:
       model = Signateur
       fields = ('img_data',)



















# from rest_framework import serializers
# from .models import Signateur
# import re
# import base64
# from django.core.files.base import ContentFile



# class SignateurSerializer(serializers.Serializer):
#     img_data = serializers.CharField()

#     def create(self , validated_data):
#         image = datavalidated_data["img_data"]
#         print(image)
#         sign = Signateur.objects.create(img_data=image)
#         sign.save()
#         return sign
#     def validate(self , data):
#         return data    

 
    # def to_internal_value(self, data):
    #     if isinstance(data, str) and data.startswith('data:image'):
    #         # base64 encoded image - decode
    #         format, imgstr = data.split(';base64,') # format ~= data:image/X,
    #         ext = format.split('/')[-1] # guess file extension
    #         id = uuid.uuid4()
    #         data = ContentFile(base64.b64decode(imgstr), name = id.urn[9:] + '.' + ext)
    #     return super(Base64ImageField, self).to_internal_value(data)





# class SignateurSerializer(serializers.ImageField):
#         img_data = serializers.SerializerMethodField()

#         def create(self , validated_data):
#             # dataUrlPattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
#             image_data = validated_data["img_data"]
#             # base64 encoded image - decode
#             format, imgstr = data.split(';base64,')  # format ~= data:image/X,
#             ext = format.split('/')[-1]  # guess file extension
#             print(ext)

#             # image_data = dataUrlPattern.match(image_data).group(2)
#             # image_data = image_data.encode()
#             # image_data = base64.b64decode(image_data)
#             # with open('screenshot.jpg', 'wb') as f:
#             #     f.write(image_data)
#             sign = Signateur.objects.create(image_data=image_data)
#             return sign



# class Base64ImageField(serializers.ImageField):
# def from_native(self, data):
# if isinstance(data, basestring) and data.startswith('data:image'):
# # base64 encoded image - decode
# format, imgstr = data.split(';base64,')  # format ~= data:image/X,
# ext = format.split('/')[-1]  # guess file extension
# data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
# return super(Base64ImageField, self).from_native(data)












# from .models import Signateur
# from rest_framework import serializers

# from django.core.files.base import ContentFile
# import base64
# import six
# import uuid
# import imghdr

# class Base64ImageField(serializers.ImageField):

#     def to_internal_value(self, data):

#         # Check if this is a base64 string
#         if isinstance(data, six.string_types):
#             # Check if the base64 string is in the "data:" format
#             if 'data:' in data and ';base64,' in data:
#             	# Break out the header from the base64 content
#             	header, data = data.split(';base64,')

#             # Try to decode the file. Return validation error if it fails.
#             try:
#             	decoded_file = base64.b64decode(data)
#             except TypeError:
#             	self.fail('invalid_image')

#             # Generate file name:
#             file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
#             # Get the file name extension:
#             file_extension = self.get_file_extension(file_name, decoded_file)

#             complete_file_name = "%s.%s" % (file_name, file_extension, )

#             data = ContentFile(decoded_file, name=complete_file_name)

#         return super(Base64ImageField, self).to_internal_value(data)

#     # def get_file_extension(self, file_name, decoded_file):

#     # 	extension = imghdr.what(file_name, decoded_file)
#     # 	extension = "jpg" if extension == "jpeg" else extension

#     # 	return extension


# class ImageSerializer(serializers.HyperlinkedModelSerializer):
#     image = Base64ImageField(
#         max_length=None, use_url=True,
#     )

#     class Meta:
#         model = Signateur
#         fields = ('img_data',)