# Evidence ledger

The ledger is a compact audit record for capability claims. It is an internal working structure, not a mandatory response format.

## Claim identity

Every capability claim must be bound to:

- `capability_statement`: the behavior being assessed;
- `task_family`: the class of similar problems covered by the claim;
- `scope_limits`: contexts, constraints, or missing evidence that limit the claim;
- `current_state`: no state earned, `emerging`, `repeatable`, or `transfer-evidenced`.

A state without this scope is too broad to be meaningful.

## Attempt record

Create one record for each attempt used as evidence.

| Field | Meaning |
| --- | --- |
| `attempt_id` | A local stable label such as `A1`; do not imply a global identifier. |
| `task` | The concrete problem attempted. |
| `relationship` | `initial`, `similar`, or `adjacent`; use `unknown` when unsupported. |
| `first_attempt_artifact` | A quote, file/path reference, hash, or faithful summary of the user's pre-critique work. |
| `outcome` | What happened, with provenance and uncertainty. |
| `delivery_evidence` | Shipped artifact, test, acceptance, observed result, or external feedback. |
| `capability_evidence` | Target behavior visible in the user's own reasoning or action. |
| `assistance_phase` | `pre_attempt`, `during_attempt`, `post_attempt`, `tool_execution`, `external_feedback`, `none`, or `unknown`. |
| `assistance_source` | `human`, `ai_reasoning`, `ai_tool`, `external_evidence`, or a clear natural-language equivalent. |
| `supplied_target_behavior` | `yes`, `no`, or `unknown`. |
| `assistance_change` | `increased`, `similar`, `reduced`, or `unknown` versus the prior comparable attempt. |
| `isolation` | `clean`, `partial`, `contaminated`, or `unknown` for transfer attempts. |
| `contamination_sources` | Visible prior answers, templates, reminders, hints, coaching, or other leakage. |

Use `unknown` instead of completing missing fields with plausible details.

## Evidence rules

Capability evidence must identify behavior attributable to the user. A final artifact can contain mixed provenance.

Examples:

- The user selected the relevant source while the AI generated the analysis: evidence for source selection, not for independent analysis.
- The user produced a complete first draft and the AI critiqued it afterward: the first draft can support capability evidence.
- The AI supplied a template before the attempt and the user filled it in: record template dependence and avoid claiming independent structure generation.
- A tool executed the user's plan: tool output can support delivery evidence; the plan itself needs separate provenance.

## Transition checks

### No state earned → `emerging`

Require one effective instance where the target behavior is visible in the user's contribution. Disclose assistance. A heavily assisted attempt may qualify only for the portion of behavior that remains attributable to the user.

### `emerging` → `repeatable`

Require another effective instance on a similar task.

Check that:

- the same bounded target behavior is visible in both attempts;
- the second attempt has an identifiable user first attempt;
- assistance did not become more substitutive;
- the comparison uses real attempt records rather than output polish.

Post-attempt critique can remain similar across attempts. Pre-attempt generation of the target behavior blocks repeatability evidence for that behavior.

### `repeatable` → `transfer-evidenced`

Require an adjacent new problem and `clean` transfer isolation.

Check that:

- adjacency is explained;
- prior answers and artifacts were unavailable;
- no solution pattern or hint was supplied before the first attempt;
- the user's first attempt is preserved;
- the target behavior is effective in the new context.

A `partial`, `contaminated`, or `unknown` transfer cannot earn this transition alone.

## Ledger exposure template

When the ledger must be shown, use compact prose or a table. Include:

- delivery goal;
- scoped target capability and task family;
- current earned state;
- relevant attempts;
- delivery evidence;
- capability evidence;
- assistance phase and change;
- transfer isolation, when applicable;
- evidence against the transition;
- capability debt;
- next deliberate challenge.

End a transition proposal by asking the user to verify whether the record of events and assistance is factually accurate. Do not ask them to choose a preferred state.

## Persistence and privacy

Keep the ledger in current context by default. Before any durable write:

1. obtain explicit authorization;
2. use a location or state system selected by the user;
3. store only the approved fields;
4. avoid secrets, personal data, or raw third-party content unless necessary and authorized;
5. preserve project truth as a separate source of record.
