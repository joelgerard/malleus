# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: malleus/api/domain/protos/timing.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='malleus/api/domain/protos/timing.proto',
  package='malleus.api.domain',
  syntax='proto3',
  serialized_pb=_b('\n&malleus/api/domain/protos/timing.proto\x12\x12malleus.api.domain\"9\n\x06Timing\x12\r\n\x05start\x18\x01 \x01(\x02\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x02\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\tb\x06proto3')
)




_TIMING = _descriptor.Descriptor(
  name='Timing',
  full_name='malleus.api.domain.Timing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='malleus.api.domain.Timing.start', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='malleus.api.domain.Timing.end', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='malleus.api.domain.Timing.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=119,
)

DESCRIPTOR.message_types_by_name['Timing'] = _TIMING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Timing = _reflection.GeneratedProtocolMessageType('Timing', (_message.Message,), dict(
  DESCRIPTOR = _TIMING,
  __module__ = 'malleus.api.domain.protos.timing_pb2'
  # @@protoc_insertion_point(class_scope:malleus.api.domain.Timing)
  ))
_sym_db.RegisterMessage(Timing)


# @@protoc_insertion_point(module_scope)
