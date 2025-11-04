# MVP Compiler Gaps

The current LLMPL → Python proof-of-concept supports only a very small subset of
the language. Notable omissions include:

- Multiple modules or complex scoping (the MVP now handles simple helper functions but not module systems or nested scopes).
- Complex expressions (parentheses, precedence beyond the provided keywords,
  unary minus) and literal forms (floats, lists, maps).
- Control-flow beyond `if`/`else` (no loops, pattern matching, or `match`).
- Result/option handling, error propagation, or type checking.
- Runtime library coverage: only `print_line` is recognised.
- Proper lexer/parser implementation – the MVP still relies on simple
  pattern matching and therefore is not yet LALR(1) compliant.

These gaps inform the backlog for the full compiler effort tracked in `TODO.md`.
