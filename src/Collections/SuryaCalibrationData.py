'''
Created on Oct 29, 2010

@author: surya
'''

from mongoengine import *

class SuryaCalibrationData(Document):
    # Primary Key for the SuryaCalibration Table
    calibrationId = IntField(primary_key = True)

## THESE ARE THE CALIBRATION VALUES FOR IMAGE ANALYSIS ##
class SuryaPump(Document):
    # Pump id
    PumpId = StringField(primary_key=True)
    
    # Air Flow rate (liters / minute)
    airFlowRate = FloatField(required=True)
 
class SuryaImageAnalysisCalibrationData(SuryaCalibrationData):

    # Air flow rate (liters / minute) 
    airFlowRate = FloatField(required=True)
    
    # ExposedTime (minutes)
    exposedTime = FloatField(required=True)
    
    # Filter Radius
    filterRadius = FloatField(required=True)

    # Area of the exposed image(cm^2) 
    bcArea = FloatField(required=True)

    # Provides 10 BC values on test strips
    bcStrips = ListField(FloatField(required=True), required=True)
    
    # FK to Pump Collection
    pumpId = ListField(ReferenceField(SuryaPump))