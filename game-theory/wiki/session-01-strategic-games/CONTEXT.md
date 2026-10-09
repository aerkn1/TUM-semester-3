# Ubiquitous Language: Session 1 Strategic Games

Source note: [session-01-strategic-games.md](session-01-strategic-games.md)  
Discovery source: `game-theory/raw/GT Slides 01.pdf`  
Provenance: Definitions and notation below are **local** to Session 1 unless marked **enriched** for a clarifying example or wording. No external course policy is inferred here.

## Model language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Player (`i∈N`)** | A decision maker represented in the model. `N` is the finite player set. [local] | participant when it hides who chooses |
| **Action set (`A_i`)** | All actions available to Player `i`; nonempty, finite or infinite. [local] | outcome set |
| **Action (`a_i`)** | One choice made by Player `i`. In Cournot it is a quantity. [local] | strategy when it obscures simultaneous action notation |
| **Action profile (`a∈A`)** | One chosen action for every player, with `A=∏_i A_i`. [local] | one player's move |
| **Opponents' profile (`a_-i`)** | All players' actions except `i`'s, held fixed in a unilateral-deviation test. [local] | the other payoff |
| **Payoff function (`u_i:A→ℝ`)** | Assigns Player `i`'s utility/payoff to a complete action profile. [local] | market payoff or total payoff when player-specific |
| **Strategic game** | The triple of players, action sets, and player-specific payoff functions. [local] | payoff matrix alone when action sets are unstated |
| **Finite game** | Every player's action set is finite. [local] | game with finitely many players only |

In a two-player matrix, the **row player** is Player 1 and the **column player** is Player 2; `(x,y)` lists their payoffs in that order. A high number is better for that player, including when all numbers are negative.

## Choice and solution language

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Unilateral deviation** | One player changes their own action while everyone else's action stays fixed. [local] | any alternative outcome |
| **Best response (`B_i(a_-i)`)** | The set of all actions maximizing Player `i`'s payoff against fixed `a_-i`. [local] | one best move if a tie is possible |
| **Best-response correspondence (`B_i`)** | A set-valued mapping from opponents' profiles to best-response sets, `B_i:A_-i→P(A_i)`. [local] | best-response function unless singleton everywhere |
| **Best-response function (`b_i`)** | The unique best action for every possible opponents' profile, when every best-response set is a singleton. [local] | correspondence in a tie case |
| **Power set (`P(Y)`)** | The set of all subsets of `Y`, including the empty set. [local] | set of players |
| **Pure Nash equilibrium (`a*`)** | Every chosen action is a best response to the other chosen actions; no player gains from a unilateral deviation. [local] | socially best outcome; dominant strategy |
| **Strictly dominant action** | An action that gives a strictly higher payoff than any alternative for every opponents' action profile. [enriched, used to explain Prisoner's Dilemma] | equilibrium action in all games |
| **Pareto improvement** | A change of profile that makes at least one player strictly better off and none worse off. [enriched equivalent formulation] | increase in total payoff alone |
| **Pareto efficient profile** | No other feasible profile is a Pareto improvement. It need not be a Nash equilibrium. [local] | stable profile |

The Nash test is `u_i(a*_-i,a*_i) ≥ u_i(a*_-i,a_i)` for **all** players and feasible deviations. The best-response form is `a*_i∈B_i(a*_-i)` for **all** players. The inequality permits ties; it does not require strict improvement to rule out an equilibrium.

A correspondence can be multivalued or empty. Example of two best responses: if Player 1 earns payoff 1 from both Head and Tail against a fixed Player 2 action, both are in `B_1`. Example of no maximum: `A_i=(0,1)` with payoff `u_i(a_i)=a_i` has no best response because 1 is excluded and any feasible number can be improved. [enriched examples]

## Utility and interpretation

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Ordinal utility** | Represents preference ranking; a strictly increasing transformation preserves that ranking. [local] | cardinal payoff size as an absolute fact |
| **Positive affine transformation** | `v_i=α_i u_i+β_i` with `α_i>0`; preserves expected-utility representation and strategic comparisons. Adding 4 to each Prisoner's Dilemma payoff is the slide's example. [local with notation enriched] | arbitrary nonlinear transformation for expected utility |
| **Rationality assumption** | In this lecture, complete/transitive preferences, utility representation, expected-utility maximization, and strong use of available knowledge. [local] | a verified description of actual human behavior |
| **Solution concept** | A rule for selecting or assessing outcomes, such as Nash equilibrium. [local] | efficiency criterion |

## Cournot notation and formula intuition

| Term | Definition | Aliases to avoid |
|---|---|---|
| **Firm quantity (`q_i`)** | Units of output supplied by Firm `i`, constrained to `q_i≥0`. [local] | price |
| **Rival quantity (`q_-i`)** | Output from the other firm, fixed while Firm `i` optimizes. [local] | total quantity |
| **Total quantity (`Q`)** | `q_1+q_2`; determines price. [local] | a firm's output |
| **Unit cost (`c`)** | Constant cost per unit of output; source assumes `0<c<1`. [local] | total cost |
| **Market price (`p(Q)`)** | `max(0,1-Q)`; cannot go below zero. [local] | profit margin |
| **Profit/payoff (`u_i`)** | `(p(Q)-c)q_i`; per-unit margin times own units. [local] | revenue `(pQ)` |
| **Cournot best response (`b_i`)** | `max{0,(1-c-q_-i)/2}`; own profit-maximizing output given rival output. [local] | equilibrium quantity before solving both firms |
| **Symmetric Cournot equilibrium** | Each firm supplies `(1-c)/3`, a mutual best response. [local] | cooperative quantity |
| **Equal-output Pareto benchmark** | Each firm supplies `(1-c)/4`, the symmetric benchmark on the slide. It improves both firms' profits relative to Cournot but invites unilateral expansion. [local, explanation enriched] | Nash quantity |

**Units and signs:** `q` is output units; `p` and `c` are currency per unit in an applied interpretation; `u_i` is currency profit. The slides use normalized values, so no currency unit is specified. The derivative `1-c-q_-i-2q_i=0` identifies an unconstrained interior optimum; the outer `max{0,...}` enforces nonnegative quantity.

```mermaid
flowchart LR
    Q[Two firms choose q_i] --> T[Total Q=q_1+q_2]
    T --> P[Price p=max(0,1-Q)]
    P --> U[Profit u_i=(p-c)q_i]
    U --> B[Best response b_i]
    B --> N[Mutual responses: Nash]
    N --> W[Compare with equal-output Pareto benchmark]
```

## Example dialogue

> **Student:** “Both firms would earn more at `(1-c)/4`. Is that the Nash equilibrium?”  
> **Coach:** “That is the **equal-output Pareto benchmark**. Hold the rival at `(1-c)/4` and calculate your **best response**. It is `3(1-c)/8`, which is larger, so the benchmark is not Nash.”  
> **Student:** “Then why is `(1-c)/3` Nash?”  
> **Coach:** “At that profile, each quantity equals its own best response to the rival's quantity. Neither firm gains by changing alone.”

## Flagged ambiguities and exam correction rules

- Use **action** for the selected element of `A_i` and **profile** for the complete tuple. Some literature uses “strategy” in normal-form games; follow the lecturer's notation when solving.
- Use **no pure Nash equilibrium** for Matching Pennies. The slides' future mixed-equilibrium topic means “no equilibrium at all” is too broad.
- Use **best-response correspondence** when a tie or missing maximizer is possible; use **function** only when the response is unique everywhere.
- Check **Nash** with unilateral deviations and **Pareto** with feasible joint comparisons. One does not imply the other.
- In Cournot, solve each firm's optimization with `q_-i` fixed, then solve the two response equations and check `q_i≥0` and the price branch.
- Distinguish **ordinal** ranking invariance under strictly increasing transformations from the **positive affine** expected-utility claim.
