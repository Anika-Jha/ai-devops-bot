import ast
import textwrap

def generate_tests(source_code):
    tree = ast.parse(source_code)
    tests = ""

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            tests += textwrap.dedent(f"""
            def test_{func_name}():
                # TODO: Replace with real test
                result = {func_name}(*args)
                assert result == expected
            """)
    return tests.strip()
