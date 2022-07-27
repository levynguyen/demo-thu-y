//===- ArithInterfaceImpl.h - Arith Impl. of BufferizableOpInterface ------===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//

#ifndef MLIR_DIALECT_LINALG_COMPREHENSIVEBUFFERIZE_ARITH_INTERFACE_IMPL_H
#define MLIR_DIALECT_LINALG_COMPREHENSIVEBUFFERIZE_ARITH_INTERFACE_IMPL_H

namespace mlir {

class DialectRegistry;

namespace linalg {
namespace comprehensive_bufferize {
namespace arith_ext {

void registerBufferizableOpInterfaceExternalModels(DialectRegistry &registry);

} // namespace arith_ext
} // namespace comprehensive_bufferize
} // namespace linalg
} // namespace mlir

#endif // MLIR_DIALECT_LINALG_COMPREHENSIVEBUFFERIZE_ARITH_INTERFACE_IMPL_H
