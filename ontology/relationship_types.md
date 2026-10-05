# Relationship Types

Allowed values in the `relationships` block of claim cards.

- `supports` — this claim provides additional evidence for the linked claim
- `qualifies` — this claim limits, refines, or adds a boundary condition to the linked claim
- `contradicts` — this claim presents evidence against the linked claim
- `depends_on` — this claim is only valid if the linked claim is also true (precondition)

## Usage

In a claim card frontmatter:

```yaml
relationships:
  supports: [claim-0003]
  qualifies: [claim-0007]
  contradicts: []
  depends_on: [claim-0002]
```

Relationships are directional. If claim-0005 supports claim-0003, record that in claim-0005. You do not need to add a reciprocal entry in claim-0003, though you may add a `supported_by` note in prose if useful.
