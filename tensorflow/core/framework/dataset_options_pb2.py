# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/framework/dataset_options.proto

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
  name='tensorflow/core/framework/dataset_options.proto',
  package='tensorflow.data',
  syntax='proto3',
  serialized_options=_b('ZVgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/dataset_options_go_proto'),
  serialized_pb=_b('\n/tensorflow/core/framework/dataset_options.proto\x12\x0ftensorflow.data\"\x92\x01\n\x0f\x41utotuneOptions\x12\x11\n\x07\x65nabled\x18\x01 \x01(\x08H\x00\x12\x14\n\ncpu_budget\x18\x02 \x01(\x05H\x01\x12\x14\n\nram_budget\x18\x03 \x01(\x03H\x02\x42\x12\n\x10optional_enabledB\x15\n\x13optional_cpu_budgetB\x15\n\x13optional_ram_budget\"\x7f\n\x11\x44istributeOptions\x12;\n\x11\x61uto_shard_policy\x18\x01 \x01(\x0e\x32 .tensorflow.data.AutoShardPolicy\x12\x15\n\x0bnum_devices\x18\x02 \x01(\x05H\x00\x42\x16\n\x14optional_num_devices\"\xf0\x04\n\x13OptimizationOptions\x12%\n\x1b\x61pply_default_optimizations\x18\x01 \x01(\x08H\x00\x12\x17\n\rfilter_fusion\x18\x06 \x01(\x08H\x01\x12\x1e\n\x14map_and_batch_fusion\x18\t \x01(\x08H\x02\x12\x1f\n\x15map_and_filter_fusion\x18\n \x01(\x08H\x03\x12\x14\n\nmap_fusion\x18\x0b \x01(\x08H\x04\x12\x1d\n\x13map_parallelization\x18\x0c \x01(\x08H\x05\x12\x1a\n\x10noop_elimination\x18\x0e \x01(\x08H\x06\x12\x18\n\x0eparallel_batch\x18\x0f \x01(\x08H\x07\x12#\n\x19shuffle_and_repeat_fusion\x18\x11 \x01(\x08H\x08\x42&\n$optional_apply_default_optimizationsB\x18\n\x16optional_filter_fusionB\x1f\n\x1doptional_map_and_batch_fusionB \n\x1eoptional_map_and_filter_fusionB\x15\n\x13optional_map_fusionB\x1e\n\x1coptional_map_parallelizationB\x1b\n\x19optional_noop_eliminationB\x19\n\x17optional_parallel_batchB$\n\"optional_shuffle_and_repeat_fusionJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x07\x10\x08J\x04\x08\x08\x10\tJ\x04\x08\r\x10\x0eJ\x04\x08\x10\x10\x11\"\xa2\x01\n\x10ThreadingOptions\x12\"\n\x18max_intra_op_parallelism\x18\x01 \x01(\x05H\x00\x12!\n\x17private_threadpool_size\x18\x02 \x01(\x05H\x01\x42#\n!optional_max_intra_op_parallelismB\"\n optional_private_threadpool_size\"\xc6\x03\n\x07Options\x12\x17\n\rdeterministic\x18\x01 \x01(\x08H\x00\x12:\n\x10\x61utotune_options\x18\x07 \x01(\x0b\x32 .tensorflow.data.AutotuneOptions\x12>\n\x12\x64istribute_options\x18\x02 \x01(\x0b\x32\".tensorflow.data.DistributeOptions\x12\x42\n\x14optimization_options\x18\x03 \x01(\x0b\x32$.tensorflow.data.OptimizationOptions\x12\x0f\n\x05slack\x18\x04 \x01(\x08H\x01\x12<\n\x11threading_options\x18\x05 \x01(\x0b\x32!.tensorflow.data.ThreadingOptions\x12\x45\n\x15\x65xternal_state_policy\x18\x06 \x01(\x0e\x32$.tensorflow.data.ExternalStatePolicyH\x02\x42\x18\n\x16optional_deterministicB\x10\n\x0eoptional_slackB \n\x1eoptional_external_state_policy*K\n\x0f\x41utoShardPolicy\x12\x08\n\x04\x41UTO\x10\x00\x12\x08\n\x04\x46ILE\x10\x01\x12\x08\n\x04\x44\x41TA\x10\x02\x12\x08\n\x04HINT\x10\x03\x12\x10\n\x03OFF\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*J\n\x13\x45xternalStatePolicy\x12\x0f\n\x0bPOLICY_WARN\x10\x00\x12\x11\n\rPOLICY_IGNORE\x10\x01\x12\x0f\n\x0bPOLICY_FAIL\x10\x02\x42XZVgithub.com/tensorflow/tensorflow/tensorflow/go/core/framework/dataset_options_go_protob\x06proto3')
)

_AUTOSHARDPOLICY = _descriptor.EnumDescriptor(
  name='AutoShardPolicy',
  full_name='tensorflow.data.AutoShardPolicy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HINT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFF', index=4, number=-1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1595,
  serialized_end=1670,
)
_sym_db.RegisterEnumDescriptor(_AUTOSHARDPOLICY)

AutoShardPolicy = enum_type_wrapper.EnumTypeWrapper(_AUTOSHARDPOLICY)
_EXTERNALSTATEPOLICY = _descriptor.EnumDescriptor(
  name='ExternalStatePolicy',
  full_name='tensorflow.data.ExternalStatePolicy',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POLICY_WARN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POLICY_IGNORE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POLICY_FAIL', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1672,
  serialized_end=1746,
)
_sym_db.RegisterEnumDescriptor(_EXTERNALSTATEPOLICY)

ExternalStatePolicy = enum_type_wrapper.EnumTypeWrapper(_EXTERNALSTATEPOLICY)
AUTO = 0
FILE = 1
DATA = 2
HINT = 3
OFF = -1
POLICY_WARN = 0
POLICY_IGNORE = 1
POLICY_FAIL = 2



_AUTOTUNEOPTIONS = _descriptor.Descriptor(
  name='AutotuneOptions',
  full_name='tensorflow.data.AutotuneOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='tensorflow.data.AutotuneOptions.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpu_budget', full_name='tensorflow.data.AutotuneOptions.cpu_budget', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ram_budget', full_name='tensorflow.data.AutotuneOptions.ram_budget', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='optional_enabled', full_name='tensorflow.data.AutotuneOptions.optional_enabled',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_cpu_budget', full_name='tensorflow.data.AutotuneOptions.optional_cpu_budget',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_ram_budget', full_name='tensorflow.data.AutotuneOptions.optional_ram_budget',
      index=2, containing_type=None, fields=[]),
  ],
  serialized_start=69,
  serialized_end=215,
)


_DISTRIBUTEOPTIONS = _descriptor.Descriptor(
  name='DistributeOptions',
  full_name='tensorflow.data.DistributeOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='auto_shard_policy', full_name='tensorflow.data.DistributeOptions.auto_shard_policy', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_devices', full_name='tensorflow.data.DistributeOptions.num_devices', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='optional_num_devices', full_name='tensorflow.data.DistributeOptions.optional_num_devices',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=217,
  serialized_end=344,
)


_OPTIMIZATIONOPTIONS = _descriptor.Descriptor(
  name='OptimizationOptions',
  full_name='tensorflow.data.OptimizationOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apply_default_optimizations', full_name='tensorflow.data.OptimizationOptions.apply_default_optimizations', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter_fusion', full_name='tensorflow.data.OptimizationOptions.filter_fusion', index=1,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_and_batch_fusion', full_name='tensorflow.data.OptimizationOptions.map_and_batch_fusion', index=2,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_and_filter_fusion', full_name='tensorflow.data.OptimizationOptions.map_and_filter_fusion', index=3,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_fusion', full_name='tensorflow.data.OptimizationOptions.map_fusion', index=4,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_parallelization', full_name='tensorflow.data.OptimizationOptions.map_parallelization', index=5,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='noop_elimination', full_name='tensorflow.data.OptimizationOptions.noop_elimination', index=6,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parallel_batch', full_name='tensorflow.data.OptimizationOptions.parallel_batch', index=7,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shuffle_and_repeat_fusion', full_name='tensorflow.data.OptimizationOptions.shuffle_and_repeat_fusion', index=8,
      number=17, type=8, cpp_type=7, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='optional_apply_default_optimizations', full_name='tensorflow.data.OptimizationOptions.optional_apply_default_optimizations',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_filter_fusion', full_name='tensorflow.data.OptimizationOptions.optional_filter_fusion',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_map_and_batch_fusion', full_name='tensorflow.data.OptimizationOptions.optional_map_and_batch_fusion',
      index=2, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_map_and_filter_fusion', full_name='tensorflow.data.OptimizationOptions.optional_map_and_filter_fusion',
      index=3, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_map_fusion', full_name='tensorflow.data.OptimizationOptions.optional_map_fusion',
      index=4, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_map_parallelization', full_name='tensorflow.data.OptimizationOptions.optional_map_parallelization',
      index=5, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_noop_elimination', full_name='tensorflow.data.OptimizationOptions.optional_noop_elimination',
      index=6, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_parallel_batch', full_name='tensorflow.data.OptimizationOptions.optional_parallel_batch',
      index=7, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_shuffle_and_repeat_fusion', full_name='tensorflow.data.OptimizationOptions.optional_shuffle_and_repeat_fusion',
      index=8, containing_type=None, fields=[]),
  ],
  serialized_start=347,
  serialized_end=971,
)


_THREADINGOPTIONS = _descriptor.Descriptor(
  name='ThreadingOptions',
  full_name='tensorflow.data.ThreadingOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_intra_op_parallelism', full_name='tensorflow.data.ThreadingOptions.max_intra_op_parallelism', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private_threadpool_size', full_name='tensorflow.data.ThreadingOptions.private_threadpool_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='optional_max_intra_op_parallelism', full_name='tensorflow.data.ThreadingOptions.optional_max_intra_op_parallelism',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_private_threadpool_size', full_name='tensorflow.data.ThreadingOptions.optional_private_threadpool_size',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=974,
  serialized_end=1136,
)


_OPTIONS = _descriptor.Descriptor(
  name='Options',
  full_name='tensorflow.data.Options',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deterministic', full_name='tensorflow.data.Options.deterministic', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='autotune_options', full_name='tensorflow.data.Options.autotune_options', index=1,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distribute_options', full_name='tensorflow.data.Options.distribute_options', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='optimization_options', full_name='tensorflow.data.Options.optimization_options', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slack', full_name='tensorflow.data.Options.slack', index=4,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='threading_options', full_name='tensorflow.data.Options.threading_options', index=5,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external_state_policy', full_name='tensorflow.data.Options.external_state_policy', index=6,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='optional_deterministic', full_name='tensorflow.data.Options.optional_deterministic',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_slack', full_name='tensorflow.data.Options.optional_slack',
      index=1, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='optional_external_state_policy', full_name='tensorflow.data.Options.optional_external_state_policy',
      index=2, containing_type=None, fields=[]),
  ],
  serialized_start=1139,
  serialized_end=1593,
)

_AUTOTUNEOPTIONS.oneofs_by_name['optional_enabled'].fields.append(
  _AUTOTUNEOPTIONS.fields_by_name['enabled'])
_AUTOTUNEOPTIONS.fields_by_name['enabled'].containing_oneof = _AUTOTUNEOPTIONS.oneofs_by_name['optional_enabled']
_AUTOTUNEOPTIONS.oneofs_by_name['optional_cpu_budget'].fields.append(
  _AUTOTUNEOPTIONS.fields_by_name['cpu_budget'])
_AUTOTUNEOPTIONS.fields_by_name['cpu_budget'].containing_oneof = _AUTOTUNEOPTIONS.oneofs_by_name['optional_cpu_budget']
_AUTOTUNEOPTIONS.oneofs_by_name['optional_ram_budget'].fields.append(
  _AUTOTUNEOPTIONS.fields_by_name['ram_budget'])
_AUTOTUNEOPTIONS.fields_by_name['ram_budget'].containing_oneof = _AUTOTUNEOPTIONS.oneofs_by_name['optional_ram_budget']
_DISTRIBUTEOPTIONS.fields_by_name['auto_shard_policy'].enum_type = _AUTOSHARDPOLICY
_DISTRIBUTEOPTIONS.oneofs_by_name['optional_num_devices'].fields.append(
  _DISTRIBUTEOPTIONS.fields_by_name['num_devices'])
_DISTRIBUTEOPTIONS.fields_by_name['num_devices'].containing_oneof = _DISTRIBUTEOPTIONS.oneofs_by_name['optional_num_devices']
_OPTIMIZATIONOPTIONS.oneofs_by_name['optional_apply_default_optimizations'].fields.append(
  _OPTIMIZATIONOPTIONS.fields_by_name['apply_default_optimizations'])
_OPTIMIZATIONOPTIONS.fields_by_name['apply_default_optimizations'].containing_oneof = _OPTIMIZATIONOPTIONS.oneofs_by_name['optional_apply_default_optimizations']
_OPTIMIZATIONOPTIONS.oneofs_by_name['optional_filter_fusion'].fields.append(
  _OPTIMIZATIONOPTIONS.fields_by_name['filter_fusion'])
_OPTIMIZATIONOPTIONS.fields_by_name['filter_fusion'].containing_oneof = _OPTIMIZATIONOPTIONS.oneofs_by_name['optional_filter_fusion']
_OPTIMIZATIONOPTIONS.oneofs_by_name['optional_map_and_batch_fusion'].fields.append(
  _OPTIMIZATIONOPTIONS.fields_by_name['map_and_batch_fusion'])
_OPTIMIZATIONOPTIONS.fields_by_name['map_and_batch_fusion'].containing_oneof = _OPTIMIZATIONOPTIONS.oneofs_by_name['optional_map_and_batch_fusion']
_OPTIMIZATIONOPTIONS.oneofs_by_name['optional_map_and_filter_fusion'].fields.append(
  _OPTIMIZATIONOPTIONS.fields_by_name['map_and_filter_fusion'])
_OPTIMIZATIONOPTIONS.fields_by_name['map_and_filter_fusion'].containing_oneof = _OPTIMIZATIONOPTIONS.oneofs_by_name['optional_map_and_filter_fusion']
_OPTIMIZATIONOPTIONS.oneofs_by_name['optional_map_fusion'].fields.append(
  _OPTIMIZATIONOPTIONS.fields_by_name['map_fusion'])
_OPTIMIZATIONOPTIONS.fields_by_name['map_fusion'].containing_oneof = _OPTIMIZATIONOPTIONS.oneofs_by_name['optional_map_fusion']
_OPTIMIZATIONOPTIONS.oneofs_by_name['optional_map_parallelization'].fields.append(
  _OPTIMIZATIONOPTIONS.fields_by_name['map_parallelization'])
_OPTIMIZATIONOPTIONS.fields_by_name['map_parallelization'].containing_oneof = _OPTIMIZATIONOPTIONS.oneofs_by_name['optional_map_parallelization']
_OPTIMIZATIONOPTIONS.oneofs_by_name['optional_noop_elimination'].fields.append(
  _OPTIMIZATIONOPTIONS.fields_by_name['noop_elimination'])
_OPTIMIZATIONOPTIONS.fields_by_name['noop_elimination'].containing_oneof = _OPTIMIZATIONOPTIONS.oneofs_by_name['optional_noop_elimination']
_OPTIMIZATIONOPTIONS.oneofs_by_name['optional_parallel_batch'].fields.append(
  _OPTIMIZATIONOPTIONS.fields_by_name['parallel_batch'])
_OPTIMIZATIONOPTIONS.fields_by_name['parallel_batch'].containing_oneof = _OPTIMIZATIONOPTIONS.oneofs_by_name['optional_parallel_batch']
_OPTIMIZATIONOPTIONS.oneofs_by_name['optional_shuffle_and_repeat_fusion'].fields.append(
  _OPTIMIZATIONOPTIONS.fields_by_name['shuffle_and_repeat_fusion'])
_OPTIMIZATIONOPTIONS.fields_by_name['shuffle_and_repeat_fusion'].containing_oneof = _OPTIMIZATIONOPTIONS.oneofs_by_name['optional_shuffle_and_repeat_fusion']
_THREADINGOPTIONS.oneofs_by_name['optional_max_intra_op_parallelism'].fields.append(
  _THREADINGOPTIONS.fields_by_name['max_intra_op_parallelism'])
_THREADINGOPTIONS.fields_by_name['max_intra_op_parallelism'].containing_oneof = _THREADINGOPTIONS.oneofs_by_name['optional_max_intra_op_parallelism']
_THREADINGOPTIONS.oneofs_by_name['optional_private_threadpool_size'].fields.append(
  _THREADINGOPTIONS.fields_by_name['private_threadpool_size'])
_THREADINGOPTIONS.fields_by_name['private_threadpool_size'].containing_oneof = _THREADINGOPTIONS.oneofs_by_name['optional_private_threadpool_size']
_OPTIONS.fields_by_name['autotune_options'].message_type = _AUTOTUNEOPTIONS
_OPTIONS.fields_by_name['distribute_options'].message_type = _DISTRIBUTEOPTIONS
_OPTIONS.fields_by_name['optimization_options'].message_type = _OPTIMIZATIONOPTIONS
_OPTIONS.fields_by_name['threading_options'].message_type = _THREADINGOPTIONS
_OPTIONS.fields_by_name['external_state_policy'].enum_type = _EXTERNALSTATEPOLICY
_OPTIONS.oneofs_by_name['optional_deterministic'].fields.append(
  _OPTIONS.fields_by_name['deterministic'])
_OPTIONS.fields_by_name['deterministic'].containing_oneof = _OPTIONS.oneofs_by_name['optional_deterministic']
_OPTIONS.oneofs_by_name['optional_slack'].fields.append(
  _OPTIONS.fields_by_name['slack'])
_OPTIONS.fields_by_name['slack'].containing_oneof = _OPTIONS.oneofs_by_name['optional_slack']
_OPTIONS.oneofs_by_name['optional_external_state_policy'].fields.append(
  _OPTIONS.fields_by_name['external_state_policy'])
_OPTIONS.fields_by_name['external_state_policy'].containing_oneof = _OPTIONS.oneofs_by_name['optional_external_state_policy']
DESCRIPTOR.message_types_by_name['AutotuneOptions'] = _AUTOTUNEOPTIONS
DESCRIPTOR.message_types_by_name['DistributeOptions'] = _DISTRIBUTEOPTIONS
DESCRIPTOR.message_types_by_name['OptimizationOptions'] = _OPTIMIZATIONOPTIONS
DESCRIPTOR.message_types_by_name['ThreadingOptions'] = _THREADINGOPTIONS
DESCRIPTOR.message_types_by_name['Options'] = _OPTIONS
DESCRIPTOR.enum_types_by_name['AutoShardPolicy'] = _AUTOSHARDPOLICY
DESCRIPTOR.enum_types_by_name['ExternalStatePolicy'] = _EXTERNALSTATEPOLICY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AutotuneOptions = _reflection.GeneratedProtocolMessageType('AutotuneOptions', (_message.Message,), {
  'DESCRIPTOR' : _AUTOTUNEOPTIONS,
  '__module__' : 'tensorflow.core.framework.dataset_options_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.AutotuneOptions)
  })
_sym_db.RegisterMessage(AutotuneOptions)

DistributeOptions = _reflection.GeneratedProtocolMessageType('DistributeOptions', (_message.Message,), {
  'DESCRIPTOR' : _DISTRIBUTEOPTIONS,
  '__module__' : 'tensorflow.core.framework.dataset_options_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.DistributeOptions)
  })
_sym_db.RegisterMessage(DistributeOptions)

OptimizationOptions = _reflection.GeneratedProtocolMessageType('OptimizationOptions', (_message.Message,), {
  'DESCRIPTOR' : _OPTIMIZATIONOPTIONS,
  '__module__' : 'tensorflow.core.framework.dataset_options_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.OptimizationOptions)
  })
_sym_db.RegisterMessage(OptimizationOptions)

ThreadingOptions = _reflection.GeneratedProtocolMessageType('ThreadingOptions', (_message.Message,), {
  'DESCRIPTOR' : _THREADINGOPTIONS,
  '__module__' : 'tensorflow.core.framework.dataset_options_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.ThreadingOptions)
  })
_sym_db.RegisterMessage(ThreadingOptions)

Options = _reflection.GeneratedProtocolMessageType('Options', (_message.Message,), {
  'DESCRIPTOR' : _OPTIONS,
  '__module__' : 'tensorflow.core.framework.dataset_options_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.data.Options)
  })
_sym_db.RegisterMessage(Options)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
