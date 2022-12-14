/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* Dialect Declarations                                                       *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

namespace mlir {
namespace tosa {

class TosaDialect : public ::mlir::Dialect {
  explicit TosaDialect(::mlir::MLIRContext *context)
    : ::mlir::Dialect(getDialectNamespace(), context,
      ::mlir::TypeID::get<TosaDialect>()) {
    
    getContext()->getOrLoadDialect<tensor::TensorDialect>();

    initialize();
  }

  void initialize();
  friend class ::mlir::MLIRContext;
public:
  ~TosaDialect() override;
  static constexpr ::llvm::StringLiteral getDialectNamespace() {
    return ::llvm::StringLiteral("tosa");
  }

  /// Materialize a single constant operation from a given attribute value with
  /// the desired resultant type.
  ::mlir::Operation *materializeConstant(::mlir::OpBuilder &builder,
                                         ::mlir::Attribute value,
                                         ::mlir::Type type,
                                         ::mlir::Location loc) override;
};
} // namespace tosa
} // namespace mlir
DECLARE_EXPLICIT_TYPE_ID(mlir::tosa::TosaDialect)
