# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: object_detection/protos/grid_anchor_generator.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    '',
    'object_detection/protos/grid_anchor_generator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3object_detection/protos/grid_anchor_generator.proto\x12\x17object_detection.protos\"\xcd\x01\n\x13GridAnchorGenerator\x12\x13\n\x06height\x18\x01 \x01(\x05:\x03\x32\x35\x36\x12\x12\n\x05width\x18\x02 \x01(\x05:\x03\x32\x35\x36\x12\x19\n\rheight_stride\x18\x03 \x01(\x05:\x02\x31\x36\x12\x18\n\x0cwidth_stride\x18\x04 \x01(\x05:\x02\x31\x36\x12\x18\n\rheight_offset\x18\x05 \x01(\x05:\x01\x30\x12\x17\n\x0cwidth_offset\x18\x06 \x01(\x05:\x01\x30\x12\x0e\n\x06scales\x18\x07 \x03(\x02\x12\x15\n\raspect_ratios\x18\x08 \x03(\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.grid_anchor_generator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GRIDANCHORGENERATOR']._serialized_start=81
  _globals['_GRIDANCHORGENERATOR']._serialized_end=286
# @@protoc_insertion_point(module_scope)
