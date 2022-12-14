/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* TypeDef Definitions                                                        *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

#ifdef GET_TYPEDEF_LIST
#undef GET_TYPEDEF_LIST

::mlir::BFloat16Type,
::mlir::ComplexType,
::mlir::Float128Type,
::mlir::Float16Type,
::mlir::Float32Type,
::mlir::Float64Type,
::mlir::Float80Type,
::mlir::FunctionType,
::mlir::IndexType,
::mlir::IntegerType,
::mlir::MemRefType,
::mlir::NoneType,
::mlir::OpaqueType,
::mlir::RankedTensorType,
::mlir::TupleType,
::mlir::UnrankedMemRefType,
::mlir::UnrankedTensorType,
::mlir::VectorType

#endif  // GET_TYPEDEF_LIST

#ifdef GET_TYPEDEF_CLASSES
#undef GET_TYPEDEF_CLASSES

namespace mlir {
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::BFloat16Type)
namespace mlir {

namespace detail {
  struct ComplexTypeStorage : public ::mlir::TypeStorage {
    ComplexTypeStorage (Type elementType)
      : elementType(elementType) { }

    /// The hash key is a tuple of the parameter types.
    using KeyTy = std::tuple<Type>;
  bool operator==(const KeyTy &tblgenKey) const {
    if (!(elementType == std::get<0>(tblgenKey)))
      return false;
    return true;
  }
  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
      return ::llvm::hash_combine(std::get<0>(tblgenKey));
    }

    /// Define a construction method for creating a new instance of this
    /// storage.
    static ComplexTypeStorage *construct(::mlir::TypeStorageAllocator &allocator,
                          const KeyTy &tblgenKey) {
      auto elementType = std::get<0>(tblgenKey);

      return new (allocator.allocate<ComplexTypeStorage>())
          ComplexTypeStorage(elementType);
    }
      Type elementType;
  };
} // namespace detail
ComplexType ComplexType::get(Type elementType) {
  
      return Base::get(elementType.getContext(), elementType);
    ;
}
ComplexType ComplexType::getChecked(llvm::function_ref<::mlir::InFlightDiagnostic()> emitErrorFn, Type elementType) {
  
      return Base::getChecked(emitErrorFn, elementType.getContext(), elementType);
    ;
}
Type ComplexType::getElementType() const { return getImpl()->elementType; }
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::ComplexType)
namespace mlir {
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::Float128Type)
namespace mlir {
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::Float16Type)
namespace mlir {
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::Float32Type)
namespace mlir {
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::Float64Type)
namespace mlir {
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::Float80Type)
namespace mlir {
FunctionType FunctionType::get(::mlir::MLIRContext *context, TypeRange inputs, TypeRange results) {
  
      return Base::get(context, inputs, results);
    ;
}
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::FunctionType)
namespace mlir {
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::IndexType)
namespace mlir {
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::IntegerType)
namespace mlir {

namespace detail {
  struct MemRefTypeStorage : public ::mlir::TypeStorage {
    MemRefTypeStorage (::llvm::ArrayRef<int64_t> shape, Type elementType, ::llvm::ArrayRef<AffineMap> affineMaps, Attribute memorySpace)
      : shape(shape), elementType(elementType), affineMaps(affineMaps), memorySpace(memorySpace) { }

    /// The hash key is a tuple of the parameter types.
    using KeyTy = std::tuple<::llvm::ArrayRef<int64_t>, Type, ::llvm::ArrayRef<AffineMap>, Attribute>;
  bool operator==(const KeyTy &tblgenKey) const {
    if (!(shape == std::get<0>(tblgenKey)))
      return false;
    if (!(elementType == std::get<1>(tblgenKey)))
      return false;
    if (!(affineMaps == std::get<2>(tblgenKey)))
      return false;
    if (!(memorySpace == std::get<3>(tblgenKey)))
      return false;
    return true;
  }
  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
      return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey), std::get<3>(tblgenKey));
    }

    /// Define a construction method for creating a new instance of this
    /// storage.
    static MemRefTypeStorage *construct(::mlir::TypeStorageAllocator &allocator,
                          const KeyTy &tblgenKey) {
      auto shape = std::get<0>(tblgenKey);
      auto elementType = std::get<1>(tblgenKey);
      auto affineMaps = std::get<2>(tblgenKey);
      auto memorySpace = std::get<3>(tblgenKey);
      shape = allocator.copyInto(shape);
      affineMaps = allocator.copyInto(affineMaps);

      return new (allocator.allocate<MemRefTypeStorage>())
          MemRefTypeStorage(shape, elementType, affineMaps, memorySpace);
    }
      ::llvm::ArrayRef<int64_t> shape;
      Type elementType;
      ::llvm::ArrayRef<AffineMap> affineMaps;
      Attribute memorySpace;
  };
} // namespace detail
MemRefType MemRefType::get(ArrayRef<int64_t> shape, Type elementType, ArrayRef<AffineMap> affineMaps, Attribute memorySpace) {
  
      // Drop identity maps from the composition. This may lead to the
      // composition becoming empty, which is interpreted as an implicit
      // identity.
      auto nonIdentityMaps = llvm::make_filter_range(affineMaps,
        [](AffineMap map) { return !map.isIdentity(); });
      // Drop default memory space value and replace it with empty attribute.
      Attribute nonDefaultMemorySpace = skipDefaultMemorySpace(memorySpace);
      return Base::get(elementType.getContext(), shape, elementType,
                   llvm::to_vector<4>(nonIdentityMaps), nonDefaultMemorySpace);
    ;
}
MemRefType MemRefType::getChecked(llvm::function_ref<::mlir::InFlightDiagnostic()> emitErrorFn, ArrayRef<int64_t> shape, Type elementType, ArrayRef<AffineMap> affineMaps, Attribute memorySpace) {
  
      // Drop identity maps from the composition. This may lead to the
      // composition becoming empty, which is interpreted as an implicit
      // identity.
      auto nonIdentityMaps = llvm::make_filter_range(affineMaps,
        [](AffineMap map) { return !map.isIdentity(); });
      // Drop default memory space value and replace it with empty attribute.
      Attribute nonDefaultMemorySpace = skipDefaultMemorySpace(memorySpace);
      return Base::getChecked(emitErrorFn, elementType.getContext(), shape, elementType,
                   llvm::to_vector<4>(nonIdentityMaps), nonDefaultMemorySpace);
    ;
}
MemRefType MemRefType::get(ArrayRef<int64_t> shape, Type elementType, ArrayRef<AffineMap> affineMaps, unsigned memorySpace) {
  
      // Convert deprecated integer-like memory space to Attribute.
      Attribute memorySpaceAttr =
          wrapIntegerMemorySpace(memorySpace, elementType.getContext());
      return MemRefType::get(shape, elementType, affineMaps, memorySpaceAttr);
    ;
}
MemRefType MemRefType::getChecked(llvm::function_ref<::mlir::InFlightDiagnostic()> emitErrorFn, ArrayRef<int64_t> shape, Type elementType, ArrayRef<AffineMap> affineMaps, unsigned memorySpace) {
  
      // Convert deprecated integer-like memory space to Attribute.
      Attribute memorySpaceAttr =
          wrapIntegerMemorySpace(memorySpace, elementType.getContext());
      return MemRefType::get(shape, elementType, affineMaps, memorySpaceAttr);
    ;
}
::llvm::ArrayRef<int64_t> MemRefType::getShape() const { return getImpl()->shape; }
Type MemRefType::getElementType() const { return getImpl()->elementType; }
::llvm::ArrayRef<AffineMap> MemRefType::getAffineMaps() const { return getImpl()->affineMaps; }
Attribute MemRefType::getMemorySpace() const { return getImpl()->memorySpace; }
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::MemRefType)
namespace mlir {
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::NoneType)
namespace mlir {

namespace detail {
  struct OpaqueTypeStorage : public ::mlir::TypeStorage {
    OpaqueTypeStorage (Identifier dialectNamespace, ::llvm::StringRef typeData)
      : dialectNamespace(dialectNamespace), typeData(typeData) { }

    /// The hash key is a tuple of the parameter types.
    using KeyTy = std::tuple<Identifier, ::llvm::StringRef>;
  bool operator==(const KeyTy &tblgenKey) const {
    if (!(dialectNamespace == std::get<0>(tblgenKey)))
      return false;
    if (!(typeData == std::get<1>(tblgenKey)))
      return false;
    return true;
  }
  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
      return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey));
    }

    /// Define a construction method for creating a new instance of this
    /// storage.
    static OpaqueTypeStorage *construct(::mlir::TypeStorageAllocator &allocator,
                          const KeyTy &tblgenKey) {
      auto dialectNamespace = std::get<0>(tblgenKey);
      auto typeData = std::get<1>(tblgenKey);
      typeData = allocator.copyInto(typeData);

      return new (allocator.allocate<OpaqueTypeStorage>())
          OpaqueTypeStorage(dialectNamespace, typeData);
    }
      Identifier dialectNamespace;
      ::llvm::StringRef typeData;
  };
} // namespace detail
OpaqueType OpaqueType::get(Identifier dialectNamespace, StringRef typeData) {
  
      return Base::get(dialectNamespace.getContext(), dialectNamespace, typeData);
    ;
}
OpaqueType OpaqueType::getChecked(llvm::function_ref<::mlir::InFlightDiagnostic()> emitErrorFn, Identifier dialectNamespace, StringRef typeData) {
  
      return Base::getChecked(emitErrorFn, dialectNamespace.getContext(), dialectNamespace, typeData);
    ;
}
Identifier OpaqueType::getDialectNamespace() const { return getImpl()->dialectNamespace; }
::llvm::StringRef OpaqueType::getTypeData() const { return getImpl()->typeData; }
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::OpaqueType)
namespace mlir {

namespace detail {
  struct RankedTensorTypeStorage : public ::mlir::TypeStorage {
    RankedTensorTypeStorage (::llvm::ArrayRef<int64_t> shape, Type elementType, Attribute encoding)
      : shape(shape), elementType(elementType), encoding(encoding) { }

    /// The hash key is a tuple of the parameter types.
    using KeyTy = std::tuple<::llvm::ArrayRef<int64_t>, Type, Attribute>;
  bool operator==(const KeyTy &tblgenKey) const {
    if (!(shape == std::get<0>(tblgenKey)))
      return false;
    if (!(elementType == std::get<1>(tblgenKey)))
      return false;
    if (!(encoding == std::get<2>(tblgenKey)))
      return false;
    return true;
  }
  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
      return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey), std::get<2>(tblgenKey));
    }

    /// Define a construction method for creating a new instance of this
    /// storage.
    static RankedTensorTypeStorage *construct(::mlir::TypeStorageAllocator &allocator,
                          const KeyTy &tblgenKey) {
      auto shape = std::get<0>(tblgenKey);
      auto elementType = std::get<1>(tblgenKey);
      auto encoding = std::get<2>(tblgenKey);
      shape = allocator.copyInto(shape);

      return new (allocator.allocate<RankedTensorTypeStorage>())
          RankedTensorTypeStorage(shape, elementType, encoding);
    }
      ::llvm::ArrayRef<int64_t> shape;
      Type elementType;
      Attribute encoding;
  };
} // namespace detail
RankedTensorType RankedTensorType::get(ArrayRef<int64_t> shape, Type elementType, Attribute encoding) {
  
      return Base::get(elementType.getContext(), shape, elementType, encoding);
    ;
}
RankedTensorType RankedTensorType::getChecked(llvm::function_ref<::mlir::InFlightDiagnostic()> emitErrorFn, ArrayRef<int64_t> shape, Type elementType, Attribute encoding) {
  
      return Base::getChecked(emitErrorFn, elementType.getContext(), shape, elementType, encoding);
    ;
}
::llvm::ArrayRef<int64_t> RankedTensorType::getShape() const { return getImpl()->shape; }
Type RankedTensorType::getElementType() const { return getImpl()->elementType; }
Attribute RankedTensorType::getEncoding() const { return getImpl()->encoding; }
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::RankedTensorType)
namespace mlir {
TupleType TupleType::get(::mlir::MLIRContext *context, TypeRange elementTypes) {
  
      return Base::get(context, elementTypes);
    ;
}
TupleType TupleType::get(::mlir::MLIRContext *context) {
  
      return Base::get(context, TypeRange());
    ;
}
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::TupleType)
namespace mlir {

namespace detail {
  struct UnrankedMemRefTypeStorage : public ::mlir::TypeStorage {
    UnrankedMemRefTypeStorage (Type elementType, Attribute memorySpace)
      : elementType(elementType), memorySpace(memorySpace) { }

    /// The hash key is a tuple of the parameter types.
    using KeyTy = std::tuple<Type, Attribute>;
  bool operator==(const KeyTy &tblgenKey) const {
    if (!(elementType == std::get<0>(tblgenKey)))
      return false;
    if (!(memorySpace == std::get<1>(tblgenKey)))
      return false;
    return true;
  }
  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
      return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey));
    }

    /// Define a construction method for creating a new instance of this
    /// storage.
    static UnrankedMemRefTypeStorage *construct(::mlir::TypeStorageAllocator &allocator,
                          const KeyTy &tblgenKey) {
      auto elementType = std::get<0>(tblgenKey);
      auto memorySpace = std::get<1>(tblgenKey);

      return new (allocator.allocate<UnrankedMemRefTypeStorage>())
          UnrankedMemRefTypeStorage(elementType, memorySpace);
    }
      Type elementType;
      Attribute memorySpace;
  };
} // namespace detail
UnrankedMemRefType UnrankedMemRefType::get(Type elementType, Attribute memorySpace) {
  
      // Drop default memory space value and replace it with empty attribute.
      Attribute nonDefaultMemorySpace = skipDefaultMemorySpace(memorySpace);
      return Base::get(elementType.getContext(), elementType, nonDefaultMemorySpace);
    ;
}
UnrankedMemRefType UnrankedMemRefType::getChecked(llvm::function_ref<::mlir::InFlightDiagnostic()> emitErrorFn, Type elementType, Attribute memorySpace) {
  
      // Drop default memory space value and replace it with empty attribute.
      Attribute nonDefaultMemorySpace = skipDefaultMemorySpace(memorySpace);
      return Base::getChecked(emitErrorFn, elementType.getContext(), elementType, nonDefaultMemorySpace);
    ;
}
UnrankedMemRefType UnrankedMemRefType::get(Type elementType, unsigned memorySpace) {
  
      // Convert deprecated integer-like memory space to Attribute.
      Attribute memorySpaceAttr =
          wrapIntegerMemorySpace(memorySpace, elementType.getContext());
      return UnrankedMemRefType::get(elementType, memorySpaceAttr);
    ;
}
UnrankedMemRefType UnrankedMemRefType::getChecked(llvm::function_ref<::mlir::InFlightDiagnostic()> emitErrorFn, Type elementType, unsigned memorySpace) {
  
      // Convert deprecated integer-like memory space to Attribute.
      Attribute memorySpaceAttr =
          wrapIntegerMemorySpace(memorySpace, elementType.getContext());
      return UnrankedMemRefType::get(elementType, memorySpaceAttr);
    ;
}
Type UnrankedMemRefType::getElementType() const { return getImpl()->elementType; }
Attribute UnrankedMemRefType::getMemorySpace() const { return getImpl()->memorySpace; }
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::UnrankedMemRefType)
namespace mlir {

namespace detail {
  struct UnrankedTensorTypeStorage : public ::mlir::TypeStorage {
    UnrankedTensorTypeStorage (Type elementType)
      : elementType(elementType) { }

    /// The hash key is a tuple of the parameter types.
    using KeyTy = std::tuple<Type>;
  bool operator==(const KeyTy &tblgenKey) const {
    if (!(elementType == std::get<0>(tblgenKey)))
      return false;
    return true;
  }
  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
      return ::llvm::hash_combine(std::get<0>(tblgenKey));
    }

    /// Define a construction method for creating a new instance of this
    /// storage.
    static UnrankedTensorTypeStorage *construct(::mlir::TypeStorageAllocator &allocator,
                          const KeyTy &tblgenKey) {
      auto elementType = std::get<0>(tblgenKey);

      return new (allocator.allocate<UnrankedTensorTypeStorage>())
          UnrankedTensorTypeStorage(elementType);
    }
      Type elementType;
  };
} // namespace detail
UnrankedTensorType UnrankedTensorType::get(Type elementType) {
  
      return Base::get(elementType.getContext(), elementType);
    ;
}
UnrankedTensorType UnrankedTensorType::getChecked(llvm::function_ref<::mlir::InFlightDiagnostic()> emitErrorFn, Type elementType) {
  
      return Base::getChecked(emitErrorFn, elementType.getContext(), elementType);
    ;
}
Type UnrankedTensorType::getElementType() const { return getImpl()->elementType; }
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::UnrankedTensorType)
namespace mlir {

namespace detail {
  struct VectorTypeStorage : public ::mlir::TypeStorage {
    VectorTypeStorage (::llvm::ArrayRef<int64_t> shape, Type elementType)
      : shape(shape), elementType(elementType) { }

    /// The hash key is a tuple of the parameter types.
    using KeyTy = std::tuple<::llvm::ArrayRef<int64_t>, Type>;
  bool operator==(const KeyTy &tblgenKey) const {
    if (!(shape == std::get<0>(tblgenKey)))
      return false;
    if (!(elementType == std::get<1>(tblgenKey)))
      return false;
    return true;
  }
  static ::llvm::hash_code hashKey(const KeyTy &tblgenKey) {
      return ::llvm::hash_combine(std::get<0>(tblgenKey), std::get<1>(tblgenKey));
    }

    /// Define a construction method for creating a new instance of this
    /// storage.
    static VectorTypeStorage *construct(::mlir::TypeStorageAllocator &allocator,
                          const KeyTy &tblgenKey) {
      auto shape = std::get<0>(tblgenKey);
      auto elementType = std::get<1>(tblgenKey);
      shape = allocator.copyInto(shape);

      return new (allocator.allocate<VectorTypeStorage>())
          VectorTypeStorage(shape, elementType);
    }
      ::llvm::ArrayRef<int64_t> shape;
      Type elementType;
  };
} // namespace detail
VectorType VectorType::get(ArrayRef<int64_t> shape, Type elementType) {
  
      return Base::get(elementType.getContext(), shape, elementType);
    ;
}
VectorType VectorType::getChecked(llvm::function_ref<::mlir::InFlightDiagnostic()> emitErrorFn, ArrayRef<int64_t> shape, Type elementType) {
  
      return Base::getChecked(emitErrorFn, elementType.getContext(), shape, elementType);
    ;
}
::llvm::ArrayRef<int64_t> VectorType::getShape() const { return getImpl()->shape; }
Type VectorType::getElementType() const { return getImpl()->elementType; }
} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::VectorType)

#endif  // GET_TYPEDEF_CLASSES

