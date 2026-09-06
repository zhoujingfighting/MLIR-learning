include_directories(${CMAKE_BINARY_DIR}/include)
include_directories(${CMAKE_BINARY_DIR})
include_directories(${CMAKE_CURRENT_BINARY_DIR})
set(LLVM_TARGET_DEFINITIONS ToyCombine.td)
mlir_tablegen(ToyCombine.inc -gen-rewriters)
add_public_tablegen_target(ToyCombineIncGen)

get_property(dialect_libs GLOBAL PROPERTY MLIR_DIALECT_LIBS)
get_property(extension_libs GLOBAL PROPERTY MLIR_EXTENSION_LIBS)

add_mlir_library(toy
    PARTIAL_SOURCES_INTENDED
    AST.cpp
    Dialect.cpp
    MLIRGen.cpp
    ToyCombine.cpp
    ToyToAffineLoops.cpp

    DEPENDS
    ToyOpsIncGen
    ToyCombineIncGen
)

add_llvm_executable(mlir-toy
    PARTIAL_SOURCES_INTENDED
    toy.cpp
)
llvm_update_compile_flags(mlir-toy)
target_link_libraries(mlir-toy PRIVATE toy ${dialect_libs} ${extension_libs})
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)
