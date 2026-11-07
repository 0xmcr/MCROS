---
trigger: always_on
---

# Clean Code, Inline Documentation, and Multi-Language Standards

## 1. Professional Code Documentation (JSDoc / TSDoc / Docstrings)
Every exported module, class, interface, and public function must include professional documentation:
- **Function Purpose**: Clear, concise explanation of the business logic and algorithmic responsibility.
- **Typed Parameter Annotations**: Documenting `@param` types, expected formats, and constraints.
- **Return Type & Exceptions**: Documenting `@returns` and possible `@throws` / error states.
- **The "Why", Not Just "What"**: Inline comments must explain *why* non-obvious business rules or edge-case handling exist, rather than repeating what the syntax already shows.

```typescript
/**
 * Processes an order checkout, applies regional tax calculation,
 * and reserves inventory within a transactional boundary.
 *
 * @param orderId - Unique UUID identifier of the customer order.
 * @param paymentToken - Verified cryptographic payment token from gateway.
 * @returns Resolves with the finalized Order entity including transaction receipt.
 * @throws {PaymentDeclinedError} When gateway declines card authorization.
 * @throws {InsufficientInventoryError} When items become out-of-stock during processing.
 */
export async function processOrderCheckout(
  orderId: string,
  paymentToken: string
): Promise<FinalizedOrderReceipt> { ... }
```

## 2. Clean Architecture & Maintainability Standards
- **Meaningful Identifiers**: Use descriptive names (`isSubscriptionActive` instead of `flag`, `customerBillingAddress` instead of `addr`).
- **No Magic Numbers**: Replace arbitrary numeric or string constants with named enums or `const` objects.
- **Single Responsibility Principle (SRP)**: Keep functions focused; split monolithic functions (>50 lines) into cohesive, testable helpers.
- **Zero Dead Code**: Remove commented-out code blocks, unused imports, and obsolete flags before committing.

## 3. Multi-Programming Language Parity
The agent must deliver identical engineering rigor across all supported languages:
- TypeScript / JavaScript: Strict types (`noImplicitAny`), JSDoc/TSDoc, ESLint compliance.
- Python: PEP 8 formatting, type hints (`typing.Optional`, `Union`, `Literal`), Google/NumPy style docstrings.
- Go: Standard `godoc` comments on exported symbols, idiomatic error handling (`if err != nil`).
- Rust: Standard rustdoc comments (`///`), exhaustive pattern matching, zero unhandled `unwrap()` in production.
- Solidity: NatSpec comments (`@notice`, `@dev`, `@param`, `@return`) on all smart contract functions.
