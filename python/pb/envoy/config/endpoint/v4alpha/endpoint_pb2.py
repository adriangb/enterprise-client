# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/endpoint/v4alpha/endpoint.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.endpoint.v4alpha import endpoint_components_pb2 as envoy_dot_config_dot_endpoint_dot_v4alpha_dot_endpoint__components__pb2
from envoy.type.v3 import percent_pb2 as envoy_dot_type_dot_v3_dot_percent__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/endpoint/v4alpha/endpoint.proto',
  package='envoy.config.endpoint.v4alpha',
  syntax='proto3',
  serialized_options=b'\n+io.envoyproxy.envoy.config.endpoint.v4alphaB\rEndpointProtoP\001\272\200\310\321\006\002\020\003',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,envoy/config/endpoint/v4alpha/endpoint.proto\x12\x1d\x65nvoy.config.endpoint.v4alpha\x1a\x37\x65nvoy/config/endpoint/v4alpha/endpoint_components.proto\x1a\x1b\x65nvoy/type/v3/percent.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"\xd2\x07\n\x15\x43lusterLoadAssignment\x12\x1d\n\x0c\x63luster_name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x45\n\tendpoints\x18\x02 \x03(\x0b\x32\x32.envoy.config.endpoint.v4alpha.LocalityLbEndpoints\x12\x61\n\x0fnamed_endpoints\x18\x05 \x03(\x0b\x32H.envoy.config.endpoint.v4alpha.ClusterLoadAssignment.NamedEndpointsEntry\x12K\n\x06policy\x18\x04 \x01(\x0b\x32;.envoy.config.endpoint.v4alpha.ClusterLoadAssignment.Policy\x1a\x8b\x04\n\x06Policy\x12`\n\x0e\x64rop_overloads\x18\x02 \x03(\x0b\x32H.envoy.config.endpoint.v4alpha.ClusterLoadAssignment.Policy.DropOverload\x12\x46\n\x17overprovisioning_factor\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x07\xfa\x42\x04*\x02 \x00\x12\x41\n\x14\x65ndpoint_stale_after\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xfa\x42\x05\xaa\x01\x02*\x00\x1a\xaf\x01\n\x0c\x44ropOverload\x12\x19\n\x08\x63\x61tegory\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x39\n\x0f\x64rop_percentage\x18\x02 \x01(\x0b\x32 .envoy.type.v3.FractionalPercent:I\x9a\xc5\x88\x1e\x44\nBenvoy.config.endpoint.v3.ClusterLoadAssignment.Policy.DropOverload:<\x9a\xc5\x88\x1e\x37\n5envoy.config.endpoint.v3.ClusterLoadAssignment.PolicyJ\x04\x08\x01\x10\x02J\x04\x08\x05\x10\x06R\x18\x64isable_overprovisioning\x1a^\n\x13NamedEndpointsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x36\n\x05value\x18\x02 \x01(\x0b\x32\'.envoy.config.endpoint.v4alpha.Endpoint:\x02\x38\x01:5\x9a\xc5\x88\x1e\x30\n.envoy.config.endpoint.v3.ClusterLoadAssignmentBF\n+io.envoyproxy.envoy.config.endpoint.v4alphaB\rEndpointProtoP\x01\xba\x80\xc8\xd1\x06\x02\x10\x03\x62\x06proto3'
  ,
  dependencies=[envoy_dot_config_dot_endpoint_dot_v4alpha_dot_endpoint__components__pb2.DESCRIPTOR,envoy_dot_type_dot_v3_dot_percent__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,udpa_dot_annotations_dot_status__pb2.DESCRIPTOR,udpa_dot_annotations_dot_versioning__pb2.DESCRIPTOR,validate_dot_validate__pb2.DESCRIPTOR,])




_CLUSTERLOADASSIGNMENT_POLICY_DROPOVERLOAD = _descriptor.Descriptor(
  name='DropOverload',
  full_name='envoy.config.endpoint.v4alpha.ClusterLoadAssignment.Policy.DropOverload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='category', full_name='envoy.config.endpoint.v4alpha.ClusterLoadAssignment.Policy.DropOverload.category', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='drop_percentage', full_name='envoy.config.endpoint.v4alpha.ClusterLoadAssignment.Policy.DropOverload.drop_percentage', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\036D\nBenvoy.config.endpoint.v3.ClusterLoadAssignment.Policy.DropOverload',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=873,
  serialized_end=1048,
)

_CLUSTERLOADASSIGNMENT_POLICY = _descriptor.Descriptor(
  name='Policy',
  full_name='envoy.config.endpoint.v4alpha.ClusterLoadAssignment.Policy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='drop_overloads', full_name='envoy.config.endpoint.v4alpha.ClusterLoadAssignment.Policy.drop_overloads', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='overprovisioning_factor', full_name='envoy.config.endpoint.v4alpha.ClusterLoadAssignment.Policy.overprovisioning_factor', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004*\002 \000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endpoint_stale_after', full_name='envoy.config.endpoint.v4alpha.ClusterLoadAssignment.Policy.endpoint_stale_after', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\252\001\002*\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CLUSTERLOADASSIGNMENT_POLICY_DROPOVERLOAD, ],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\0367\n5envoy.config.endpoint.v3.ClusterLoadAssignment.Policy',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=625,
  serialized_end=1148,
)

_CLUSTERLOADASSIGNMENT_NAMEDENDPOINTSENTRY = _descriptor.Descriptor(
  name='NamedEndpointsEntry',
  full_name='envoy.config.endpoint.v4alpha.ClusterLoadAssignment.NamedEndpointsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='envoy.config.endpoint.v4alpha.ClusterLoadAssignment.NamedEndpointsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='envoy.config.endpoint.v4alpha.ClusterLoadAssignment.NamedEndpointsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1150,
  serialized_end=1244,
)

_CLUSTERLOADASSIGNMENT = _descriptor.Descriptor(
  name='ClusterLoadAssignment',
  full_name='envoy.config.endpoint.v4alpha.ClusterLoadAssignment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster_name', full_name='envoy.config.endpoint.v4alpha.ClusterLoadAssignment.cluster_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='endpoints', full_name='envoy.config.endpoint.v4alpha.ClusterLoadAssignment.endpoints', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='named_endpoints', full_name='envoy.config.endpoint.v4alpha.ClusterLoadAssignment.named_endpoints', index=2,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='policy', full_name='envoy.config.endpoint.v4alpha.ClusterLoadAssignment.policy', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CLUSTERLOADASSIGNMENT_POLICY, _CLUSTERLOADASSIGNMENT_NAMEDENDPOINTSENTRY, ],
  enum_types=[
  ],
  serialized_options=b'\232\305\210\0360\n.envoy.config.endpoint.v3.ClusterLoadAssignment',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=321,
  serialized_end=1299,
)

_CLUSTERLOADASSIGNMENT_POLICY_DROPOVERLOAD.fields_by_name['drop_percentage'].message_type = envoy_dot_type_dot_v3_dot_percent__pb2._FRACTIONALPERCENT
_CLUSTERLOADASSIGNMENT_POLICY_DROPOVERLOAD.containing_type = _CLUSTERLOADASSIGNMENT_POLICY
_CLUSTERLOADASSIGNMENT_POLICY.fields_by_name['drop_overloads'].message_type = _CLUSTERLOADASSIGNMENT_POLICY_DROPOVERLOAD
_CLUSTERLOADASSIGNMENT_POLICY.fields_by_name['overprovisioning_factor'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT32VALUE
_CLUSTERLOADASSIGNMENT_POLICY.fields_by_name['endpoint_stale_after'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_CLUSTERLOADASSIGNMENT_POLICY.containing_type = _CLUSTERLOADASSIGNMENT
_CLUSTERLOADASSIGNMENT_NAMEDENDPOINTSENTRY.fields_by_name['value'].message_type = envoy_dot_config_dot_endpoint_dot_v4alpha_dot_endpoint__components__pb2._ENDPOINT
_CLUSTERLOADASSIGNMENT_NAMEDENDPOINTSENTRY.containing_type = _CLUSTERLOADASSIGNMENT
_CLUSTERLOADASSIGNMENT.fields_by_name['endpoints'].message_type = envoy_dot_config_dot_endpoint_dot_v4alpha_dot_endpoint__components__pb2._LOCALITYLBENDPOINTS
_CLUSTERLOADASSIGNMENT.fields_by_name['named_endpoints'].message_type = _CLUSTERLOADASSIGNMENT_NAMEDENDPOINTSENTRY
_CLUSTERLOADASSIGNMENT.fields_by_name['policy'].message_type = _CLUSTERLOADASSIGNMENT_POLICY
DESCRIPTOR.message_types_by_name['ClusterLoadAssignment'] = _CLUSTERLOADASSIGNMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClusterLoadAssignment = _reflection.GeneratedProtocolMessageType('ClusterLoadAssignment', (_message.Message,), {

  'Policy' : _reflection.GeneratedProtocolMessageType('Policy', (_message.Message,), {

    'DropOverload' : _reflection.GeneratedProtocolMessageType('DropOverload', (_message.Message,), {
      'DESCRIPTOR' : _CLUSTERLOADASSIGNMENT_POLICY_DROPOVERLOAD,
      '__module__' : 'envoy.config.endpoint.v4alpha.endpoint_pb2'
      # @@protoc_insertion_point(class_scope:envoy.config.endpoint.v4alpha.ClusterLoadAssignment.Policy.DropOverload)
      })
    ,
    'DESCRIPTOR' : _CLUSTERLOADASSIGNMENT_POLICY,
    '__module__' : 'envoy.config.endpoint.v4alpha.endpoint_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.endpoint.v4alpha.ClusterLoadAssignment.Policy)
    })
  ,

  'NamedEndpointsEntry' : _reflection.GeneratedProtocolMessageType('NamedEndpointsEntry', (_message.Message,), {
    'DESCRIPTOR' : _CLUSTERLOADASSIGNMENT_NAMEDENDPOINTSENTRY,
    '__module__' : 'envoy.config.endpoint.v4alpha.endpoint_pb2'
    # @@protoc_insertion_point(class_scope:envoy.config.endpoint.v4alpha.ClusterLoadAssignment.NamedEndpointsEntry)
    })
  ,
  'DESCRIPTOR' : _CLUSTERLOADASSIGNMENT,
  '__module__' : 'envoy.config.endpoint.v4alpha.endpoint_pb2'
  # @@protoc_insertion_point(class_scope:envoy.config.endpoint.v4alpha.ClusterLoadAssignment)
  })
_sym_db.RegisterMessage(ClusterLoadAssignment)
_sym_db.RegisterMessage(ClusterLoadAssignment.Policy)
_sym_db.RegisterMessage(ClusterLoadAssignment.Policy.DropOverload)
_sym_db.RegisterMessage(ClusterLoadAssignment.NamedEndpointsEntry)


DESCRIPTOR._options = None
_CLUSTERLOADASSIGNMENT_POLICY_DROPOVERLOAD.fields_by_name['category']._options = None
_CLUSTERLOADASSIGNMENT_POLICY_DROPOVERLOAD._options = None
_CLUSTERLOADASSIGNMENT_POLICY.fields_by_name['overprovisioning_factor']._options = None
_CLUSTERLOADASSIGNMENT_POLICY.fields_by_name['endpoint_stale_after']._options = None
_CLUSTERLOADASSIGNMENT_POLICY._options = None
_CLUSTERLOADASSIGNMENT_NAMEDENDPOINTSENTRY._options = None
_CLUSTERLOADASSIGNMENT.fields_by_name['cluster_name']._options = None
_CLUSTERLOADASSIGNMENT._options = None
# @@protoc_insertion_point(module_scope)
