// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: tensorflow/core/protobuf/data_service.proto

#ifndef GOOGLE_PROTOBUF_INCLUDED_tensorflow_2fcore_2fprotobuf_2fdata_5fservice_2eproto
#define GOOGLE_PROTOBUF_INCLUDED_tensorflow_2fcore_2fprotobuf_2fdata_5fservice_2eproto

#include <limits>
#include <string>

#include <google/protobuf/port_def.inc>
#if PROTOBUF_VERSION < 3009000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers. Please update
#error your headers.
#endif
#if 3009002 < PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers. Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/port_undef.inc>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/arena.h>
#include <google/protobuf/arenastring.h>
#include <google/protobuf/generated_message_table_driven.h>
#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/inlined_string_field.h>
#include <google/protobuf/metadata.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>  // IWYU pragma: export
#include <google/protobuf/extension_set.h>  // IWYU pragma: export
#include <google/protobuf/generated_enum_reflection.h>
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)
#include <google/protobuf/port_def.inc>
#define PROTOBUF_INTERNAL_EXPORT_tensorflow_2fcore_2fprotobuf_2fdata_5fservice_2eproto
PROTOBUF_NAMESPACE_OPEN
namespace internal {
class AnyMetadata;
}  // namespace internal
PROTOBUF_NAMESPACE_CLOSE

// Internal implementation detail -- do not use these members.
struct TableStruct_tensorflow_2fcore_2fprotobuf_2fdata_5fservice_2eproto {
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTableField entries[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::AuxillaryParseTableField aux[]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::ParseTable schema[1]
    PROTOBUF_SECTION_VARIABLE(protodesc_cold);
  static const ::PROTOBUF_NAMESPACE_ID::internal::FieldMetadata field_metadata[];
  static const ::PROTOBUF_NAMESPACE_ID::internal::SerializationTable serialization_table[];
  static const ::PROTOBUF_NAMESPACE_ID::uint32 offsets[];
};
extern const ::PROTOBUF_NAMESPACE_ID::internal::DescriptorTable descriptor_table_tensorflow_2fcore_2fprotobuf_2fdata_5fservice_2eproto;
namespace tensorflow {
namespace data {
class ProcessingModeDef;
class ProcessingModeDefDefaultTypeInternal;
extern ProcessingModeDefDefaultTypeInternal _ProcessingModeDef_default_instance_;
}  // namespace data
}  // namespace tensorflow
PROTOBUF_NAMESPACE_OPEN
template<> ::tensorflow::data::ProcessingModeDef* Arena::CreateMaybeMessage<::tensorflow::data::ProcessingModeDef>(Arena*);
PROTOBUF_NAMESPACE_CLOSE
namespace tensorflow {
namespace data {

enum ProcessingModeDef_ShardingPolicy : int {
  ProcessingModeDef_ShardingPolicy_OFF = 0,
  ProcessingModeDef_ShardingPolicy_DYNAMIC = 1,
  ProcessingModeDef_ShardingPolicy_FILE = 2,
  ProcessingModeDef_ShardingPolicy_DATA = 3,
  ProcessingModeDef_ShardingPolicy_FILE_OR_DATA = 4,
  ProcessingModeDef_ShardingPolicy_HINT = 5,
  ProcessingModeDef_ShardingPolicy_ProcessingModeDef_ShardingPolicy_INT_MIN_SENTINEL_DO_NOT_USE_ = std::numeric_limits<::PROTOBUF_NAMESPACE_ID::int32>::min(),
  ProcessingModeDef_ShardingPolicy_ProcessingModeDef_ShardingPolicy_INT_MAX_SENTINEL_DO_NOT_USE_ = std::numeric_limits<::PROTOBUF_NAMESPACE_ID::int32>::max()
};
bool ProcessingModeDef_ShardingPolicy_IsValid(int value);
constexpr ProcessingModeDef_ShardingPolicy ProcessingModeDef_ShardingPolicy_ShardingPolicy_MIN = ProcessingModeDef_ShardingPolicy_OFF;
constexpr ProcessingModeDef_ShardingPolicy ProcessingModeDef_ShardingPolicy_ShardingPolicy_MAX = ProcessingModeDef_ShardingPolicy_HINT;
constexpr int ProcessingModeDef_ShardingPolicy_ShardingPolicy_ARRAYSIZE = ProcessingModeDef_ShardingPolicy_ShardingPolicy_MAX + 1;

const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor* ProcessingModeDef_ShardingPolicy_descriptor();
template<typename T>
inline const std::string& ProcessingModeDef_ShardingPolicy_Name(T enum_t_value) {
  static_assert(::std::is_same<T, ProcessingModeDef_ShardingPolicy>::value ||
    ::std::is_integral<T>::value,
    "Incorrect type passed to function ProcessingModeDef_ShardingPolicy_Name.");
  return ::PROTOBUF_NAMESPACE_ID::internal::NameOfEnum(
    ProcessingModeDef_ShardingPolicy_descriptor(), enum_t_value);
}
inline bool ProcessingModeDef_ShardingPolicy_Parse(
    const std::string& name, ProcessingModeDef_ShardingPolicy* value) {
  return ::PROTOBUF_NAMESPACE_ID::internal::ParseNamedEnum<ProcessingModeDef_ShardingPolicy>(
    ProcessingModeDef_ShardingPolicy_descriptor(), name, value);
}
// ===================================================================

class ProcessingModeDef :
    public ::PROTOBUF_NAMESPACE_ID::Message /* @@protoc_insertion_point(class_definition:tensorflow.data.ProcessingModeDef) */ {
 public:
  ProcessingModeDef();
  virtual ~ProcessingModeDef();

  ProcessingModeDef(const ProcessingModeDef& from);
  ProcessingModeDef(ProcessingModeDef&& from) noexcept
    : ProcessingModeDef() {
    *this = ::std::move(from);
  }

  inline ProcessingModeDef& operator=(const ProcessingModeDef& from) {
    CopyFrom(from);
    return *this;
  }
  inline ProcessingModeDef& operator=(ProcessingModeDef&& from) noexcept {
    if (GetArenaNoVirtual() == from.GetArenaNoVirtual()) {
      if (this != &from) InternalSwap(&from);
    } else {
      CopyFrom(from);
    }
    return *this;
  }

  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* descriptor() {
    return GetDescriptor();
  }
  static const ::PROTOBUF_NAMESPACE_ID::Descriptor* GetDescriptor() {
    return GetMetadataStatic().descriptor;
  }
  static const ::PROTOBUF_NAMESPACE_ID::Reflection* GetReflection() {
    return GetMetadataStatic().reflection;
  }
  static const ProcessingModeDef& default_instance();

  static void InitAsDefaultInstance();  // FOR INTERNAL USE ONLY
  static inline const ProcessingModeDef* internal_default_instance() {
    return reinterpret_cast<const ProcessingModeDef*>(
               &_ProcessingModeDef_default_instance_);
  }
  static constexpr int kIndexInFileMessages =
    0;

  friend void swap(ProcessingModeDef& a, ProcessingModeDef& b) {
    a.Swap(&b);
  }
  inline void Swap(ProcessingModeDef* other) {
    if (other == this) return;
    InternalSwap(other);
  }

  // implements Message ----------------------------------------------

  inline ProcessingModeDef* New() const final {
    return CreateMaybeMessage<ProcessingModeDef>(nullptr);
  }

  ProcessingModeDef* New(::PROTOBUF_NAMESPACE_ID::Arena* arena) const final {
    return CreateMaybeMessage<ProcessingModeDef>(arena);
  }
  void CopyFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void MergeFrom(const ::PROTOBUF_NAMESPACE_ID::Message& from) final;
  void CopyFrom(const ProcessingModeDef& from);
  void MergeFrom(const ProcessingModeDef& from);
  PROTOBUF_ATTRIBUTE_REINITIALIZES void Clear() final;
  bool IsInitialized() const final;

  size_t ByteSizeLong() const final;
  #if GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  const char* _InternalParse(const char* ptr, ::PROTOBUF_NAMESPACE_ID::internal::ParseContext* ctx) final;
  #else
  bool MergePartialFromCodedStream(
      ::PROTOBUF_NAMESPACE_ID::io::CodedInputStream* input) final;
  #endif  // GOOGLE_PROTOBUF_ENABLE_EXPERIMENTAL_PARSER
  void SerializeWithCachedSizes(
      ::PROTOBUF_NAMESPACE_ID::io::CodedOutputStream* output) const final;
  ::PROTOBUF_NAMESPACE_ID::uint8* InternalSerializeWithCachedSizesToArray(
      ::PROTOBUF_NAMESPACE_ID::uint8* target) const final;
  int GetCachedSize() const final { return _cached_size_.Get(); }

  private:
  inline void SharedCtor();
  inline void SharedDtor();
  void SetCachedSize(int size) const final;
  void InternalSwap(ProcessingModeDef* other);
  friend class ::PROTOBUF_NAMESPACE_ID::internal::AnyMetadata;
  static ::PROTOBUF_NAMESPACE_ID::StringPiece FullMessageName() {
    return "tensorflow.data.ProcessingModeDef";
  }
  private:
  inline ::PROTOBUF_NAMESPACE_ID::Arena* GetArenaNoVirtual() const {
    return nullptr;
  }
  inline void* MaybeArenaPtr() const {
    return nullptr;
  }
  public:

  ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadata() const final;
  private:
  static ::PROTOBUF_NAMESPACE_ID::Metadata GetMetadataStatic() {
    ::PROTOBUF_NAMESPACE_ID::internal::AssignDescriptors(&::descriptor_table_tensorflow_2fcore_2fprotobuf_2fdata_5fservice_2eproto);
    return ::descriptor_table_tensorflow_2fcore_2fprotobuf_2fdata_5fservice_2eproto.file_level_metadata[kIndexInFileMessages];
  }

  public:

  // nested types ----------------------------------------------------

  typedef ProcessingModeDef_ShardingPolicy ShardingPolicy;
  static constexpr ShardingPolicy OFF =
    ProcessingModeDef_ShardingPolicy_OFF;
  static constexpr ShardingPolicy DYNAMIC =
    ProcessingModeDef_ShardingPolicy_DYNAMIC;
  static constexpr ShardingPolicy FILE =
    ProcessingModeDef_ShardingPolicy_FILE;
  static constexpr ShardingPolicy DATA =
    ProcessingModeDef_ShardingPolicy_DATA;
  static constexpr ShardingPolicy FILE_OR_DATA =
    ProcessingModeDef_ShardingPolicy_FILE_OR_DATA;
  static constexpr ShardingPolicy HINT =
    ProcessingModeDef_ShardingPolicy_HINT;
  static inline bool ShardingPolicy_IsValid(int value) {
    return ProcessingModeDef_ShardingPolicy_IsValid(value);
  }
  static constexpr ShardingPolicy ShardingPolicy_MIN =
    ProcessingModeDef_ShardingPolicy_ShardingPolicy_MIN;
  static constexpr ShardingPolicy ShardingPolicy_MAX =
    ProcessingModeDef_ShardingPolicy_ShardingPolicy_MAX;
  static constexpr int ShardingPolicy_ARRAYSIZE =
    ProcessingModeDef_ShardingPolicy_ShardingPolicy_ARRAYSIZE;
  static inline const ::PROTOBUF_NAMESPACE_ID::EnumDescriptor*
  ShardingPolicy_descriptor() {
    return ProcessingModeDef_ShardingPolicy_descriptor();
  }
  template<typename T>
  static inline const std::string& ShardingPolicy_Name(T enum_t_value) {
    static_assert(::std::is_same<T, ShardingPolicy>::value ||
      ::std::is_integral<T>::value,
      "Incorrect type passed to function ShardingPolicy_Name.");
    return ProcessingModeDef_ShardingPolicy_Name(enum_t_value);
  }
  static inline bool ShardingPolicy_Parse(const std::string& name,
      ShardingPolicy* value) {
    return ProcessingModeDef_ShardingPolicy_Parse(name, value);
  }

  // accessors -------------------------------------------------------

  enum : int {
    kShardingPolicyFieldNumber = 1,
  };
  // .tensorflow.data.ProcessingModeDef.ShardingPolicy sharding_policy = 1;
  void clear_sharding_policy();
  ::tensorflow::data::ProcessingModeDef_ShardingPolicy sharding_policy() const;
  void set_sharding_policy(::tensorflow::data::ProcessingModeDef_ShardingPolicy value);

  // @@protoc_insertion_point(class_scope:tensorflow.data.ProcessingModeDef)
 private:
  class _Internal;

  ::PROTOBUF_NAMESPACE_ID::internal::InternalMetadataWithArena _internal_metadata_;
  int sharding_policy_;
  mutable ::PROTOBUF_NAMESPACE_ID::internal::CachedSize _cached_size_;
  friend struct ::TableStruct_tensorflow_2fcore_2fprotobuf_2fdata_5fservice_2eproto;
};
// ===================================================================


// ===================================================================

#ifdef __GNUC__
  #pragma GCC diagnostic push
  #pragma GCC diagnostic ignored "-Wstrict-aliasing"
#endif  // __GNUC__
// ProcessingModeDef

// .tensorflow.data.ProcessingModeDef.ShardingPolicy sharding_policy = 1;
inline void ProcessingModeDef::clear_sharding_policy() {
  sharding_policy_ = 0;
}
inline ::tensorflow::data::ProcessingModeDef_ShardingPolicy ProcessingModeDef::sharding_policy() const {
  // @@protoc_insertion_point(field_get:tensorflow.data.ProcessingModeDef.sharding_policy)
  return static_cast< ::tensorflow::data::ProcessingModeDef_ShardingPolicy >(sharding_policy_);
}
inline void ProcessingModeDef::set_sharding_policy(::tensorflow::data::ProcessingModeDef_ShardingPolicy value) {
  
  sharding_policy_ = value;
  // @@protoc_insertion_point(field_set:tensorflow.data.ProcessingModeDef.sharding_policy)
}

#ifdef __GNUC__
  #pragma GCC diagnostic pop
#endif  // __GNUC__

// @@protoc_insertion_point(namespace_scope)

}  // namespace data
}  // namespace tensorflow

PROTOBUF_NAMESPACE_OPEN

template <> struct is_proto_enum< ::tensorflow::data::ProcessingModeDef_ShardingPolicy> : ::std::true_type {};
template <>
inline const EnumDescriptor* GetEnumDescriptor< ::tensorflow::data::ProcessingModeDef_ShardingPolicy>() {
  return ::tensorflow::data::ProcessingModeDef_ShardingPolicy_descriptor();
}

PROTOBUF_NAMESPACE_CLOSE

// @@protoc_insertion_point(global_scope)

#include <google/protobuf/port_undef.inc>
#endif  // GOOGLE_PROTOBUF_INCLUDED_GOOGLE_PROTOBUF_INCLUDED_tensorflow_2fcore_2fprotobuf_2fdata_5fservice_2eproto
