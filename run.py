# +
import ast
import types
import sys

with open("sample.py") as f:
       p = ast.parse(f.read())

for node in p.body[:]:
    if not isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom)):
        p.body.remove(node)

module = types.ModuleType("mod")
code = compile(p, "mod.py", 'exec')
sys.modules["mod"] = module
exec(code,  module.__dict__)

from mod import *
# -

if __name__ == '__main__':
    sample_class = SampleClass(10)
    print("run.py: SampleClass", sample_class())
    print("run.py: make_randint", make_randint(100))
