# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: routes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='routes.proto',
  package='dsc650.assignment03',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x0croutes.proto\x12\x13\x64sc650.assignment03\"\x90\x01\n\x07\x41irline\x12\x12\n\nairline_id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\r\n\x05\x61lias\x18\x03 \x01(\t\x12\x0c\n\x04iata\x18\x04 \x01(\t\x12\x0c\n\x04icao\x18\x05 \x01(\t\x12\x10\n\x08\x63\x61llsign\x18\x06 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x07 \x01(\t\x12\x15\n\x06\x61\x63tive\x18\x08 \x02(\x08:\x05\x66\x61lse\"\xd8\x01\n\x07\x41irport\x12\x12\n\nairport_id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ity\x18\x03 \x01(\t\x12\x0c\n\x04iata\x18\x04 \x01(\t\x12\x0c\n\x04icao\x18\x05 \x01(\t\x12\x10\n\x08latitude\x18\x06 \x02(\x01\x12\x11\n\tlongitude\x18\x07 \x02(\x01\x12\x10\n\x08\x61ltitude\x18\x08 \x01(\x05\x12\x10\n\x08timezone\x18\t \x01(\x01\x12\x0b\n\x03\x64st\x18\n \x01(\t\x12\r\n\x05tz_id\x18\x0b \x01(\t\x12\x0c\n\x04type\x18\x0c \x01(\t\x12\x0e\n\x06source\x18\r \x01(\t\"\xd8\x01\n\x05Route\x12-\n\x07\x61irline\x18\x01 \x01(\x0b\x32\x1c.dsc650.assignment03.Airline\x12\x31\n\x0bsrc_airport\x18\x02 \x01(\x0b\x32\x1c.dsc650.assignment03.Airport\x12\x31\n\x0b\x64st_airport\x18\x03 \x01(\x0b\x32\x1c.dsc650.assignment03.Airport\x12\x18\n\tcodeshare\x18\x04 \x02(\x08:\x05\x66\x61lse\x12\r\n\x05stops\x18\x05 \x01(\x05\x12\x11\n\tequipment\x18\x06 \x03(\t\"3\n\x06Routes\x12)\n\x05route\x18\x01 \x03(\x0b\x32\x1a.dsc650.assignment03.Route')
)




_AIRLINE = _descriptor.Descriptor(
  name='Airline',
  full_name='dsc650.assignment03.Airline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='airline_id', full_name='dsc650.assignment03.Airline.airline_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dsc650.assignment03.Airline.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alias', full_name='dsc650.assignment03.Airline.alias', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iata', full_name='dsc650.assignment03.Airline.iata', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icao', full_name='dsc650.assignment03.Airline.icao', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callsign', full_name='dsc650.assignment03.Airline.callsign', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country', full_name='dsc650.assignment03.Airline.country', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active', full_name='dsc650.assignment03.Airline.active', index=7,
      number=8, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=182,
)


_AIRLINE = _descriptor.Descriptor(
  name='Airline',
  full_name='dsc650.assignment03.Airline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='airline_id', full_name='dsc650.assignment03.Airline.airline_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='dsc650.assignment03.Airline.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='city', full_name='dsc650.assignment03.Airline.city', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iata', full_name='dsc650.assignment03.Airline.iata', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icao', full_name='dsc650.assignment03.Airline.icao', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='dsc650.assignment03.Airline.latitude', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='dsc650.assignment03.Airline.longitude', index=6,
      number=7, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='dsc650.assignment03.Airline.altitude', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='dsc650.assignment03.Airline.timezone', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dst', full_name='dsc650.assignment03.Airline.dst', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tz_id', full_name='dsc650.assignment03.Airline.tz_id', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='dsc650.assignment03.Airline.type', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source', full_name='dsc650.assignment03.Airline.source', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=401,
)


_ROUTE = _descriptor.Descriptor(
  name='Route',
  full_name='dsc650.assignment03.Route',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='airline', full_name='dsc650.assignment03.Route.airline', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src_airport', full_name='dsc650.assignment03.Route.src_airport', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dst_airport', full_name='dsc650.assignment03.Route.dst_airport', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeshare', full_name='dsc650.assignment03.Route.codeshare', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stops', full_name='dsc650.assignment03.Route.stops', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='equipment', full_name='dsc650.assignment03.Route.equipment', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=404,
  serialized_end=620,
)


_ROUTES = _descriptor.Descriptor(
  name='Routes',
  full_name='dsc650.assignment03.Routes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='route', full_name='dsc650.assignment03.Routes.route', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=622,
  serialized_end=673,
)

_ROUTE.fields_by_name['airline'].message_type = _AIRLINE
_ROUTE.fields_by_name['src_airport'].message_type = _AIRPORT
_ROUTE.fields_by_name['dst_airport'].message_type = _AIRPORT
_ROUTES.fields_by_name['route'].message_type = _ROUTE
DESCRIPTOR.message_types_by_name['Airline'] = _AIRLINE
DESCRIPTOR.message_types_by_name['Airport'] = _AIRPORT
DESCRIPTOR.message_types_by_name['Route'] = _ROUTE
DESCRIPTOR.message_types_by_name['Routes'] = _ROUTES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Airline = _reflection.GeneratedProtocolMessageType('Airline', (_message.Message,), dict(
  DESCRIPTOR = _AIRLINE,
  __module__ = 'routes_pb2'
  # @@protoc_insertion_point(class_scope:dsc650.assignment03.Airline)
  ))
_sym_db.RegisterMessage(Airline)

Airport = _reflection.GeneratedProtocolMessageType('Airport', (_message.Message,), dict(
  DESCRIPTOR = _AIRPORT,
  __module__ = 'routes_pb2'
  # @@protoc_insertion_point(class_scope:dsc650.assignment03.Airport)
  ))
_sym_db.RegisterMessage(Airport)

Route = _reflection.GeneratedProtocolMessageType('Route', (_message.Message,), dict(
  DESCRIPTOR = _ROUTE,
  __module__ = 'routes_pb2'
  # @@protoc_insertion_point(class_scope:dsc650.assignment03.Route)
  ))
_sym_db.RegisterMessage(Route)

Routes = _reflection.GeneratedProtocolMessageType('Routes', (_message.Message,), dict(
  DESCRIPTOR = _ROUTES,
  __module__ = 'routes_pb2'
  # @@protoc_insertion_point(class_scope:dsc650.assignment03.Routes)
  ))
_sym_db.RegisterMessage(Routes)


# @@protoc_insertion_point(module_scope)
