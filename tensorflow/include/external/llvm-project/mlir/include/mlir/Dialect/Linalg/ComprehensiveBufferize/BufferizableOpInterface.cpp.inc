/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* Interface Definitions                                                      *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

bool mlir::linalg::comprehensive_bufferize::BufferizableOpInterface::bufferizesToMemoryRead(OpOperand & opOperand, const BufferizationState & state) {
      return getImpl()->bufferizesToMemoryRead(getImpl(), getOperation(), opOperand, state);
  }
bool mlir::linalg::comprehensive_bufferize::BufferizableOpInterface::bufferizesToMemoryWrite(OpOperand & opOperand, const BufferizationState & state) {
      return getImpl()->bufferizesToMemoryWrite(getImpl(), getOperation(), opOperand, state);
  }
bool mlir::linalg::comprehensive_bufferize::BufferizableOpInterface::isMemoryWrite(OpResult opResult, const BufferizationState & state) {
      return getImpl()->isMemoryWrite(getImpl(), getOperation(), opResult, state);
  }
bool mlir::linalg::comprehensive_bufferize::BufferizableOpInterface::mustBufferizeInPlace(OpOperand & opOperand, const BufferizationState & state) {
      return getImpl()->mustBufferizeInPlace(getImpl(), getOperation(), opOperand, state);
  }
OpResult mlir::linalg::comprehensive_bufferize::BufferizableOpInterface::getAliasingOpResult(OpOperand & opOperand, const BufferizationState & state) {
      return getImpl()->getAliasingOpResult(getImpl(), getOperation(), opOperand, state);
  }
SmallVector<OpOperand *> mlir::linalg::comprehensive_bufferize::BufferizableOpInterface::getAliasingOpOperand(OpResult opResult, const BufferizationState & state) {
      return getImpl()->getAliasingOpOperand(getImpl(), getOperation(), opResult, state);
  }
BufferRelation mlir::linalg::comprehensive_bufferize::BufferizableOpInterface::bufferRelation(OpResult opResult, const BufferizationAliasInfo & aliasInfo, const BufferizationState & state) {
      return getImpl()->bufferRelation(getImpl(), getOperation(), opResult, aliasInfo, state);
  }
LogicalResult mlir::linalg::comprehensive_bufferize::BufferizableOpInterface::bufferize(RewriterBase & rewriter, const BufferizationState & state) {
      return getImpl()->bufferize(getImpl(), getOperation(), rewriter, state);
  }
bool mlir::linalg::comprehensive_bufferize::BufferizableOpInterface::isWritable(Value value, const BufferizationState & state) {
      return getImpl()->isWritable(getImpl(), getOperation(), value, state);
  }
bool mlir::linalg::comprehensive_bufferize::BufferizableOpInterface::isAllocationHoistingBarrier() {
      return getImpl()->isAllocationHoistingBarrier(getImpl(), getOperation());
  }
bool mlir::linalg::comprehensive_bufferize::BufferizableOpInterface::isNotConflicting(OpOperand * uRead, OpOperand * uWrite, const BufferizationState & state, const BufferizationAliasInfo & aliasInfo) {
      return getImpl()->isNotConflicting(getImpl(), getOperation(), uRead, uWrite, state, aliasInfo);
  }
