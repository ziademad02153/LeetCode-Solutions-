# LeetCode Problem Solving | Medium & Hard

## Overview
This repository is dedicated exclusively to solving Medium and Hard level algorithmic problems from LeetCode. The core objective is to showcase advanced problem-solving skills, deep understanding of data structures, and the ability to write highly optimized, production-ready code.

## Methodology
Every solution provided in this repository is crafted with a focus on:
1. **Mathematical Precision:** Utilizing advanced mathematical concepts (e.g., GCD, Combinatorics) to bypass common precision errors.
2. **Memory Optimization:** Implementing in-place operations and smart memory allocations to minimize Space Complexity.
3. **Execution Speed:** Eliminating redundant loops and leveraging C-optimized built-in functions (in Python) to achieve maximum runtime efficiency.

## Standard Solution Blueprint

Each problem's solution follows a rigorous documentation standard to clarify the thought process and the algorithmic execution flow.

### Algorithmic Execution Flow

The following flowchart represents the general strategy applied to complex problems, ensuring edge cases are handled before executing the core logic.

```mermaid
graph TD;
    A[Start Algorithm] --> B{Edge Case Validation};
    B -- Invalid / Trivial --> C[Return Base Case];
    B -- Valid Input --> D[Initialize Core Data Structures];
    D --> E[Main Execution Loop];
    E --> F{Optimization Condition Met?};
    F -- Yes --> G[Update Global State & Continue];
    F -- No --> H[Break / Skip Redundant Work];
    G --> I{Is End of Data?};
    H --> I;
    I -- No --> E;
    I -- Yes --> J[Calculate Final Result];
    J --> K[Return Output];
