# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: object_detection/protos/region_similarity_calculator.proto
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
    'object_detection/protos/region_similarity_calculator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:object_detection/protos/region_similarity_calculator.proto\x12\x17object_detection.protos\"\xde\x02\n\x1aRegionSimilarityCalculator\x12N\n\x16neg_sq_dist_similarity\x18\x01 \x01(\x0b\x32,.object_detection.protos.NegSqDistSimilarityH\x00\x12@\n\x0eiou_similarity\x18\x02 \x01(\x0b\x32&.object_detection.protos.IouSimilarityH\x00\x12@\n\x0eioa_similarity\x18\x03 \x01(\x0b\x32&.object_detection.protos.IoaSimilarityH\x00\x12W\n\x1athresholded_iou_similarity\x18\x04 \x01(\x0b\x32\x31.object_detection.protos.ThresholdedIouSimilarityH\x00\x42\x13\n\x11region_similarity\"\x15\n\x13NegSqDistSimilarity\"\x0f\n\rIouSimilarity\"\x0f\n\rIoaSimilarity\"6\n\x18ThresholdedIouSimilarity\x12\x1a\n\riou_threshold\x18\x01 \x01(\x02:\x03\x30.5')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'object_detection.protos.region_similarity_calculator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REGIONSIMILARITYCALCULATOR']._serialized_start=88
  _globals['_REGIONSIMILARITYCALCULATOR']._serialized_end=438
  _globals['_NEGSQDISTSIMILARITY']._serialized_start=440
  _globals['_NEGSQDISTSIMILARITY']._serialized_end=461
  _globals['_IOUSIMILARITY']._serialized_start=463
  _globals['_IOUSIMILARITY']._serialized_end=478
  _globals['_IOASIMILARITY']._serialized_start=480
  _globals['_IOASIMILARITY']._serialized_end=495
  _globals['_THRESHOLDEDIOUSIMILARITY']._serialized_start=497
  _globals['_THRESHOLDEDIOUSIMILARITY']._serialized_end=551
# @@protoc_insertion_point(module_scope)
