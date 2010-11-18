'''
Created on Oct 29, 2010

@author: surya
'''

from mongoengine import *
from Collections.SuryaUploadData import SuryaUploadData
from Collections.SuryaCalibrationData import SuryaImagePreProcessingCalibrationData,\
    SuryaImageAnalysisCalibrationData, SuryaImageAnalysisBCStripData

class SuryaResult(Document):
    pass


## THESE ARE RESULTS FROM THE IMAGE ANALYSIS ##

class BccResult(EmbeddedDocument):
    fitRed         = ListField(FloatField(), required=True)
    fitGreen       = ListField(FloatField(), required=True)
    fitBlue        = ListField(FloatField(), required=True)
    rSquaredRed    = FloatField(required=True)
    rSquaredGreen  = FloatField(required=True)
    rSquaredBlue   = FloatField(required=True)
    BCAreaRed      = FloatField(required=True)
    BCAreaGreen    = FloatField(required=True)
    BCAreaBlue     = FloatField(required=True)
    BCVolRed       = FloatField(required=True)
    BCVolGreen     = FloatField(required=True)
    BCVolBlue      = FloatField(required=True)

class SuryaImageAnalysisResult(EmbeddedDocument):    
    # The result on processing an image
    result = EmbeddedDocumentField(BccResult)
    
    # The Chart Image
    chartImage = FileField()
        
    # The Status on analyzing the current image
    status = StringField(max_length=512, required=True)
    
    # validFlag - True- if pre-processing was successful, False- otherwise
    validFlag = BooleanField(required=True)
    
class SuryaImagePreProcessingResult(EmbeddedDocument):    
    # The Debug Image
    debugImage = FileField()
    
    # validFlag - True- if pre-processing was successful, False- otherwise
    validFlag = BooleanField(required=True)
    
    # The process status
    status = StringField(max_length=512, required=True)
    
    # The Sampled value
    sampled = ListField(FloatField(required=True))
    
class SuryaIANAResult(SuryaResult):
    # The upload data item corresponding to the result
    item = ReferenceField(SuryaUploadData, required=True)
    
    # The pre-processing configuration under which this item was processed
    preProcessingConfiguration = ReferenceField(SuryaImagePreProcessingCalibrationData, required=True)

    # The image pre-processing result
    preProcessingResult = EmbeddedDocumentField(SuryaImagePreProcessingResult)
    
    # The calibration configuration under which image analysis result was computed
    computationConfiguration = ReferenceField(SuryaImageAnalysisCalibrationData, required=True)

    # The BCStrip value under which the image analysis result was computed
    bcStrips = ReferenceField(SuryaImageAnalysisBCStripData, required=True, unique_with=('preProcessingConfiguration','computationConfiguration','item'))
    
    # The image calibration result
    computationResult = EmbeddedDocumentField(SuryaImageAnalysisResult) 

    # The process status "PPROCCALIB", "PPROC", "COMPUCALIB", "COMPU", "SAVIN"
    status = StringField(max_length=512, required=True)
     
    # If this has been emailed
    isEmailed = BooleanField(default=False, required=True)
    
    # The Datetime corresponding to when this result was generated
    date = DateTimeField(required=True)

class SuryaIANAFailedResult(SuryaResult):
    # The upload data item corresponding to the result
    item = ReferenceField(SuryaUploadData, required=True)
    
    # The pre-processing configuration under which this item was processed
    preProcessingConfiguration = ReferenceField(SuryaImagePreProcessingCalibrationData)

    # The image pre-processing result
    preProcessingResult = EmbeddedDocumentField(SuryaImagePreProcessingResult)
    
    # The calibration configuration under which image analysis result was computed
    computationConfiguration = ReferenceField(SuryaImageAnalysisCalibrationData)

    # The BCStrip value under which the image analysis result was computed
    bcStrips = ReferenceField(SuryaImageAnalysisBCStripData)
    
    # The image calibration result
    computationResult = EmbeddedDocumentField(SuryaImageAnalysisResult) 

    # The process status "PPROCCALIB", "PPROC", "COMPUCALIB", "COMPU", "SAVIN"
    status = StringField(max_length=512, required=True)
     
    # If this has been emailed 
    isEmailed = BooleanField(default=False, required=True)
    
    # The Datetime corresponding to when this result was generated
    date = DateTimeField(required=True)
