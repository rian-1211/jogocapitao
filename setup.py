import cx_Freeze

executables = [cx_Freeze. Executable(script="capitao.py")]
cx_Freeze.setup(
    name='capitao',
    options={
        "build_exe": {
        "packages": ["pygame"],
        "include_files":["assets"]
    }},
    executables = executables
)