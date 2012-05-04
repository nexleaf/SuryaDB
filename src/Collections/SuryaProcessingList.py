'''
Created on Oct 29, 2010

@author: surya
'''

from mongoengine import *
from SuryaUploadData import *
from SuryaCalibrationData import *

class SuryaProcessingList(Document):
    # The image/accoustic data to process
    processEntity = ReferenceField(SuryaUploadData, required=True)
    
    # The status of the processing, i.e. is this item being processed currently
    processingFlag = BooleanField(default=False, required=True)

    meta = {'allow_inheritance': True}
    
class SuryaIANAProcessingList(SuryaProcessingList):
    
    # A boolean field indicating if this image has been processed
    processedFlag = BooleanField(required=True)
    
    # Override flag, indicating if results from preProcessing can override the current calibration config
    overrideFlag = BooleanField(default=True, required=True)
    
    # The pre-processing configuration under which this item should be processed
    preProcessingConfiguration = ReferenceField(SuryaCalibrationData, required=True)
    
    # The computation configuration under which BCVol must be computed
    computationConfiguration = ReferenceField(SuryaCalibrationData, required=True)
    
    # The BCStrip value with which to process this item
    bcStrips = ReferenceField(SuryaCalibrationData, required=True)
