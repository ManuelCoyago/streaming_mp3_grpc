# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: audio.proto
# Protobuf Python Version: 5.29.0
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
    0,
    '',
    'audio.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61udio.proto\x12\x05\x61udio\"\x07\n\x05\x45mpty\"\x19\n\x08\x46ileList\x12\r\n\x05\x66iles\x18\x01 \x03(\t\" \n\x0c\x41udioRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"\x1a\n\nAudioChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"U\n\x08Metadata\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x10\n\x08\x64uration\x18\x02 \x01(\x02\x12\x13\n\x0bsample_rate\x18\x03 \x01(\x05\x12\x10\n\x08\x63hannels\x18\x04 \x01(\x05\x32\xa8\x01\n\x0c\x41udioService\x12*\n\tListFiles\x12\x0c.audio.Empty\x1a\x0f.audio.FileList\x12\x37\n\x0bStreamAudio\x12\x13.audio.AudioRequest\x1a\x11.audio.AudioChunk0\x01\x12\x33\n\x0bGetMetadata\x12\x13.audio.AudioRequest\x1a\x0f.audio.Metadatab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'audio_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=22
  _globals['_EMPTY']._serialized_end=29
  _globals['_FILELIST']._serialized_start=31
  _globals['_FILELIST']._serialized_end=56
  _globals['_AUDIOREQUEST']._serialized_start=58
  _globals['_AUDIOREQUEST']._serialized_end=90
  _globals['_AUDIOCHUNK']._serialized_start=92
  _globals['_AUDIOCHUNK']._serialized_end=118
  _globals['_METADATA']._serialized_start=120
  _globals['_METADATA']._serialized_end=205
  _globals['_AUDIOSERVICE']._serialized_start=208
  _globals['_AUDIOSERVICE']._serialized_end=376
# @@protoc_insertion_point(module_scope)
