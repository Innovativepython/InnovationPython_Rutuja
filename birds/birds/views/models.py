from django.db import models
import xmltodict


class Xml(models.Model):
    def list(self):
        with open('birds_north_america.xml', 'r') as myfile:
            obj = xmltodict.parse(myfile.read())
        return obj