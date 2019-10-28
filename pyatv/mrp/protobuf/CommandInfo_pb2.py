# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/CommandInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/CommandInfo.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n$pyatv/mrp/protobuf/CommandInfo.proto\"\x8e\x04\n\x0b\x43ommandInfo\x12\x19\n\x07\x63ommand\x18\x01 \x01(\x0e\x32\x08.Command\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x0e\n\x06\x61\x63tive\x18\x03 \x01(\x08\x12\x1a\n\x12preferredIntervals\x18\x04 \x03(\x01\x12\x16\n\x0elocalizedTitle\x18\x05 \x01(\t\x12\x15\n\rminimumRating\x18\x06 \x01(\x02\x12\x15\n\rmaximumRating\x18\x07 \x01(\x02\x12\x16\n\x0esupportedRates\x18\x08 \x03(\x02\x12\x1b\n\x13localizedShortTitle\x18\t \x01(\t\x12\x12\n\nrepeatMode\x18\n \x01(\x05\x12\x13\n\x0bshuffleMode\x18\x0b \x01(\x05\x12\x19\n\x11presentationStyle\x18\x0c \x01(\x05\x12\x14\n\x0cskipInterval\x18\r \x01(\x05\x12\x19\n\x11numAvailableSkips\x18\x0e \x01(\x05\x12\x15\n\rskipFrequency\x18\x0f \x01(\x05\x12\x10\n\x08\x63\x61nScrub\x18\x10 \x01(\x05\x12#\n\x1bsupportedPlaybackQueueTypes\x18\x11 \x03(\x05\x12\'\n\x1fsupportedCustomQueueIdentifiers\x18\x12 \x03(\t\x12#\n\x1bsupportedInsertionPositions\x18\x13 \x03(\x05\x12\x1b\n\x13supportsSharedQueue\x18\x14 \x01(\x08*\x8b\x08\n\x07\x43ommand\x12\x0b\n\x07Unknown\x10\x00\x12\x08\n\x04Play\x10\x01\x12\t\n\x05Pause\x10\x02\x12\x13\n\x0fTogglePlayPause\x10\x03\x12\x08\n\x04Stop\x10\x04\x12\r\n\tNextTrack\x10\x05\x12\x11\n\rPreviousTrack\x10\x06\x12\x16\n\x12\x41\x64vanceShuffleMode\x10\x07\x12\x15\n\x11\x41\x64vanceRepeatMode\x10\x08\x12\x14\n\x10\x42\x65ginFastForward\x10\t\x12\x12\n\x0e\x45ndFastForward\x10\n\x12\x0f\n\x0b\x42\x65ginRewind\x10\x0b\x12\r\n\tEndRewind\x10\x0c\x12\x13\n\x0fRewind15Seconds\x10\r\x12\x18\n\x14\x46\x61stForward15Seconds\x10\x0e\x12\x13\n\x0fRewind30Seconds\x10\x0f\x12\x18\n\x14\x46\x61stForward30Seconds\x10\x10\x12\x0f\n\x0bSkipForward\x10\x12\x12\x10\n\x0cSkipBackward\x10\x13\x12\x16\n\x12\x43hangePlaybackRate\x10\x14\x12\r\n\tRateTrack\x10\x15\x12\r\n\tLikeTrack\x10\x16\x12\x10\n\x0c\x44islikeTrack\x10\x17\x12\x11\n\rBookmarkTrack\x10\x18\x12\x1a\n\x16SeekToPlaybackPosition\x10-\x12\x14\n\x10\x43hangeRepeatMode\x10.\x12\x15\n\x11\x43hangeShuffleMode\x10/\x12\x18\n\x14\x45nableLanguageOption\x10\x35\x12\x19\n\x15\x44isableLanguageOption\x10\x36\x12\x0f\n\x0bNextChapter\x10\x19\x12\x13\n\x0fPreviousChapter\x10\x1a\x12\r\n\tNextAlbum\x10\x1b\x12\x11\n\rPreviousAlbum\x10\x1c\x12\x10\n\x0cNextPlaylist\x10\x1d\x12\x14\n\x10PreviousPlaylist\x10\x1e\x12\x0c\n\x08\x42\x61nTrack\x10\x1f\x12\x16\n\x12\x41\x64\x64TrackToWishList\x10 \x12\x1b\n\x17RemoveTrackFromWishList\x10!\x12\x11\n\rNextInContext\x10\"\x12\x15\n\x11PreviousInContext\x10#\x12\x18\n\x14ResetPlaybackTimeout\x10)\x12\x14\n\x10SetPlaybackQueue\x10\x30\x12\x1e\n\x1a\x41\x64\x64NowPlayingItemToLibrary\x10\x31\x12\x16\n\x12\x43reateRadioStation\x10\x32\x12\x14\n\x10\x41\x64\x64ItemToLibrary\x10\x33\x12\x1b\n\x17InsertIntoPlaybackQueue\x10\x34\x12\x18\n\x14ReorderPlaybackQueue\x10\x37\x12\x1b\n\x17RemoveFromPlaybackQueue\x10\x38\x12\x1b\n\x17PlayItemInPlaybackQueue\x10\x39')
)

_COMMAND = _descriptor.EnumDescriptor(
  name='Command',
  full_name='Command',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Unknown', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Play', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Pause', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TogglePlayPause', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Stop', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NextTrack', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PreviousTrack', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AdvanceShuffleMode', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AdvanceRepeatMode', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BeginFastForward', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EndFastForward', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BeginRewind', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EndRewind', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Rewind15Seconds', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FastForward15Seconds', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Rewind30Seconds', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FastForward30Seconds', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SkipForward', index=17, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SkipBackward', index=18, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ChangePlaybackRate', index=19, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RateTrack', index=20, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LikeTrack', index=21, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DislikeTrack', index=22, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BookmarkTrack', index=23, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SeekToPlaybackPosition', index=24, number=45,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ChangeRepeatMode', index=25, number=46,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ChangeShuffleMode', index=26, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EnableLanguageOption', index=27, number=53,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DisableLanguageOption', index=28, number=54,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NextChapter', index=29, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PreviousChapter', index=30, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NextAlbum', index=31, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PreviousAlbum', index=32, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NextPlaylist', index=33, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PreviousPlaylist', index=34, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BanTrack', index=35, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AddTrackToWishList', index=36, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RemoveTrackFromWishList', index=37, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NextInContext', index=38, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PreviousInContext', index=39, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ResetPlaybackTimeout', index=40, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SetPlaybackQueue', index=41, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AddNowPlayingItemToLibrary', index=42, number=49,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CreateRadioStation', index=43, number=50,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AddItemToLibrary', index=44, number=51,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='InsertIntoPlaybackQueue', index=45, number=52,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ReorderPlaybackQueue', index=46, number=55,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RemoveFromPlaybackQueue', index=47, number=56,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PlayItemInPlaybackQueue', index=48, number=57,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=570,
  serialized_end=1605,
)
_sym_db.RegisterEnumDescriptor(_COMMAND)

Command = enum_type_wrapper.EnumTypeWrapper(_COMMAND)
Unknown = 0
Play = 1
Pause = 2
TogglePlayPause = 3
Stop = 4
NextTrack = 5
PreviousTrack = 6
AdvanceShuffleMode = 7
AdvanceRepeatMode = 8
BeginFastForward = 9
EndFastForward = 10
BeginRewind = 11
EndRewind = 12
Rewind15Seconds = 13
FastForward15Seconds = 14
Rewind30Seconds = 15
FastForward30Seconds = 16
SkipForward = 18
SkipBackward = 19
ChangePlaybackRate = 20
RateTrack = 21
LikeTrack = 22
DislikeTrack = 23
BookmarkTrack = 24
SeekToPlaybackPosition = 45
ChangeRepeatMode = 46
ChangeShuffleMode = 47
EnableLanguageOption = 53
DisableLanguageOption = 54
NextChapter = 25
PreviousChapter = 26
NextAlbum = 27
PreviousAlbum = 28
NextPlaylist = 29
PreviousPlaylist = 30
BanTrack = 31
AddTrackToWishList = 32
RemoveTrackFromWishList = 33
NextInContext = 34
PreviousInContext = 35
ResetPlaybackTimeout = 41
SetPlaybackQueue = 48
AddNowPlayingItemToLibrary = 49
CreateRadioStation = 50
AddItemToLibrary = 51
InsertIntoPlaybackQueue = 52
ReorderPlaybackQueue = 55
RemoveFromPlaybackQueue = 56
PlayItemInPlaybackQueue = 57



_COMMANDINFO = _descriptor.Descriptor(
  name='CommandInfo',
  full_name='CommandInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='CommandInfo.command', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='CommandInfo.enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active', full_name='CommandInfo.active', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preferredIntervals', full_name='CommandInfo.preferredIntervals', index=3,
      number=4, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='localizedTitle', full_name='CommandInfo.localizedTitle', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minimumRating', full_name='CommandInfo.minimumRating', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximumRating', full_name='CommandInfo.maximumRating', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supportedRates', full_name='CommandInfo.supportedRates', index=7,
      number=8, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='localizedShortTitle', full_name='CommandInfo.localizedShortTitle', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='repeatMode', full_name='CommandInfo.repeatMode', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shuffleMode', full_name='CommandInfo.shuffleMode', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='presentationStyle', full_name='CommandInfo.presentationStyle', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skipInterval', full_name='CommandInfo.skipInterval', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numAvailableSkips', full_name='CommandInfo.numAvailableSkips', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skipFrequency', full_name='CommandInfo.skipFrequency', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='canScrub', full_name='CommandInfo.canScrub', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supportedPlaybackQueueTypes', full_name='CommandInfo.supportedPlaybackQueueTypes', index=16,
      number=17, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supportedCustomQueueIdentifiers', full_name='CommandInfo.supportedCustomQueueIdentifiers', index=17,
      number=18, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supportedInsertionPositions', full_name='CommandInfo.supportedInsertionPositions', index=18,
      number=19, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supportsSharedQueue', full_name='CommandInfo.supportsSharedQueue', index=19,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=41,
  serialized_end=567,
)

_COMMANDINFO.fields_by_name['command'].enum_type = _COMMAND
DESCRIPTOR.message_types_by_name['CommandInfo'] = _COMMANDINFO
DESCRIPTOR.enum_types_by_name['Command'] = _COMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CommandInfo = _reflection.GeneratedProtocolMessageType('CommandInfo', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDINFO,
  '__module__' : 'pyatv.mrp.protobuf.CommandInfo_pb2'
  # @@protoc_insertion_point(class_scope:CommandInfo)
  })
_sym_db.RegisterMessage(CommandInfo)


# @@protoc_insertion_point(module_scope)