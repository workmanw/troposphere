# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 31.1.0


from . import AWSObject
from . import AWSProperty
from .validators import boolean


class TransformationConfiguration(AWSProperty):
    props = {
        'Actions': ([basestring], False),
        'ContentTransformation': (dict, False),
    }


class ObjectLambdaConfiguration(AWSProperty):
    props = {
        'AllowedFeatures': ([basestring], False),
        'CloudWatchMetricsEnabled': (boolean, False),
        'SupportingAccessPoint': (basestring, True),
        'TransformationConfigurations':
            ([TransformationConfiguration], True),
    }


class AccessPoint(AWSObject):
    resource_type = "AWS::S3ObjectLambda::AccessPoint"

    props = {
        'Name': (basestring, True),
        'ObjectLambdaConfiguration': (ObjectLambdaConfiguration, False),
    }


class AccessPointPolicy(AWSObject):
    resource_type = "AWS::S3ObjectLambda::AccessPointPolicy"

    props = {
        'ObjectLambdaAccessPoint': (basestring, True),
        'PolicyDocument': (dict, True),
    }
