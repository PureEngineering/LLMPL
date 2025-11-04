```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██╗     ██╗     ███╗   ███╗██████╗ ██╗                                     ║
║   ██║     ██║     ████╗ ████║██╔══██╗██║                                     ║
║   ██║     ██║     ██╔████╔██║██████╔╝██║                                     ║
║   ██║     ██║     ██║╚██╔╝██║██╔═══╝ ██║                                     ║
║   ███████╗███████╗██║ ╚═╝ ██║██║     ███████╗                                ║
║   ╚══════╝╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝                                ║
║                                                                              ║
║              Large Language Model Programming Language                       ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

<div align="center">

**A programming language designed from the ground up for LLM code generation**

*When Large Language Models write code, precision matters. LLMPL makes correctness verifiable.*

[![Status](https://img.shields.io/badge/status-prototype-yellow)]()
[![Phase](https://img.shields.io/badge/phase-MVP_Complete-green)]()
[![License](https://img.shields.io/badge/license-MIT-blue)]()

</div>

---

## 🎯 Mission

**Deliver an industrial-strength programming language where Large Language Models can generate *provably correct* code through strict compiler enforcement rather than probabilistic luck.**

```
┌─────────────────────────────────────────────────────────────┐
│  Traditional Approach:                                      │
│    LLM → Generate Code → Hope It Works → Debug Forever      │
│                                                             │
│  LLMPL Approach:                                            │
│    LLM → Generate Code → Compiler Enforces Rules            │
└─────────────────────────────────────────────────────────────┘
```

---

## 💡 The Problem

Large Language Models struggle with:
- **Ambiguous syntax**: `+` means addition? Concatenation? Pointer arithmetic?
- **Silent failures**: Forgot error handling? Runtime crash.
- **Implicit conversions**: `"5" + 3` = who knows what?
- **Delimiter confusion**: Lost track of which `}` closes which `{`
- **Missing edge cases**: Handled success but forgot the error path

**Traditional languages were designed for humans.** Humans have context, intuition, and decades of debugging muscle memory. LLMs don't.

---

## ✨ The Solution

**LLMPL shifts the burden of correctness from the LLM to the compiler.**

```
╔════════════════════════════════════════════════════════════════╗
║                   LLMPL Core Principles                        ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║  ⚡ DETERMINISTIC GRAMMAR                                     ║
║     Every program has exactly one valid parse tree             ║
║                                                                ║
║  🔍 CONTEXT-RICH DELIMITERS                                    ║
║     'end function', 'end if' - always know what you're closing║
║                                                                ║
║  📝 NO SYMBOL OVERLOADING                                      ║
║     'plus', 'concatenated with' - one symbol, one meaning     ║
║                                                                ║
║  🛡️ NO IMPLICIT CONVERSIONS                                    ║
║     convert_int(x) - every type change is explicit            ║
║                                                                ║
║  ✅ NO SILENT FAILURES                                         ║
║     Result types - errors are values, not exceptions          ║
║                                                                ║
║  🎯 EXHAUSTIVE MATCHING                                        ║
║     Handle every case or compilation fails                    ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
```

---

## 🚀 Quick Start

### Hello World

```llmpl
define function main taking argv as List of String returning Result of Integer or String
function body:
  call print_line("Hello, LLMPL!")
  return success with value 0
end function
```

### Try the MVP Compiler

```bash
# Navigate to MVP directory
cd mvp

# Run the demo
python run_demo.py

# Compile and run your own LLMPL code
python llmpl_to_python.py --run example_mvp.llmpl
```

---

## 📖 Language Features

### Context-Rich Delimiters (SR-1)

**Traditional:**
```
if (condition) {
    for (i = 0; i < 10; i++) {
        if (check) {
        }
    }
}  // Which } closes what?
```

**LLMPL:**
```llmpl
if condition then:
  for each item in items do:
    if check then:
      // do something
    end if
  end for
end if  // Crystal clear!
```

### No Symbol Overloading (SR-3)

**Traditional:**
```
x = y + z     // Is this math? String concat? List merge?
ptr = &value  // Is & a reference? Bitwise AND?
```

**LLMPL:**
```llmpl
set x to y plus z
set greeting to "Hello" concatenated with " World"
```

### No Implicit Conversions (SR-6)

**Traditional:**
```javascript
"5" + 3        // "53" in JavaScript
"5" - 3        // 2 in JavaScript (wait, what?)
```

**LLMPL:**
```llmpl
// This won't compile - you must be explicit
declare variable count as Integer with value 5
call print_line("Count: " concatenated with convert_int(count))
```

### Result Types - No Silent Failures (SR-10)

**Traditional:**
```python
def divide(a, b):
    return a / b  # ZeroDivisionError surprise!
```

**LLMPL:**
```llmpl
define function divide taking a as Integer and b as Integer returning Result of Integer or String
function body:
  if b is equal to 0 then:
    return failure with error "Division by zero"
  end if
  return success with value a divided by b
end function

// Usage - MUST handle both cases
declare variable result with value divide(10, 2)
match result with cases:
  case success with value v:
    call print_line("Result: " concatenated with convert_int(v))
  case failure with error e:
    call print_line("Error: " concatenated with e)
end cases
```

### Exhaustive Pattern Matching (SR-11)

**Traditional:**
```rust
match status {
    Status::Ok => handle_ok(),
    Status::Pending => handle_pending(),
    // Forgot Status::Error - runtime panic!
}
```

**LLMPL:**
```llmpl
define enumeration Status with variants:
  variant Ok
  variant Pending
  variant Error
end enumeration Status

// This MUST handle all three variants or compilation fails
match current_status with cases:
  case Ok:
    call handle_ok()
  case Pending:
    call handle_pending()
  case Error:
    call handle_error()
end cases
```

---

## 🏗️ Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                      LLMPL Compiler Pipeline                    │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌──────────┐      ┌──────────┐      ┌──────────────────┐   │
│  │  Source  │ ───▶ │  Lexer   │ ───▶ │  Parser (LALR)   │   │
│  │  .llmpl  │      │          │      │                  │   │
│  └──────────┘      └──────────┘      └──────────────────┘   │
│                                              │                │
│                                              ▼                │
│                                      ┌──────────────────┐   │
│                                      │  Canonical IR    │   │
│                                      │  (Deterministic) │   │
│                                      └──────────────────┘   │
│                                              │                │
│                            ┌─────────────────┼─────────┐     │
│                            ▼                 ▼         ▼     │
│                    ┌──────────────┐  ┌──────────┐  ┌─────┐ │
│                    │ Type Checker │  │ Semantic │  │ ... │ │
│                    │   (SR-6)     │  │ Analysis │  │     │ │
│                    └──────────────┘  └──────────┘  └─────┘ │
│                                              │                │
│                            ┌─────────────────┴─────────┐     │
│                            ▼                           ▼     │
│                    ┌──────────────┐          ┌──────────────┐│
│                    │ LLVM Backend │          │  C Backend   ││
│                    │  (Native)    │          │  (Portable)  ││
│                    └──────────────┘          └──────────────┘│
│                            │                           │      │
│                            ▼                           ▼      │
│                    ┌──────────────┐          ┌──────────────┐│
│                    │   Binary     │          │  C99 Source  ││
│                    └──────────────┘          └──────────────┘│
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

**Current Status:** ✅ MVP compiler (Python backend) complete  
**In Progress:** Full compiler with LLVM and C backends

---

## 📂 Project Structure

```
llmpl/
│
├── README.md                    ← You are here
├── TODO.md                      ← Full compiler build plan
│
├── AGENTS.llmpl                 ← Agent guidelines (in LLMPL!)
├── requirements.llmpl           ← Critical requirements (in LLMPL!)
├── example.txt                  ← Language examples
│
└── mvp/                         ← ✅ Working MVP Compiler
    ├── llmpl_to_python.py      ← MVP compiler implementation
    ├── run_demo.py              ← Demo runner
    ├── example_mvp.llmpl        ← Example program
    ├── out.py                   ← Generated Python
    └── MVP_GAPS.md              ← What the MVP doesn't do (yet)
```

---

## 🎯 Critical Requirements

The language is built on **8 critical requirements** that work together to make LLM-generated code reliable:

| ID | Requirement | Why It Matters |
|----|-------------|----------------|
| **ARCH-1.0** | Formal Deterministic Grammar | One program = one parse tree, always |
| **ARCH-2.0** | Canonical IR | Lossless, stable intermediate representation |
| **SR-1** | Context-Rich Delimiters | `end function`, `end if` - never lose track |
| **SR-3** | No Symbol Overloading | One symbol = one meaning |
| **SR-6** | No Implicit Conversions | Every type change is explicit |
| **SR-10** | No Silent Failures | Errors are types, not exceptions |
| **SR-11** | Exhaustive Matching | Handle every case or don't compile |
| **NFR-1** | Transparent Diagnostics | Precise, reproducible error messages |

> 📖 **Full requirements specification:** See [`requirements.llmpl`](requirements.llmpl) (written in LLMPL itself!)

---

## 🤖 LLM Agent Guidelines

LLMPL includes comprehensive guidelines for LLM agents writing LLMPL code:

```
╔═══════════════════════════════════════════════════════════╗
║           Agent Code Generation Checklist                 ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  1. START with type definitions                           ║
║  2. PLAN function decomposition                           ║
║  3. GENERATE using keywords only, never operators         ║
║  4. CLOSE every block with context-specific delimiters    ║
║  5. CONVERT types explicitly                              ║
║  6. RETURN Result for fallible operations                 ║
║  7. MATCH exhaustively on all variants                    ║
║  8. VERIFY delimiter balance and type consistency         ║
║  9. REFACTOR repeated patterns                            ║
║  10. DOCUMENT non-obvious logic                           ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

> 🤖 **Full agent playbook:** See [`AGENTS.llmpl`](AGENTS.llmpl) (also in LLMPL!)

---

## 🔬 Examples

### Variable Declaration and Assignment

```llmpl
// Explicit type declaration
declare variable count as Integer with value 0
declare variable message as String with value "Hello"

// Type inference from value
declare variable items with value create_empty_list_of<String>()

// Assignment
set count to count plus 1
set message to message concatenated with " World"
```

### Control Flow

```llmpl
// If-else
if temperature is greater than 30 then:
  call print_line("Hot day!")
else:
  call print_line("Nice weather")
end if

// Loops
for each item in items do:
  call print_line(item)
end for
```

### Custom Types

```llmpl
// Enumerations
define enumeration Priority with variants:
  variant Critical
  variant High
  variant Medium
  variant Low
end enumeration Priority

// Records (structs)
define record Task with layout sequential
fields:
  field id as Integer
  field title as String
  field priority as Priority
end fields
end record Task

// Create records
declare variable task with value create_record Task with fields:
  set id to 1
  set title to "Fix compiler bug"
  set priority to Critical
end fields
```

### Functions with Result Types

```llmpl
define function parse_integer taking input as String returning Result of Integer or String
function body:
  // Validation logic here
  if is_valid_integer(input) then:
    declare variable parsed_value with value convert_string_to_integer(input)
    return success with value parsed_value
  else:
    return failure with error "Invalid integer format"
  end if
end function
```

---

## 🛣️ Roadmap

### ✅ Phase 1: MVP Proof of Concept (Complete)
- [x] Minimal syntax subset
- [x] Python backend for quick validation
- [x] Basic demonstrations
- [x] Gap analysis documented

### 🚧 Phase 2: Full Compiler (In Progress)
- [ ] Complete EBNF grammar
- [ ] Lexer with location tracking
- [ ] LALR(1) parser
- [ ] Type checker with Result enforcement
- [ ] Canonical IR with serialization

### 📅 Phase 3: Production Backends (Planned)
- [ ] LLVM backend (native binaries)
- [ ] C99 backend (portable code)
- [ ] Runtime library (strings, lists, maps)
- [ ] Differential testing (LLVM vs C equivalence)

### 🎯 Phase 4: Tooling & Ecosystem (Future)
- [ ] Language Server Protocol (LSP)
- [ ] Debugger integration
- [ ] Package manager
- [ ] Standard library expansion
- [ ] IDE plugins

> 📋 **Detailed timeline:** See [`TODO.md`](TODO.md) for 24-week implementation plan

---

## 🎓 Philosophy

### Why Verbose Syntax?

**Short answer:** Verbosity is a feature, not a bug.

**Long answer:**

Traditional languages optimize for **human reading speed**. Humans see patterns, use context, and fill in gaps naturally.

LLMs work differently. They:
- Don't have context awareness across token boundaries
- Can't "see" the overall structure of deeply nested code
- Struggle with overloaded symbols that mean different things in different contexts
- Generate code line-by-line without global awareness

**LLMPL trades brevity for precision.** When you write:
```llmpl
if condition then: ... end if
```

Instead of:
```
if (condition) { ... }
```

You're giving the LLM (and humans!) explicit context at every boundary. The compiler can catch mismatched delimiters immediately. The error message can say "expected 'end if' but found 'end for'" instead of generic "syntax error".

### Shift Left, Shift Up

```
Traditional Approach:           LLMPL Approach:
┌────────────────┐             ┌────────────────┐
│ LLM generates  │             │ LLM generates  │
│ ambiguous code │             │ strict code    │
└────────┬───────┘             └────────┬───────┘
         │                              │
         ▼                              ▼
┌────────────────┐             ┌────────────────┐
│ Compiles with  │             │ Compiler       │
│ warnings       │             │ enforces rules │
└────────┬───────┘             └────────┬───────┘
         │                              │
         ▼                              ├─✗─▶ Violation
┌────────────────┐                     │     Caught!
│ Runs with      │                     │
│ subtle bugs    │                     ▼
└────────┬───────┘             ┌────────────────┐
         │                     │ LLM fixes and  │
         ▼                     │ re-generates   │
┌────────────────┐             └────────┬───────┘
│ Runtime crash  │                      │
└────────┬───────┘                      ▼
         │                     ┌────────────────┐
         ▼                     │ Correct code,  │
┌────────────────┐             │ first run      │
│ Hours of       │             └────────────────┘
│ debugging      │
└────────────────┘
```

**Catch errors at compile time, not runtime. Use the type system, not testing.**

---

## 📚 Documentation

- **[TODO.md](TODO.md)** - Complete compiler build plan with 9 workstreams
- **[MVP_GAPS.md](mvp/MVP_GAPS.md)** - What the MVP doesn't do (yet)
- **[requirements.llmpl](requirements.llmpl)** - Critical requirements (executable spec!)
- **[AGENTS.llmpl](AGENTS.llmpl)** - LLM agent guidelines (meta-programming!)
- **[example.txt](example.txt)** - Language syntax examples
- **[example_mvp.llmpl](mvp/example_mvp.llmpl)** - Working MVP example

---

## 🧪 Running the MVP

The MVP compiler demonstrates LLMPL's core syntax by transpiling to Python:

```bash
# Basic compilation
cd mvp
python llmpl_to_python.py example_mvp.llmpl

# Compile and run
python llmpl_to_python.py --run example_mvp.llmpl

# Using the demo runner
python run_demo.py
```

**What works in MVP:**
- ✅ Function definitions with parameters
- ✅ Variable declarations and assignments
- ✅ Arithmetic and string operations with keywords
- ✅ If/else conditionals
- ✅ Boolean logic
- ✅ Function calls
- ✅ Result types (basic)

**What doesn't work yet:**
- ❌ Loops (for/while)
- ❌ Pattern matching (match statements)
- ❌ Custom types (enumerations, records)
- ❌ Type checking
- ❌ Module system
- ❌ Standard library

> 🔍 **See [MVP_GAPS.md](mvp/MVP_GAPS.md) for complete gap analysis**

---

## 🤝 Contributing

This project is in active prototype phase. Contributions welcome in:

1. **Language Design** - Discuss syntax, semantics, and requirements
2. **Compiler Implementation** - Help build the full compiler (Rust target)
3. **Tooling** - LSP, formatters, linters
4. **Documentation** - Examples, tutorials, guides
5. **Testing** - Test cases, fuzzing, differential testing

**Design Principles:**
- Determinism first - every decision must be reproducible
- Explicit over implicit - verbosity is a feature
- Type safety - shift errors left to compile time
- LLM-friendly - optimize for reliable code generation

---

## 🔬 Research Context

LLMPL is an exploration of a fundamental question:

> **Can we design a programming language where LLMs are *systematically more reliable* than in traditional languages?**

Traditional languages evolved over decades with human ergonomics in mind. LLMPL starts from first principles:

1. **What errors do LLMs make most often?**
   - Delimiter mismatches → Context-rich delimiters
   - Symbol confusion → No overloading
   - Forgotten error handling → Result types
   - Type mismatches → No implicit conversions
   - Missing edge cases → Exhaustive matching

2. **What compiler features catch those errors?**
   - Deterministic parsing
   - Strong static typing
   - Exhaustiveness checking
   - Explicit conversion enforcement

3. **What syntax makes those features natural?**
   - Keyword-based operators
   - Context-specific delimiters
   - Explicit type annotations
   - Result-based error handling

**LLMPL is designed to make the compiler the LLM's best friend, not its adversary.**

---

## 📊 Comparison

| Feature | JavaScript | Python | Rust | LLMPL |
|---------|-----------|--------|------|-------|
| **Deterministic Grammar** | ❌ ASI | ✅ | ✅ | ✅ |
| **Context-Rich Delimiters** | ❌ `}` | ❌ Indent | ❌ `}` | ✅ `end X` |
| **No Symbol Overload** | ❌ `+` | ❌ `+` | ❌ `*` | ✅ Keywords |
| **No Implicit Convert** | ❌ `"5"+3` | ❌ Many | ⚠️ Some | ✅ None |
| **Result Types** | ❌ Exceptions | ❌ Exceptions | ✅ | ✅ |
| **Exhaustive Matching** | ❌ | ❌ | ✅ | ✅ |
| **LLM-Optimized** | ❌ | ❌ | ❌ | ✅ |

---

## 🎬 Example Programs

### Fibonacci Sequence

```llmpl
define function fibonacci taking n as Integer returning Result of Integer or String
function body:
  if n is less than 0 then:
    return failure with error "Negative input not allowed"
  end if
  
  if n is equal to 0 then:
    return success with value 0
  end if
  
  if n is equal to 1 then:
    return success with value 1
  end if
  
  declare variable a as Integer with value 0
  declare variable b as Integer with value 1
  declare variable counter as Integer with value 2
  
  loop while counter is less than or equal to n do:
    declare variable temp with value a plus b
    set a to b
    set b to temp
    set counter to counter plus 1
  end loop
  
  return success with value b
end function
```

### Error Handling Chain

```llmpl
define function process_user_input taking input as String returning Result of Integer or String
function body:
  // Chain of fallible operations
  declare variable trimmed_result with value trim_whitespace(input)
  match trimmed_result with cases:
    case failure with error e:
      return failure with error e
    case success with value trimmed:
      declare variable parsed_result with value parse_integer(trimmed)
      match parsed_result with cases:
        case failure with error e:
          return failure with error e
        case success with value number:
          if number is greater than 0 then:
            return success with value number
          else:
            return failure with error "Number must be positive"
          end if
      end cases
  end cases
end function
```

---

## 💬 FAQ

### Q: Why not just use linters on existing languages?

**A:** Linters warn; compilers enforce. LLMPL requirements aren't optional style preferences—they're architectural guarantees. You can't turn off "no implicit conversions" any more than you can disable type checking.

### Q: Isn't this just verbose Rust?

**A:** Rust inspired several features (Result types, exhaustive matching), but LLMPL makes different tradeoffs:
- **More verbose delimiters** (`end function` vs `}`) to help LLMs track nesting
- **Keyword operators** (`plus` vs `+`) to eliminate symbol overloading
- **Even stricter conversions** (Rust allows `as`, we require named functions)
- **LLM-first design** (humans are secondary consideration)

### Q: Will real programmers use this?

**A:** Maybe not for hand-written code. LLMPL is optimized for:
1. LLM-generated code that needs to be correct the first time
2. Safety-critical applications where verbose clarity beats terse ambiguity
3. Teaching contexts where explicit syntax aids understanding
4. Code generation pipelines where humans rarely read the output

### Q: What about performance?

**A:** The compiler targets both LLVM (native performance) and C99 (portable). The verbose syntax doesn't impact runtime—it only affects parsing. Once compiled, LLMPL code should perform comparably to Rust or C.

### Q: Can I use LLMPL in production?

**A:** Not yet. This is a prototype. The MVP compiler exists for syntax validation. The full compiler targeting LLVM/C is under development. Check back in 2026 for production-ready releases.

---

## 📜 License

MIT License - see LICENSE file for details

---

## 🌟 Credits

**LLMPL** is an experimental language exploring the intersection of:
- Programming language design
- Large language model capabilities and limitations
- Type system theory
- Compiler construction
- Human-computer interaction (but for AIs)

Inspired by the explicit syntax of Ada, the safety of Rust, the simplicity of Go, and the determinism of formal methods.

---

<div align="center">

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║  "Programs must be written for people to read, and only      ║
║   incidentally for machines to execute."                     ║
║                                        — Abelson & Sussman   ║
║                                                               ║
║  "Programs must be written for LLMs to generate correctly,   ║
║   and only incidentally for humans to read."                 ║
║                                        — LLMPL Philosophy    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**Made with precision, designed for reliability, built for the future of AI-assisted programming.**

⭐ **Star this repo if you believe LLMs deserve better languages to work with!**

</div>

---

**Latest Update:** November 4, 2025  
**Project Status:** MVP Complete, Full Compiler In Progress  
**Feedback:** Open an issue or start a discussion!

