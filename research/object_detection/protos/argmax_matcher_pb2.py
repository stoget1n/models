# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: object_detection/protos/argmax_matcher.proto
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
    'object_detection/protos/argmax_matcher.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,object_detection/protos/argmax_matcher.proto\x12\x17object_detection.protos\"\xec\x01\n\rArgMaxMatcher\x12\x1e\n\x11matched_threshold\x18\x01 \x01(\x02:\x03\x30.5\x12 \n\x13unmatched_threshold\x18\x02 \x01(\x02:\x03\x30.5\x12 \n\x11ignore_thresholds\x18\x03 \x01(\x08:\x05\x66\x61lse\x12,\n\x1enegatives_lower_than_unmatched\x18\x04 \x01(\x08:\x04true\x12\'\n\x18\x66orce_match_for_each_row\x18\x05 \x01(\x08:\x05\x66\x61lse\x12 \n\x11use_matmul_gather\x18\x06 \x01(\x08:\x05\x66\x61lse')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.argmax_matcher_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ARGMAXMATCHER']._serialized_start=74
  _globals['_ARGMAXMATCHER']._serialized_end=310
# @@protoc_insertion_point(module_scope)
