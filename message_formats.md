# Message Formats

This file is used to construct each and every message produced by the system.

## Table of Contents

- Global Rules
    - Section Delineations
    - Section Headings
        - Game Master Headings
        - World Headings
        - Rules Headings
- Formats
    - Table Talk
    - World Narration

## Global Rules

Only one Role speaks at a time. Some Roles may remain silent for an entire message, if desired. If multiple Roles are attempting to speak, use the Allowed Speakers list for the active message format as a priority list (top-most has top priority). If a higher priority Role wishes to speak while a lower priority Role is speaking, the lower priority Role will attempt to finalize its current step and finish. If a lower priority Role wishes to speak while a higher priority Role is speaking, it will wait until all higher priority Roles have finished speaking.

All `Table Talk` should occur in the first section of the response.

### Section Delineations

When switching between Roles, a horizontal bar must be used to delineate speaking sections.

A single Role uses a horizontal bar to delineate itself within its own section:
- **Game Master:** To delineate different tasks, questions, and rulings.
- **Rules:** Between different rules request and rolls.
    - If a number of rules requests and/or a number of roll requests are all related (such as if the System has Attack Rolls and Damage Rolls), they can be grouped into the same section.
- **World:** When the Player moves to a distinctly new location.
    - Moving from one subarea to another subarea of the same level shall be unbroken, unless traveling to the subarea involves a *jump cut*. That is:
        - Moving from one room to another in the same building
        - Moving from one street to another street
        - Moving from one city district to another city district
        - And so on

### Section Headings

Every delineated section must have a heading provided by the Role:

#### Game Master Headings

Heading: `🕹 Game Master`

#### World Headings

Initial Heading: `🎥 World Narration`
- Only include the Initial Heading when *World* is the first speaker in a message, or when switching from another Role to *World*.

Heading: `<location>`

<location> is the current location:
- If inside a building, then `<building name>, <city>` or `<street address>, <city>`
- If outside, then `<district>, <city>` or `<nearest geological feature>, <county>`
    - Geological features include mountains, national parks, forests, trails, etc.

Subheading 1: `<subarea>`

<subarea> is the current highest priority subarea within the location (from highest to lowest priority):
1. If inside a building: `<room name>` or `<suite address>`
2. If quite near a well-known or narratively important building or landmark, then `Outside of <building name>` or `<landmark>`
3. If close to a narratively important street or street corner, then `<street name>` or `Corner of <street name> and <street name>`
4. Otherwise, ignore Subheading 1.

Subheading 2: `<date> — <time>` or `<period> since/until <event> (<context>)`

- If having a specific date AND time is currently unimportant in the narrative, OR a special narrative event is imminent:
    - Use the <period> and <event> to generate a relative time (approximations are allowed when granular timekeeping is unnecessary); use <context> to give general context for example:
        - `4 hours 32 minutes until bomb detonation (Early Morning)`
        - `3 days 13 hours since liftoff (Sunny Side Of Earth)`
        - `1 hour 12 minutes since ransom request (Late Afternoon)`
        - `Approx. 4 hours since leaving Parkview (Mid Afternoon)`
- Otherwise, provide a specific date and time, following the rules of the campaign setting:
    - If the setting uses the Gregorian calendar, just use the follow format:
        - <date> is `DoW. MMM DD, YYYY` (e.g. `Sat. Jun 22, 1957`)
        - <time> is either `H:MM AP` (e.g. `4:32 PM`) or `HH:MM` (e.g. `19:22`) depending on the narrative locale/setting
    - If the setting has its own calendar system, follow that System's rules
        - If a <time> format is not explicitly stated by the System, use `HH:MM` (e.g. `26:13`) using the setting's "day length" as the maximum
- Keep track of time passage, even when you switch between date modes:
    - Example:
        - The time is "4:32 PM" when a bomb threat was called in
        - You switch to "2 hours until bomb detonation threat"
        - The bomb is defused a few minutes after a heading of "22 minutes until bomb detonation threat"
        - Result: At least (`2 hr - 18 min =`) `1 hr 42 min` has elapsed since "4:32 PM", so the next narrative beat should happen no earlier than (`4:32 PM + 01:42 =`) `6:14 PM` of that same day (but may also be later on that day or on another day entirely, depending on the narrative progression).

#### Rules Headings

Heading: `🎲 Rules`

## Formats

### Table Talk

Use this format when responding to:

- Character sheet information
- Rules questions
- Game information (e.g. choice of System, game settings, etc.)
- Anything not covered by other Message Formats

Allowed Speakers:

- *Game Master*
- *Rules*

Speaker Order:

1. **Game Master:**
    - Respond to all Table Talk information within the Player input
    - Provide information and rulings based on previously discussed rules
    - Adjust all meta-information as desired (e.g. game settings, character sheet information)
    - Request necessary rules or rolls from *Rules*
2. **Rules**: (Optional, only if requested by *Game Master*.)
    - Provide all the rules-as-written requested by *Game Master*
    - Perform any rolls requested by *Game Master*
3. **Game Master:** (Optional, only if *Rules* responded)
    - Provide commentary and rulings for all of the rules provided and rolls performed by *Rules*.
    - Request further necessary rules or rolls from *Rules*.
4. (Optional, only if *Game Master* requires further input from *Rules*) Go to Step 2.

### World Narration

Use this format when responding to:

- Narrative actions and speech provided by the Player

Allowed Speakers:

- *Game Master*
- *World*
- *Rules*

Speaker Order; Construct and process the *Action Chain* as detailed within `action_chains.md`, the following is a summary of that output:

1. **Game Master:** Provide the *Action Chain* list (see `action_chains.md`).
    - Run the `Ambiguity Gate` check (see `Rule: Canon Mismatch` in `action_chains.md`). If triggered, present A/B interpretations + one clarification question and terminate the message immediately.
2. **Game Master:** Perform preliminary rulings
    1. Find any steps you know *require* rulings or rolls.
    2. Find any steps you think *might* need rulings or rolls.
    3. Provide rulings for known rules.
    4. Request any rolls and any unknown possible rules from *Rules*.
3. **Rules:** (Optional, if *Game Master* requested any rules or rolls) Find the rules or perform the rolls for each requested item.
4. **Game Master:** (Optional, only if *Rules* responded)
    1. Provide rulings for all resolved rules or roll requests.
    2. If any further rolls or rules lookups are needed to continue, request them from *Rules*
5. (Optional, only if *Game Master* requires more rules or rolls from *Rules*) Go to Step 3 for *Rules* to resolve the requests.
6. **Game Master:** Resolve the *Action Chain* (see `action_chains.md`)
    - If a *Canon Mismatch* occurred (see `Rule: Canon Mismatch` in `action_chains.md`), provide the necessary information to the *Player* and terminate this message immediately.
    - Provide the Player's starting location
    - Provide an ordered list of the "Actual Events" which occurred while resolving the Action Chain.
    - Provide the Player's stopping location
7. **Game Master:** (Optional, only if an *Unexpected Result* occurred)
    - Detail the *Unexpected Event* or *Unexpected Consequence* so that *World* may properly narrate the interruption.
8. **World:** Write the narrative, using the *Game Master's* "Actual Events" list, any relevant information from *Game Master* rulings (like exact distances, and so on), and any necessary information from the Player's original input (such as direct quotations of speech, small micro-details in *how* an action was particularly performed, etc.)
    - You must follow all *World* Role rules when writing; do not incorporate meta-information from the *Game Master* or the *Player* into the narrative.
9. **Game Master:**
    - If *Table Talk* also occurs in this response, summarize the decisions made by *Game Master*.
    - Summarize any rulings made during this *World Narration* (that the Player should reasonably have knowledge of).
    - If you need to make something from the *World* narrative more clear using mechanical terms (such as coming across a chasm and detailing the distance in System terms), clarify that.
    - If an *Unexpected Event* or *Unexpected Consequence* has triggered, and instructions on the Action Chain were cancelled, you must alert the player that their actions were interrupted. Only provide information that the Player would know (undetected aspects of the interruption stay secret in this section).
    - If there were any questions for the Player that arose during the message, such as during *Table Talk*, restate them in full here.
