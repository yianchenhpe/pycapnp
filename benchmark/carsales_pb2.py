# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: carsales.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="carsales.proto",
    package="capnp.benchmark.protobuf",
    syntax="proto2",
    serialized_pb=_b(
        '\n\x0e\x63\x61rsales.proto\x12\x18\x63\x61pnp.benchmark.protobuf"8\n\nParkingLot\x12*\n\x03\x63\x61r\x18\x01 \x03(\x0b\x32\x1d.capnp.benchmark.protobuf.Car"\x1c\n\nTotalValue\x12\x0e\n\x06\x61mount\x18\x01 \x02(\x04"\xbc\x03\n\x03\x43\x61r\x12\x0c\n\x04make\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12.\n\x05\x63olor\x18\x03 \x01(\x0e\x32\x1f.capnp.benchmark.protobuf.Color\x12\r\n\x05seats\x18\x04 \x01(\r\x12\r\n\x05\x64oors\x18\x05 \x01(\r\x12.\n\x05wheel\x18\x06 \x03(\x0b\x32\x1f.capnp.benchmark.protobuf.Wheel\x12\x0e\n\x06length\x18\x07 \x01(\r\x12\r\n\x05width\x18\x08 \x01(\r\x12\x0e\n\x06height\x18\t \x01(\r\x12\x0e\n\x06weight\x18\n \x01(\r\x12\x30\n\x06\x65ngine\x18\x0b \x01(\x0b\x32 .capnp.benchmark.protobuf.Engine\x12\x15\n\rfuel_capacity\x18\x0c \x01(\x02\x12\x12\n\nfuel_level\x18\r \x01(\x02\x12\x19\n\x11has_power_windows\x18\x0e \x01(\x08\x12\x1a\n\x12has_power_steering\x18\x0f \x01(\x08\x12\x1a\n\x12has_cruise_control\x18\x10 \x01(\x08\x12\x13\n\x0b\x63up_holders\x18\x11 \x01(\r\x12\x16\n\x0ehas_nav_system\x18\x12 \x01(\x08"C\n\x05Wheel\x12\x10\n\x08\x64iameter\x18\x01 \x01(\r\x12\x14\n\x0c\x61ir_pressure\x18\x02 \x01(\x02\x12\x12\n\nsnow_tires\x18\x03 \x01(\x08"d\n\x06\x45ngine\x12\x12\n\nhorsepower\x18\x01 \x01(\r\x12\x11\n\tcylinders\x18\x02 \x01(\r\x12\n\n\x02\x63\x63\x18\x03 \x01(\r\x12\x10\n\x08uses_gas\x18\x04 \x01(\x08\x12\x15\n\ruses_electric\x18\x05 \x01(\x08*j\n\x05\x43olor\x12\t\n\x05\x42LACK\x10\x00\x12\t\n\x05WHITE\x10\x01\x12\x07\n\x03RED\x10\x02\x12\t\n\x05GREEN\x10\x03\x12\x08\n\x04\x42LUE\x10\x04\x12\x08\n\x04\x43YAN\x10\x05\x12\x0b\n\x07MAGENTA\x10\x06\x12\n\n\x06YELLOW\x10\x07\x12\n\n\x06SILVER\x10\x08'
    ),
)

_COLOR = _descriptor.EnumDescriptor(
    name="Color",
    full_name="capnp.benchmark.protobuf.Color",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="BLACK", index=0, number=0, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="WHITE", index=1, number=1, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="RED", index=2, number=2, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="GREEN", index=3, number=3, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="BLUE", index=4, number=4, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="CYAN", index=5, number=5, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="MAGENTA", index=6, number=6, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="YELLOW", index=7, number=7, options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="SILVER", index=8, number=8, options=None, type=None
        ),
    ],
    containing_type=None,
    options=None,
    serialized_start=750,
    serialized_end=856,
)
_sym_db.RegisterEnumDescriptor(_COLOR)

Color = enum_type_wrapper.EnumTypeWrapper(_COLOR)
BLACK = 0
WHITE = 1
RED = 2
GREEN = 3
BLUE = 4
CYAN = 5
MAGENTA = 6
YELLOW = 7
SILVER = 8


_PARKINGLOT = _descriptor.Descriptor(
    name="ParkingLot",
    full_name="capnp.benchmark.protobuf.ParkingLot",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="car",
            full_name="capnp.benchmark.protobuf.ParkingLot.car",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=44,
    serialized_end=100,
)


_TOTALVALUE = _descriptor.Descriptor(
    name="TotalValue",
    full_name="capnp.benchmark.protobuf.TotalValue",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="amount",
            full_name="capnp.benchmark.protobuf.TotalValue.amount",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=2,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=102,
    serialized_end=130,
)


_CAR = _descriptor.Descriptor(
    name="Car",
    full_name="capnp.benchmark.protobuf.Car",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="make",
            full_name="capnp.benchmark.protobuf.Car.make",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="model",
            full_name="capnp.benchmark.protobuf.Car.model",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="color",
            full_name="capnp.benchmark.protobuf.Car.color",
            index=2,
            number=3,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="seats",
            full_name="capnp.benchmark.protobuf.Car.seats",
            index=3,
            number=4,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="doors",
            full_name="capnp.benchmark.protobuf.Car.doors",
            index=4,
            number=5,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="wheel",
            full_name="capnp.benchmark.protobuf.Car.wheel",
            index=5,
            number=6,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="length",
            full_name="capnp.benchmark.protobuf.Car.length",
            index=6,
            number=7,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="width",
            full_name="capnp.benchmark.protobuf.Car.width",
            index=7,
            number=8,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="height",
            full_name="capnp.benchmark.protobuf.Car.height",
            index=8,
            number=9,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="weight",
            full_name="capnp.benchmark.protobuf.Car.weight",
            index=9,
            number=10,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="engine",
            full_name="capnp.benchmark.protobuf.Car.engine",
            index=10,
            number=11,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="fuel_capacity",
            full_name="capnp.benchmark.protobuf.Car.fuel_capacity",
            index=11,
            number=12,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="fuel_level",
            full_name="capnp.benchmark.protobuf.Car.fuel_level",
            index=12,
            number=13,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="has_power_windows",
            full_name="capnp.benchmark.protobuf.Car.has_power_windows",
            index=13,
            number=14,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="has_power_steering",
            full_name="capnp.benchmark.protobuf.Car.has_power_steering",
            index=14,
            number=15,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="has_cruise_control",
            full_name="capnp.benchmark.protobuf.Car.has_cruise_control",
            index=15,
            number=16,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="cup_holders",
            full_name="capnp.benchmark.protobuf.Car.cup_holders",
            index=16,
            number=17,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="has_nav_system",
            full_name="capnp.benchmark.protobuf.Car.has_nav_system",
            index=17,
            number=18,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=133,
    serialized_end=577,
)


_WHEEL = _descriptor.Descriptor(
    name="Wheel",
    full_name="capnp.benchmark.protobuf.Wheel",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="diameter",
            full_name="capnp.benchmark.protobuf.Wheel.diameter",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="air_pressure",
            full_name="capnp.benchmark.protobuf.Wheel.air_pressure",
            index=1,
            number=2,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="snow_tires",
            full_name="capnp.benchmark.protobuf.Wheel.snow_tires",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=579,
    serialized_end=646,
)


_ENGINE = _descriptor.Descriptor(
    name="Engine",
    full_name="capnp.benchmark.protobuf.Engine",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="horsepower",
            full_name="capnp.benchmark.protobuf.Engine.horsepower",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="cylinders",
            full_name="capnp.benchmark.protobuf.Engine.cylinders",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="cc",
            full_name="capnp.benchmark.protobuf.Engine.cc",
            index=2,
            number=3,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="uses_gas",
            full_name="capnp.benchmark.protobuf.Engine.uses_gas",
            index=3,
            number=4,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
        _descriptor.FieldDescriptor(
            name="uses_electric",
            full_name="capnp.benchmark.protobuf.Engine.uses_electric",
            index=4,
            number=5,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=648,
    serialized_end=748,
)

_PARKINGLOT.fields_by_name["car"].message_type = _CAR
_CAR.fields_by_name["color"].enum_type = _COLOR
_CAR.fields_by_name["wheel"].message_type = _WHEEL
_CAR.fields_by_name["engine"].message_type = _ENGINE
DESCRIPTOR.message_types_by_name["ParkingLot"] = _PARKINGLOT
DESCRIPTOR.message_types_by_name["TotalValue"] = _TOTALVALUE
DESCRIPTOR.message_types_by_name["Car"] = _CAR
DESCRIPTOR.message_types_by_name["Wheel"] = _WHEEL
DESCRIPTOR.message_types_by_name["Engine"] = _ENGINE
DESCRIPTOR.enum_types_by_name["Color"] = _COLOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParkingLot = _reflection.GeneratedProtocolMessageType(
    "ParkingLot",
    (_message.Message,),
    dict(
        DESCRIPTOR=_PARKINGLOT,
        __module__="carsales_pb2",
        # @@protoc_insertion_point(class_scope:capnp.benchmark.protobuf.ParkingLot)
    ),
)
_sym_db.RegisterMessage(ParkingLot)

TotalValue = _reflection.GeneratedProtocolMessageType(
    "TotalValue",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TOTALVALUE,
        __module__="carsales_pb2",
        # @@protoc_insertion_point(class_scope:capnp.benchmark.protobuf.TotalValue)
    ),
)
_sym_db.RegisterMessage(TotalValue)

Car = _reflection.GeneratedProtocolMessageType(
    "Car",
    (_message.Message,),
    dict(
        DESCRIPTOR=_CAR,
        __module__="carsales_pb2",
        # @@protoc_insertion_point(class_scope:capnp.benchmark.protobuf.Car)
    ),
)
_sym_db.RegisterMessage(Car)

Wheel = _reflection.GeneratedProtocolMessageType(
    "Wheel",
    (_message.Message,),
    dict(
        DESCRIPTOR=_WHEEL,
        __module__="carsales_pb2",
        # @@protoc_insertion_point(class_scope:capnp.benchmark.protobuf.Wheel)
    ),
)
_sym_db.RegisterMessage(Wheel)

Engine = _reflection.GeneratedProtocolMessageType(
    "Engine",
    (_message.Message,),
    dict(
        DESCRIPTOR=_ENGINE,
        __module__="carsales_pb2",
        # @@protoc_insertion_point(class_scope:capnp.benchmark.protobuf.Engine)
    ),
)
_sym_db.RegisterMessage(Engine)


# @@protoc_insertion_point(module_scope)
