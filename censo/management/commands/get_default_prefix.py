# coding: utf-8

from censo import models

from django.forms.models import inlineformset_factory

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):

    args = 'referenced_class referencing_class'
    help = "Run this command to display the default form prefix of a model pointing with a foreign key to another, e.g. python manage.py get_default_prefix Cuerpo CuerpoOtherOfficial"

    def handle(self, *args, **options):
        if len(args) != 2:
            raise CommandError('You must specify the referenced_class and the referencing_class')
        referenced_class = getattr(models, args[0])
        referencing_class = getattr(models, args[1])
        try:
            f = inlineformset_factory(referenced_class, referencing_class)
            print "the prefix is %s" % f.get_default_prefix()
        except AttributeError:
            raise CommandError('The values you entered are not classes, you must specify class names')
        except:
            raise CommandError('The classes you entered are not associated, maybe you specified them swapped?')
            
