#!/usr/bin/env python3
# Very simple calculator — enter arithmetic expressions and get results.
# Type q, quit or press Ctrl-C/Ctrl-D to exit.
# Note: For simplicity this uses eval with builtins disabled; don't run untrusted input.

def main():
    print("Simple calculator. Type 'q' or 'quit' to exit.")
    while True:
        try:
            expr = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not expr:
            continue
        if expr.lower() in ("q", "quit", "exit"):
            break

        try:
            # Evaluate expression simply; no builtins available.
            result = eval(expr, {"__builtins__": None}, {})
        except Exception as e:
            print("Error:", e)
        else:
            print(result)

if __name__ == "__main__":
    main()
