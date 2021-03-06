
from . import base
from .sensors_packet_pb2 import sensors_packet as pkt


class Producer(base.SensorProducer):
    event_name = 'linear_acc'

    schema = {
        'type': 'object',
        'properties': {
            'x': {
                'type': 'number'
            },
            'y': {
                'type': 'number'
            },
            'z': {
                'type': 'number'
            },
        },
        'required': ['x', 'y', 'z']
    }

    @staticmethod
    def pack(*, request, x, y, z):
        return pkt(
            sensor_linear_acc=pkt.SensorLinearAccPayload(
                x=x,
                y=y,
                z=z
            )
        )
