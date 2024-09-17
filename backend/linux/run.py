from cffi import FFI
import os

ffi = FFI()

# Load the shared library
lib_path = os.path.join(os.path.dirname(__file__), 'main.cpython-311-x86_64-linux-gnu.so')
main = ffi.dlopen(lib_path)

# Define the function signature
ffi.cdef('void startgame();')

# Call the startgame function
main.startgame()
