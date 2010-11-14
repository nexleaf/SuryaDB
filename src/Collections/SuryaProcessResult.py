'''
Created on Oct 29, 2010

@author: surya
'''

from mongoengine import *

class SuryaResult(EmbeddedDocument):
    pass

## THESE ARE RESULTS FROM THE IMAGE ANALYSIS ##

class BccResult(SuryaResult):
    fitRed         = ListField(FloatField(), required=True)
    fitGreen       = ListField(FloatField(), required=True)
    fitBlue        = ListField(FloatField(), required=True)
    rSquaredRed    = FloatField(required=True)
    rSquaredGreen  = FloatField(required=True)
    rSquaredBlue   = FloatField(required=True)
    sample         = ListField(FloatField(required=True), required=True)
    BCAreaRed      = FloatField(required=True)
    BCAreaGreen    = FloatField(required=True)
    BCAreaBlue     = FloatField(required=True)
    BCVolRed       = FloatField(required=True)
    BCVolGreen     = FloatField(required=True)
    BCVolBlue      = FloatField(required=True)

class SuryaImageAnalysisResult(SuryaResult):
    # The result on processing an image
    result = EmbeddedDocumentField(BccResult, required=True)
    
    # The Chart Image
    chartImage = FileField(required=True)
    
    # Epoch to which this result corresponds to
    epoch = IntField(required=True)
    
    # Whether this result has been emailed
    isEmailed = BooleanField(default=False)
    
    # The Status on analyzing the current image
    status = StringField(max_length=512, required=True)
    
class SuryaImagePreProcessingResult(SuryaResult):
    # The Debug Image
    debugImage = FileField(required=True)
    
    # The process status
    status = StringField(max_length=512, required=True)
    
    # If this has been emailed
    isEmailed = BooleanField(default=False)