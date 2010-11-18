'''
Created on Oct 29, 2010

@author: surya
'''

from mongoengine import *
from SuryaCalibrationData import *


class SuryaDeploymentData(Document):
    # Each deployment ID can map to multiple calibration ID (but in a certain
    # time, there can be only one mapping)
    deploymentId = StringField(max_length=128, required=True)

    # The time that the calibration id becomes validate
    activateDatetime = DateTimeField(required=True)

    # FK to Calibration Collection
    calibrationId = ReferenceField(SuryaCalibrationData, required=True)