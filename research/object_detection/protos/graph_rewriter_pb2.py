# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: object_detection/protos/graph_rewriter.proto
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
    'object_detection/protos/graph_rewriter.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,object_detection/protos/graph_rewriter.proto\x12\x17object_detection.protos\"W\n\rGraphRewriter\x12;\n\x0cquantization\x18\x01 \x01(\x0b\x32%.object_detection.protos.Quantization*\t\x08\xe8\x07\x10\x80\x80\x80\x80\x02\"s\n\x0cQuantization\x12\x15\n\x05\x64\x65lay\x18\x01 \x01(\x05:\x06\x35\x30\x30\x30\x30\x30\x12\x16\n\x0bweight_bits\x18\x02 \x01(\x05:\x01\x38\x12\x1a\n\x0f\x61\x63tivation_bits\x18\x03 \x01(\x05:\x01\x38\x12\x18\n\tsymmetric\x18\x04 \x01(\x08:\x05\x66\x61lse')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.graph_rewriter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GRAPHREWRITER']._serialized_start=73
  _globals['_GRAPHREWRITER']._serialized_end=160
  _globals['_QUANTIZATION']._serialized_start=162
  _globals['_QUANTIZATION']._serialized_end=277
# @@protoc_insertion_point(module_scope)
