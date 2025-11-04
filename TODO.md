# LLMPL Compiler Build Plan

**Mission**  
Deliver an industrial-strength LLMPL compiler that targets both LLVM IR (native binaries) and portable C99, while demonstrably upholding the critical language requirements (ARCH-1.0, ARCH-2.0, SR-1, SR-3, SR-6, SR-10, SR-11, NFR-1).

**Status**: Planning ✔︎ | Implementation ✖︎  
**Primary Deliverables**
- **First**, ship a minimal compiler proof-of-concept that validates LLMPL syntax and produces any executable artifact (even a stub interpreter) to de-risk the grammar.
- Deterministic front-end (lexer, parser, semantic analysis) with canonical IR (ARCH-2.0)
- Dual code generators (LLVM & C) producing identical observable behaviour
- Runtime + standard library sufficient for `example.txt`, `requirements.llmpl`, `AGENTS.llmpl`
- Tooling, diagnostics, and tests that enforce the critical requirements

---

## Guiding Constraints & Principles
- **Determinism first**: Grammar, parser, and IR must remain unambiguous and reproducible (ARCH-1.0, ARCH-2.0).
- **Explicit syntax**: Context-rich delimiters and keyword-only operators are mandatory (SR-1, SR-3).
- **Type discipline**: No implicit conversions; errors are surfaced through types and exhaustive matches (SR-6, SR-10, SR-11).
- **Transparent diagnostics**: Every phase must emit structured, stable diagnostics (NFR-1).
- **Backend parity**: LLVM and C outputs must stay behaviourally equivalent; regressions are detected through differential tests.

---

## Workstream Overview
Each workstream ends with a gating review. Tasks are grouped by priority within the workstream.

### WS-MVP – Minimal Syntax Proof of Concept
- [x] Stand up a lightweight lexer + parser for a curated subset (functions, declarations, control flow)
- [x] Emit a simple executable artifact (e.g., direct interpretation or translation to a scripting language) to prove end-to-end flow
- [x] Capture diagnostics for malformed syntax (delimiter mismatches, unknown keywords)
- [x] Script automated runs for the subset of `example.txt` to verify viability
- [x] Document gaps between MVP syntax and full language spec

**Gate MVP**: PoC parses and executes the subset program end-to-end, confirming grammar direction before full compiler investment.

### WS0 – Language Definition & Project Bootstrap
- [ ] Draft complete EBNF + token vocabulary (ARCH-1.0, SR-1, SR-3)
- [ ] Establish “source of truth” spec repo (version-controlled, reviewed)
- [ ] Publish glossary of keywords, delimiters, and intrinsic signatures
- [ ] Define minimal coding conventions for compiler implementation (Rust recommended)

**Gate 0**: Spec bundle approved; grammar validated against `example.txt`, `requirements.llmpl`, `AGENTS.llmpl` via exploratory parser.

---

### WS1 – Front-End Infrastructure (Lexer & Parser)
- [ ] Implement hand-written lexer with location tracking, keyword table, and strict operator rejection (SR-3)
- [ ] Implement LALR(1)-compatible recursive-descent parser that mirrors grammar ordering
- [ ] Enforce delimiter matching during parse; emit structured errors (SR-1, NFR-1)
- [ ] Build AST definitions with explicit node tags and source spans
- [ ] Provide golden parser tests for all core constructs + negative cases

**Gate 1**: Parser accepts all reference programs; mismatch tests confirm SR-1 enforcement; diagnostic snapshots stored.

---

### WS2 – Semantic Analysis & Type Checking
- [ ] Design symbol table with explicit scopes (module, function, block)
- [ ] Implement type checker with explicit conversions only (SR-6)
- [ ] Enforce Result-type usage and propagation (SR-10)
- [ ] Implement exhaustive pattern checks for enums and Result (SR-11)
- [ ] Validate intrinsic declarations vs usage (undeclared bodies)
- [ ] Add semantic regression suite (positive + failure fixtures)

**Gate 2**: `example.txt`, `requirements.llmpl`, `AGENTS.llmpl` type-check cleanly; failure fixtures exercise SR-6/10/11 diagnostics.

---

### WS3 – Canonical Intermediate Representation (ARCH-2.0)
- [ ] Define lossless IR schema (types, control flow, metadata, source mapping)
- [ ] Implement AST → IR lowering with deterministic ordering
- [ ] Serialize IR to JSON/CBOR for debugging and LLM feedback loops
- [ ] Add IR validation pass (structural invariants, type sanity)
- [ ] Generate IR visualizer for dev ergonomics

**Gate 3**: IR round-trips without loss; `requirements.llmpl` lowered IR reviewed and approved.

---

### WS4 – Shared Runtime & Intrinsics
- [ ] Specify runtime ABI for strings, lists, maps, Result, Date
- [ ] Implement reference counting (baseline) with hooks for optional GC
- [ ] Provide intrinsic stubs for both backends (print_line, join, convert_int, etc.)
- [ ] Document runtime error semantics (panic vs Result)
- [ ] Add runtime unit tests (language-independent)

**Gate 4**: Runtime library builds for host platform; intrinsic contract tests pass.

---

### WS5 – LLVM Backend
- [ ] Map IR types to LLVM types; establish module/layout metadata
- [ ] Emit LLVM IR for expressions, control flow, pattern matches (switch-based)
- [ ] Lower Result and enum representations to tagged unions
- [ ] Integrate runtime intrinsics via LLVM external declarations
- [ ] Emit DWARF-friendly debug info leveraging source spans (nice-to-have)
- [ ] Provide `llmplc --emit-llvm` artifact + pipeline to native binary

**Gate 5**: LLVM backend executes smoke programs; outputs captured for regression comparison.

---

### WS6 – C Backend
- [ ] Define C naming and file structure (headers, source modules)
- [ ] Generate C structs/enums matching IR layout
- [ ] Render control flow + pattern matches using structured if/switch trees
- [ ] Integrate shared runtime via headers and symbol table
- [ ] Ensure emitted C adheres to C99 and passes clang-format (or custom formatter)
- [ ] Provide build scripts for GCC/Clang targets

**Gate 6**: C backend executes same smoke programs as LLVM; recorded outputs match LLVM results.

---

### WS7 – Compiler Driver, Tooling & CLI
- [ ] Implement `llmplc` driver with `--target {llvm,c,obj,exe}`
- [ ] Add `--emit-ir`, `--emit-llvm`, `--emit-c`, `--check`, `--verify` flags
- [ ] Provide basic build caching (hashed IR)
- [ ] Supply AST/IR debugging commands

**Gate 7**: Driver builds both backends from single invocation; developer ergonomics validated by dogfooding.

---

### WS8 – Quality, Testing & Compliance
- [ ] Unit tests: lexer, parser, type checker, IR lowering, backends
- [ ] Integration tests: sample programs through both backends → runtime comparison
- [ ] Differential testing harness (LLVM vs C output equivalence)
- [ ] Property-based tests for type system invariants
- [ ] Fuzzing: lexer -> parser -> IR pipeline with sanitizer builds
- [ ] Automated requirement compliance report referencing ARCH/SR/NFR IDs

**Gate 8**: CI pipeline runs full suite; compliance report shows 100% coverage of critical requirements.

---

### WS9 – Documentation & Ecosystem
- [ ] Language reference + coding guidelines published
- [ ] Compiler architecture docs (frontend, IR, backends, runtime)
- [ ] Getting-started + tutorials (Result types, exhaustive matches)
- [ ] Contributor guide + code review checklist tied to requirements
- [ ] LSP stub or integration backlog documented

**Gate 9**: Documentation reviewed, published, and linked from project README.

---

## Cross-Cutting Checks
- [ ] Maintain traceability matrix linking tasks → requirements → tests
- [ ] Add structured diagnostics library reused across phases (NFR-1)
- [ ] Track performance budgets (compile time, runtime) once functional parity is achieved
- [ ] Run weekly architecture review to catch regression in determinism or clarity

---

## Milestones & Timeline (Indicative)

| Milestone | Workstreams | Target | Exit Criteria |
|-----------|-------------|--------|---------------|
| **M0** Syntax PoC | WS-MVP | Week 2 | Minimal subset parsed + executed via PoC backend |
| **M1** Front-End MVP | WS0–WS1 | Week 4 | Parser + diagnostics verified on reference sources |
| **M2** Type-Safe Front-End | WS2 | Week 7 | Semantic checks & diagnostics complete |
| **M3** Canonical IR | WS3 | Week 9 | IR spec approved, lowering functional |
| **M4** Runtime Foundation | WS4 | Week 11 | Intrinsics operational, shared runtime ABI |
| **M5** LLVM Backend MVP | WS5 | Week 14 | Native binary generation for smoke suite |
| **M6** C Backend MVP | WS6 | Week 17 | C output parity with LLVM suite |
| **M7** Tooling & Driver | WS7 | Week 19 | CLI + artifacts integrated |
| **M8** Quality & Compliance | WS8 | Week 22 | CI + differential + compliance dashboard |
| **M9** Documentation Launch | WS9 | Week 24 | Docs published; ready for external users |

Timelines assume one dedicated team; adjust if contributors vary.

---

## Open Decisions
- [ ] Confirm implementation language (default: Rust)
- [ ] Select IR serialization format (JSON vs CBOR)
- [ ] Choose runtime memory strategy roadmap (reference counting first, optional GC later)
- [ ] Determine testing framework (Rust’s built-in vs custom harness)
- [ ] Finalize differential testing oracle (snapshot outputs vs behavioural probes)

---

## Risks & Mitigations
- **Grammar ambiguity** → schedule early parser prototypes + grammar linting.  
- **Backend divergence** → enforce differential tests starting with first backend.  
- **Runtime complexity** → prioritize minimal RC-based runtime before adding advanced features.  
- **Diagnostic drift** → shared diagnostic library + golden test snapshots.  
- **Schedule slip** → milestone reviews with go/no-go decision on optional features (optimizations, GC, advanced stdlib).

---

## Reference Corpus
- `example.txt` – Core syntax smoketest
- `requirements.llmpl` – Non-negotiable rules (input + compliance target)
- `AGENTS.llmpl` – Agent guidelines and meta-tests

---

**Last Updated**: 2025-11-04  
**Plan Owner**: LLMPL Compiler Team
