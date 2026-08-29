'''
this calculator is optimised than other calculator and takes less memory
'''

from typing import Union, Callable, Dict
from operator import add, sub, mul, truediv, floordiv, mod, pow as power


class Calculator:
    OPERATIONS: Dict[str, Callable[[Union[int, float], Union[int, float]], Union[int, float]]] = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': truediv,
        '//': floordiv,
        '%': mod,
        '**': power,
    }
    
    def calculate(self, a: Union[int, float], operator: str, b: Union[int, float]) -> Union[int, float]:
        if operator not in self.OPERATIONS:
            raise ValueError(f"Invalid operator: {operator}. Available: {', '.join(self.OPERATIONS.keys())}")
        
        if operator in ('/', '//') and b == 0:
            raise ValueError("Cannot divide by zero")
        
        return self.OPERATIONS[operator](a, b)


def main() -> None:
    calc = Calculator()
    
    print("=" * 50)
    print(" Calculator")
    print("=" * 50)
    print(f"Available operations: {', '.join(calc.OPERATIONS.keys())}")
    print("Commands: 'quit'")
    print("=" * 50)
    
    while True:
        try:
            user_input = input("\nEnter expression (e.g., 10 + 5): ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            tokens = None
            operator = None
            
            for op in calc.OPERATIONS:
                if op in user_input:
                    tokens = user_input.split(op)
                    if len(tokens) == 2:
                        operator = op
                        break
            
            if not tokens or operator is None:
                print("Invalid format. Use: <number> <operator> <number>")
                continue
            
            a, b = float(tokens[0].strip()), float(tokens[1].strip())
            result = calc.calculate(a, operator, b)
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except (IndexError, ValueError) as e:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
