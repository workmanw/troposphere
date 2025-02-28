# Copyright (c) 2012-2021, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***
# Resource specification version: 31.0.0


from troposphere import Tags

from . import AWSObject, AWSProperty
from .validators import boolean, integer


class Destination(AWSObject):
    resource_type = "AWS::IoTWireless::Destination"

    props = {
        "Description": (str, False),
        "Expression": (str, True),
        "ExpressionType": (str, True),
        "Name": (str, True),
        "RoleArn": (str, True),
        "Tags": (Tags, False),
    }


class LoRaWANDeviceProfile(AWSProperty):
    props = {
        "ClassBTimeout": (integer, False),
        "ClassCTimeout": (integer, False),
        "MacVersion": (str, False),
        "MaxDutyCycle": (integer, False),
        "MaxEirp": (integer, False),
        "PingSlotDr": (integer, False),
        "PingSlotFreq": (integer, False),
        "PingSlotPeriod": (integer, False),
        "RegParamsRevision": (str, False),
        "RfRegion": (str, False),
        "Supports32BitFCnt": (boolean, False),
        "SupportsClassB": (boolean, False),
        "SupportsClassC": (boolean, False),
        "SupportsJoin": (boolean, False),
    }


class DeviceProfile(AWSObject):
    resource_type = "AWS::IoTWireless::DeviceProfile"

    props = {
        "LoRaWAN": (LoRaWANDeviceProfile, False),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class LoRaWANServiceProfile(AWSProperty):
    props = {
        "AddGwMetadata": (boolean, False),
        "ChannelMask": (str, False),
        "DevStatusReqFreq": (integer, False),
        "DlBucketSize": (integer, False),
        "DlRate": (integer, False),
        "DlRatePolicy": (str, False),
        "DrMax": (integer, False),
        "DrMin": (integer, False),
        "HrAllowed": (boolean, False),
        "MinGwDiversity": (integer, False),
        "NwkGeoLoc": (boolean, False),
        "PrAllowed": (boolean, False),
        "RaAllowed": (boolean, False),
        "ReportDevStatusBattery": (boolean, False),
        "ReportDevStatusMargin": (boolean, False),
        "TargetPer": (integer, False),
        "UlBucketSize": (integer, False),
        "UlRate": (integer, False),
        "UlRatePolicy": (str, False),
    }


class ServiceProfile(AWSObject):
    resource_type = "AWS::IoTWireless::ServiceProfile"

    props = {
        "LoRaWAN": (LoRaWANServiceProfile, False),
        "Name": (str, False),
        "Tags": (Tags, False),
    }


class SessionKeysAbpV10x(AWSProperty):
    props = {
        "AppSKey": (str, True),
        "NwkSKey": (str, True),
    }


class AbpV10x(AWSProperty):
    props = {
        "DevAddr": (str, True),
        "SessionKeys": (SessionKeysAbpV10x, True),
    }


class SessionKeysAbpV11(AWSProperty):
    props = {
        "AppSKey": (str, True),
        "FNwkSIntKey": (str, True),
        "NwkSEncKey": (str, True),
        "SNwkSIntKey": (str, True),
    }


class AbpV11(AWSProperty):
    props = {
        "DevAddr": (str, True),
        "SessionKeys": (SessionKeysAbpV11, True),
    }


class OtaaV10x(AWSProperty):
    props = {
        "AppEui": (str, True),
        "AppKey": (str, True),
    }


class OtaaV11(AWSProperty):
    props = {
        "AppKey": (str, True),
        "JoinEui": (str, True),
        "NwkKey": (str, True),
    }


class LoRaWANDevice(AWSProperty):
    props = {
        "AbpV10x": (AbpV10x, False),
        "AbpV11": (AbpV11, False),
        "DevEui": (str, False),
        "DeviceProfileId": (str, False),
        "OtaaV10x": (OtaaV10x, False),
        "OtaaV11": (OtaaV11, False),
        "ServiceProfileId": (str, False),
    }


class WirelessDevice(AWSObject):
    resource_type = "AWS::IoTWireless::WirelessDevice"

    props = {
        "Description": (str, False),
        "DestinationName": (str, True),
        "LastUplinkReceivedAt": (str, False),
        "LoRaWAN": (LoRaWANDevice, False),
        "Name": (str, False),
        "Tags": (Tags, False),
        "ThingArn": (str, False),
        "Type": (str, True),
    }


class LoRaWANGateway(AWSProperty):
    props = {
        "GatewayEui": (str, True),
        "RfRegion": (str, True),
    }


class WirelessGateway(AWSObject):
    resource_type = "AWS::IoTWireless::WirelessGateway"

    props = {
        "Description": (str, False),
        "LastUplinkReceivedAt": (str, False),
        "LoRaWAN": (LoRaWANGateway, True),
        "Name": (str, False),
        "Tags": (Tags, False),
        "ThingArn": (str, False),
    }
