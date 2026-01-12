from typing import List, Tuple
import ast

def extract_function_definitions(source_code: str) -> List[Tuple[str, List[str]]]:
    """
    Extracts function definitions from the given Python source code.

    Args:
        source_code (str): The Python source code to parse.
    Returns:
        List[Tuple[str, List[str]]]: A list of tuples where each tuple contains
                                      the function name and a list of its argument names.
    """
    function_definitions = []

    class FunctionDefVisitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node: ast.FunctionDef):
            arg_names = [arg.arg for arg in node.args.args]
            function_definitions.append((node.name, arg_names))
            self.generic_visit(node)

    tree = ast.parse(source_code)
    visitor = FunctionDefVisitor()
    visitor.visit(tree)

    return function_definitions