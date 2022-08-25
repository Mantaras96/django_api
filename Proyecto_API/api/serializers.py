
#The serializers will convert the Person model and Species
# model and others into JSON that will be used by the API to return the
# data to the user.
from django.core import serializers
from models import Person,Species

class PersonSerializer(serializers.ModelSerilizer):
        class Meta:
            model = Person
            fields = ('name', 'birth_year', 'eye_color', 'species')


class SpeciesSerializer(serializers.ModelSerilizer):
    class Meta:
        model = Species
        fields = ('name', 'classification', 'language')
