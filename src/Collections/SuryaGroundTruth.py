'''
Created on Oct 26, 2010

@author: surya
'''

from mongoengine import *


class SuryaGroundTruth(Document):
    catalogNumber = StringField(max_length=50, required=True, unique=True)

# Schema No1
class SuryaGroundTruthSchema1(SuryaGroundTruth):
    startTime     = StringField(max_length=50, required=True)
    endTime       = StringField(max_length=50, required=True)
    totalTime     = FloatField(required=True)
    flowRate      = FloatField(required=True)
    ec_ug_cm2     = FloatField(required=True)
    ec_error_ug_cm2 = FloatField(required=True)
    aeth_conc_ug_m3 = FloatField(required=True)
    aeth_conc_ug_m2 = FloatField(required=True)
    filterDiameter = FloatField(required=True)
    gt_From       = StringField(max_length=5, required=True)
    location      = StringField(max_length=20, required=True)
    region        = StringField(max_length=20, required=True)
    red           = IntField(0,255, required=True)
    green         = IntField(0,255, required=True)
    blue          = IntField(0,255, required=True)
    bcStrip       = ListField(ListField(FloatField(required=True),required=True),required=True)
    