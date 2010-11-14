'''
Created on Oct 29, 2010

@author: surya
'''

from mongoengine import *
from SuryaUploadData import *
from SuryaCalibrationData import *
from SuryaProcessResult import *

class SuryaConfiguration(EmbeddedDocument):
    # A Reference to the Calibration Data
    calibrationData = ReferenceField(SuryaCalibrationData, required=True)
    
    # A List of Results obtained for this configuration
    resultList = ListField(EmbeddedDocumentField(SuryaResult))

# TODO: InvalidReason per Epoch
class SuryaProcessingList(Document):
    # The image/accoustic data to process
    processEntity = ReferenceField(SuryaUploadData, required=True)
    
    # A boolean field indicating if this image has been processed
    processedFlag = BooleanField(required=True)
    
    # Current epoch
    epoch = IntField(required=True)
    
    # The results obtained after preprocessing the image/accoustic data
    preProcessResultList = ListField(EmbeddedDocumentField(SuryaResult))
    
    # Its corresponding list of calibration configurations
    configurations = ListField(EmbeddedDocumentField(SuryaConfiguration))
    