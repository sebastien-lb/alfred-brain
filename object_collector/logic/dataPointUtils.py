from object_collector.models import *
from object_collector.serializers import DataPointSerializer

from .dataTypeConversion import fromBinary


def getLatestDataPointFromDataSource(data_source_id):
    data_source = DataSource.objects.get(pk=data_source_id)

    try:
        data_point = DataPoint.objects.filter(data_source=data_source).latest("timestamp")
    except:
        return None
    data_point_serializer = DataPointSerializer(data_point)
    # serializer doesn't work with binary
    ret_val = data_point_serializer.data
    ret_val["value"] = fromBinary(data_point.value, data_source.data_type.name)
    return ret_val


def getLatestDataPointsFromDataSource(data_source_id, nb_points = 10):
    data_source = DataSource.objects.get(pk=data_source_id)

    try:
        data_points = DataPoint.objects.filter(data_source=data_source).order_by("-timestamp")[:nb_points]
    except:
        return None
    ret_val = []
    for data_point in data_points:
        data_point_serializer = DataPointSerializer(data_point)
        # serializer doesn't work with binary
        point = data_point_serializer.data
        point["value"] = fromBinary(data_point.value, data_source.data_type.name)
        ret_val.append(point)
    return ret_val