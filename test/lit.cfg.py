
import os
import platform

import lit.formats
# Global instance of LLVMConfig provided by lit
from lit.llvm import llvm_config
from lit.llvm.subst import ToolSubst

config.name = 'LLVM-TUTOR'
config.test_format = lit.formats.ShTest(not llvm_config.use_lit_shell)
# suffixes: A list of file extensions to treat as test files. This is overriden
# by individual lit.local.cfg files in the test subdirectories.
config.suffixes = ['.mlir']

# test_source_root: The root path where tests are located.
config.test_source_root = os.path.dirname(__file__)

# The list of tools required for testing - prepend them with the path specified
# during configuration (i.e. LT_LLVM_TOOLS_DIR/bin)
tools = ["opt", "lli", "not-14", "FileCheck-14", "clang"]

# llvm_config.add_tool_substitutions(tools, "/home/triton/tools/clang17/bin/")
