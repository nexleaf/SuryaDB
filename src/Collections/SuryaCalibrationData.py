'''
Created on Oct 29, 2010

@author: surya
'''

from mongoengine import *

class SuryaCalibrationData(Document):
    # Primary Key for the SuryaCalibration Table
    calibrationId = IntField(unique = True)

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

class SuryaImageAnalysisBCStripData(SuryaCalibrationData):
    
    # Provides 10 BC values on test strips
    bcStrips = ListField(FloatField(required=True), required=True, unique=True)

class SuryaImagePreProcessingCalibrationData(SuryaCalibrationData):
    
    # Resolution of the accumulator
    dp = IntField(required=True)
    
    # Minimum Radius of circles to detect
    minimumRadius = IntField(required=True)
    
    # Maximum Radius of circles to detect
    maximumRadius = IntField(required=True)
    
    # Minimum Distance between circles
    minimumDistance = IntField(required=True)
    
    # Accumulator Threshold to detect a circle
    accumulatorThreshold = IntField(required=True)
    
    # The edge detection threshold(the low threshold is half the high threshold by default)
    highThreshold = IntField(required=True)
    
    # Sampling factor
    samplingFactor = IntField(required=True)
    