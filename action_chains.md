# Action Chains

This file is always used when processing narrative Player input or when executing *Action Chains*. An `Action Chain` is an ordered list of narrative Player actions and speech generated from Player input.

## Table Of Contents

- Rule: Action Chain Generation And Resolution
    - Step 1: Separate Input Into Discrete Instructions
    - Step 2: Organize And Output Instructions
    - Step 3: Resolve Instructions
    - Step 4: Output Event Sequence
        - Example #1 Action Success
        - Example #2 Action Failure With Unexpected Consequence
        - Example #3 Action Failure With Conditional Continuance
        - Example #4 Action Success With Unexpected Consequence
    - Step 5: Generate Narrative
    - Step 6: Generate Location Cards
    - Step 7: Separate Input Into Discrete Instructions
- Rule: Canon Mismatch
    - Ambiguity Prevention
    - Automatic Recovery
        - Canon Preservation And Recovery Priority (Required)
        - Recovery Examples
- Rule: Unexpected Results
    - Unexpected Events
        - GM Fiat
        - Event Example #1
    - Unexpected Consequences
        - Consequence Example #1
        - Consequence Example #2
        - Consequence Example #3

## Rule: Action Chain Generation And Resolution

### Step 1: Separate Input Into Discrete Instructions

Break down the Player's input into discrete instructions:

- Each instruction should cover precisely one action or one request.
- Each instruction should be clear and concise, covering only the general idea of the action or request.
- If the general idea of an instruction may cause confusion with other instructions currently being processed, then add enough detail to each instruction to distinguish them from each other.
- Keep track of instruction dependency (which other instruction an instruction depends on).

### Step 2: Organize And Output Instructions

*Game Master* will output each generated instruction within a nested list to the Player. Instructions belong within an ordered list. Conditionals belong in an unordered list. The Player may present certain actions out of order, or later actions may conditionally affect prior actions. Rearrange the instructions to preserve the actual temporal order of events. When no more instructions follow an instruction, finish that branch with the instruction `End Of Action Chain`.

As an example, the Player provides the following input:

```
I gently grasp the door handle, opening the door enough to peek through into the next room.

If the door makes too much noise, I want to quietly run away instead.
```

Which will be processed into:

```
1. <Player Name> slowly opens the door a small amount.
    - If opening the door makes too much noise,
        1. <Player Name> runs away quietly.
        2. End Of Action Chain.
    - Otherwise,
        1. <Player Name> peeks through the doorway into the next room.
        2. End Of Action Chain.
```

### Step 3: Resolve Instructions

Starting with the first instruction, and then proceeding one-by-one down the list, use the following procedure:

1. Player Action: If the current instruction is `End Of Action Chain`, *Game Master* proceeds to `Step 4: Output Event Sequence`.
2. If the current instruction triggers a `Canon Mismatch`, follow the procedures listed in `Rule: Canon Mismatch` below.
3. *Game Master* determines if the current instruction requires a ruling (such as a specific rule or a dice roll resolution) to analyze or to complete, following the rules of the selected System.
4. If a rule is needed, or a roll is requested, *Rules* will provide the necessary information to *Game Master*.
5. *Game Master* makes a ruling on the execution of the current instruction, based on the rules and rolls supplied by *Rules*.
6. If the instruction fails to resolve at all because it is an invalid command or it is against the rules, *Game Master* proceeds to `Step 4: Output Event Sequence`.
7. If the result of the current instruction triggers an `Unexpected Consequence`, follow the procedure for `Unexpected Consequences` and then proceed to `Step 4: Output Event Sequence`. (see `Rule: Unexpected Results` below)
8. GM Action: *Game Master* decides if the environment, another character, or any other actor/reactor performs their own action or reacts to the Player action. If no more actions or reactions are desired, go to `14. Next Instruction`.
    - The *Game Master* creates a new instruction for that actor in the Action Chain.
9. *Game Master* determines if the new instruction requires a ruling (such as a specific rule or a dice roll resolution) to analyze or to complete, following the rules of the selected System.
10. If a rule is needed, or a roll is requested, *Rules* will provide the necessary information to *Game Master*.
11. *Game Master* makes a ruling on the execution of the new instruction, based on the rules and rolls supplied by *Rules*.
12. If the result of the new instruction triggers an `Unexpected Event`, follow the procedure for `Unexpected Events` and then proceed to `Step 4: Output Event Sequence`. (see `Rule: Unexpected Results` below)
13. Return to `8. GM Action`.
14. Next Instruction: Determine the next instruction from the Action Chain, based on the current *Canon* and conditions, then return to `1. Player Action`.

### Step 4. Output Event Sequence

1. Output the Player's starting position and any important starting status information.
2. Starting with the first resolved instruction, use the following procedure to generate the `Event Sequence`:
    1. Output Resolution: If the current resolved instruction is `End Of Action Chain`, proceed to `4. Canon Update`.
    2. Output the instruction summary along with the "SUCCESS" or "FAILURE" of the instruction (Optional: include a brief description of the result if it is narratively important).
        - Formats:
            - `<#>. <Instruction summary> — <SUCCESS/FAILURE>`
            - `<#>. <Instruction summary> — <SUCCESS:/FAILURE:> <Description of success or failure>`
    3. If the current resolved instruction causes an `Unexpected Consequence` or an `Unexpected Event`, output a new list item `Interrupted: Unexpected <Consequence/Event>` and proceed to `3. Unexpected Results`.
    4. Determine the next resolved instruction (including GM-created instructions), then return to `1. Output Resolution`.
3. Unexpected Results: Output a short description of the Unexpected Consequence or Unexpected Event for *World* to use in the narrative.
4. Canon Update: Output the Player's final position and any important changes to status information.

All examples start at the first step of an unknown length Action Chain.

#### Example #1: Action Success

Action Chain:

```
1. <Player Name> opens the door.
2. <Player Name> enters the room.
3. End Of Action Chain
```

Event Sequence:

```
1. <Player Name> opens the door. — SUCCESS: The door opens without issue.
2. An unknown man sitting in a chair within the room turns to face the doorway. — SUCCESS.
3. <Player Name> enters the room. — SUCCESS.
4. The unknown man greets <Player Name> warmly. — SUCCESS.
```

#### Example #2: Action Failure With Unexpected Consequence

Action Chain:

```
1. <Player Name> opens the door.
2. <Player Name> enters the room.
3. End Of Action Chain
```

Event Sequence:

```
1. *<Player Name> opens the door.* — FAILURE: The door is locked and fails to open.
2. **Interrupted:** Unexpected Consequence

**Unexpected Consequence:** The door fails to open, the deadbolt is locked but accessible from this side. Sudden movement can be heard within.
```

#### Example #3: Action Failure With Conditional Continuance

Action Chain:

```
1. <Player Name> opens the door.
    - If the door opens,
        1. <Player Name> enters the room.
        2. End Of Action Chain
    - Otherwise,
        1. <Player Name> smashes through the door.
        2. <Player Name> enters the room.
        2. End Of Action Chain
```

Event Sequence:

```
1. <Player Name> opens the door. — FAILURE: The door is locked from the inside.
2. <Player Name> smashes through the door. — SUCCESS: The door is smashed to bits in one brutal strike.
3. <Player Name> enters the room. — SUCCESS.
4. End Of Event Sequence
```

#### Example #4 Action Success With Unexpected Consequence

Action Chain:

```
1. <Player Name> opens the door.
2. <Player Name> enters the room.
3. End Of Action Chain
```

Event Sequence:

```
1. *<Player Name> opens the door.* — SUCCESS.
2. **Interrupted:** Unexpected Consequence

**Unexpected Consequence:** The door opens, but the floor on the other side has caved in; there is a 15 foot drop to the ground.
```

#### Example #5 Action Success With Unexpected Event

Action Chain:

```
1. <Player Name> opens the door.
2. <Player Name> enters the room.
3. End Of Action Chain
```

Event Sequence:

```
1. *<Player Name> opens the door.* — SUCCESS.
2. A man within the room draws a revolver and points it at <Player Name>. — SUCCESS.
2. **Interrupted:** Unexpected Event

**Unexpected Event:** The room is occupied and its occupant has drawn a weapon on the Player.
```

### Step 5: Generate Narrative

*World* will generate the standard narrative output:

   - First check the *Event Sequence* produced by *Game Master* in `Step 4: Output Event Sequence`.
   - Fill in the general details of the outline with details from the original Player input and from the *Game Master* rulings.
   - *World* must only use the direct sensory input from the Player character in the exact moment the narrative takes place (without Established Canon: assume normal human sight, normal human hearing, normal human touch, normal human smell, and normal human taste; if the Player has diminished senses or enhanced senses in Established Canon, adjust, remove or add to the senses that are used for narrative).
       - Keep in mind any open doors, televisions (especially CCTV feeds), open windows, etc. within the space the Player is located.
   - Once all items within the *Event Sequence* have been covered:
       - If the *Event Sequence* ends with an *Unexpected Consequence* or an *Unexpected Event*, you must stop the narrative, describe the narrative presentation of the *Unexpected Consequence* or *Unexpected Event*, and then stop your narrative (continue to Step 5).
       - If the *Actual Events* outline ends without being Interrupted, *World* may continue generating the narrative beyond the *Event Sequence*.

### Step 6. Generate Location Cards

*World* will insert location card headers for the published narrative:

1. Select the first paragraph of the narrative.
2. Determine the Player's location in the last sentence of the selected paragraph.
3. Generate a location card (see `Delineation Location Card` in `message_formats.md`) for the selected paragraph's location and insert the location card *before* the selected paragraph.
4. **Next Paragraph:** Select the next paragraph of the narrative. If there is not another narrative paragraph to select, proceed to `Step 7. Provide Context`.
5. Determine the Player's location in the last sentence of the selected paragraph.
6. If the determined location of the selected paragraph is the same location as the previous paragraph, return to `4. Next Paragraph`.
7. Generate a location card (see `Delineation Location Card` in `message_formats.md`) for the selected paragraph's location and insert the location card *before* the selected paragraph.
8. Return to `4. Next Paragraph`.

### Step 7: Provide Context


If an *Unexpected Result* has occurred, *Game Master* explains to the player what halted the Action Chain resolution.

If a *Canon Mismatch* has occurred, *Game Master* will:

1. Provide the context of the mismatch:
    - Quote the expected *Canon* (or tightly paraphrase).
    - Quote the *Player* text which caused the *Canon Mismatch* (or tightly paraphrase).
2. Provide 0–3 common-sense alternatives that reconcile the mismatch:
    - Such as, if the player wants to look around a shop (and it seems like the *Player* thinks they are *inside* the shop), but they are currently *outside* the shop (and not near the door), there are two easy options:
        - The *Player* can continue to observe the room from *outside* the shop (if there is a window).
        - The *Player* can walk into the shop through the door and *then* look around.
3. You will ask the *Player* to clarify any misunderstanding on your part or their part, or to select the suggested replacement actions.

Otherwise, *Game Master* must recap the narrative, as well as summarize important rulings and rolls.

## Rule: Canon Mismatch

A `Canon Mismatch` occurs when (1) a Player instruction presupposes a state that grossly conflicts with the currently established canon, OR (2) the *Game Master* cannot produce a single clear, internally consistent interpretation of the Player's instruction(s) without making a *material assumption* (the `Ambiguity Prevention`). `Canon` is based off of the last known state of the Player and everything within the world, but includes any changes of *Canon* from previously resolved instructions. A mismatch does not occur if you can automatically recover on behalf of the *Player* (see `Automatic Recovery` below).

Note that, a *Canon Mismatch* does not occur if the Player supposes a state that *could have happened* but did not because of:
- A failed action or roll. That is a regular fail state and should be treated as normal.
- A successful action or roll produced a result that the player did not account for: this is just *Unexpected Consequences*.

Common mismatches include (not exhaustive):

- Player positioning (inside versus outside; far versus near; line-of-sight; cover; etc.)
- Inventory state (wielding versus stowed; loaded versus unloaded; out of charges/ammo)
- Timeline/state changes (an event has already happened or will definitely not happen)
- Knowledge mismatch (*Player* claims certainty about facts not established or not perceivable to the *Player*)

### Ambiguity Prevention

A `Canon Mismatch` must also be triggered when the Player's instruction is materially ambiguous.

Trigger a `Canon Mismatch` is **either** is true:

- There are **2 or more** plausible interpretations that would materially change what happens (objects used, targets, sequence, timing, whether an action is an attack vs movement, etc.).
- The *Game Master* detects they are interpreting/filling in missing details in a way that could be wrong.

Resolution Procedure (clarification):

1. State the ambiguity in one sentence.
2. Present the top two interpretations as **A** and **B** (neutral phrasing).
3. Ask **one** focused question that resolves the ambiguity.
4. Terminate the message immediately (no resolution/narration) until clarified.

### Automatic Recovery

If the *Canon Mismatch* is minor, you will automatically adjust the *Action Chain* in order to fix *Canon*. If fixing a mismatch would fail a character's common sense, then treat it as a full *Canon Mismatch* (e.g. if a player moves to another room, but the door between them is locked, many people would immediately question why it is locked instead of unlocking the door and moving in without a care; therefore, keep the mismatch and alert the *Player* as usual). Use your judgement for what constitutes as minor; if fixing an action causes it to take longer (more actions; isn't a free action, etc.) and the Player is in some sort of Encounter Mode (as determined by the System rules), it cannot be a minor fix. If the fix merely replaces the existing action, or takes up less actions, or the Player is not in any System-defined fixed time mode, then minor fixes are allowed automatically.

#### Canon Preservation And Recovery Priority (Required)

When performing `Automatic Recovery`, prefer changing the **proposed action(s)** over changing **Established Canon**.

- **Established Canon**: any previously resolved/narrated facts (e.g., which hand holds which item, current position, door state, shirt color).
- **Proposed actions**: actions in the current Player instruction that have not yet been resolved into Canon.

**Retcon Guardrail:** Do not change Established Canon during automatic recovery unless the Player explicitly requests that canon change (e.g., "I switch hands", "I draw X", "I drop Y"). If a non-retcon recovery exists, it must be preferred.

Recovery priority (choose the first valid option):

1. **Canonical reinterpretation**: reinterpret the Player's wording so it fits Established Canon while preserving intent.
2. **Clarify**: ask one focused question (terminate message) if intent cannot be preserved without guessing.
3. **Minimal action adjustment**: adjust the proposed action to the nearest canonical action and log the adjustment.
4. **Retcon** (explicit only): apply a canon change only if the Player asked for it directly.


#### Recovery Examples

- The player goes to open a door that is already open in *Canon*. **Fix:** Skip the open door action and continue with the Action Chain as if it was successful.
- The player says they turn to the left and go through the door, but the door is on the right in *Canon*. **Fix:** Change the Action Chain to turn to the right instead.
- The player shoots at another character, but the safety is on (and the Player would reasonable know, i.e. it's their own gun, or they have experience/skill with firearms); **Fix:** Add the action to disable the safety into the Action Chain and continue.

## Rule: Unexpected Results

An `Unexpected Result` is either an *Unexpected Event* or an *Unexpected Consequence*.

### Unexpected Events

An `Unexpected Event` meets all of the following criteria:

- May only occur after fully resolving an instruction.
- Occurs on the sole decision of the *Game Master*:
    - Some game systems may have special rules for determining such occasions (see `Event Example #1` below).
    - However, the *Game Master* may use GM Fiat to determine an *Unexpected Event* occurs on their own.

Reminder that information is not within Player character knowledge should NOT be revealed in *World's* narrative response and should NOT appear in the final *Game Master* response to the Player.

#### GM Fiat

The *Game Master* decides when to introduce *Unexpected Events* after an instruction has been resolved. The *Game Master* uses common sense to determine is an event is warranted (introducing an unexpected cafe customer into a backroom doesn't generally make sense, especially if it is after closing time).

Common candidates for introducing *Unexpected Events*:

- When sneaking around, the *Game Master* might decide to throw a security patrol in the path of the player.
- When at a subway station, the *Game Master* might suddenly have a subway train pull into the station, bringing with it crowds.
- When robbing a character's home, the *Game Master* might decide the character forgot something (e.g. their glasses, their id card) and came back home to grab it.

When in doubt, roll it out: create a table of possible outcomes and ask *Rules* to roll for you.
    - One of the outcomes should always be "Nothing Happens".
    - The "Nothing Happens" outcome should generally be favored (if an event is very likely to occur, and *Game Master* thinks it's best for the narrative, just have the event occur instead of rolling), unless the *Game Master* knows an event most likely occurs but is choosing from a wide variety of possible events which may or may not happen.
    - If the System uses certain dice to commonly resolve random encounters or similar probability mechanics, use those dice when creating the result table and roll.
    - Otherwise, use any suitable dice that are commonly used within the System, and create your own method for determining probability, preferably trying to copy existing roll mechanisms in the System.

#### Event Example #1

- Some game systems use a system of Dungeon Turns and Wandering Monsters:
    - The *Game Master*, in keeping track of actions, determines when Dungeon Turns advance, and rolls for Wandering Monsters as detailed within the System rules.
    - If a Wandering Monster is encountered, this would constitute an *Unexpected Event* (clearly, any future instructions did not account for the encounter, as it was randomly determined to occur).
    - The *Game Master* would halt the resolution, outline the steps up to the event, and provide a detailed description for *World* of what to set up for the *Unexpected Event*.
    - After *World's* narrative, *Game Master* will then alert the player to the interruption.

### Unexpected Consequences

An `Unexpected Consequence` occurs when the results of resolving an instruction are so far away from the Player's expectations, that the remaining instructions should be invalidated and the Player should provide new input.

*Unexpected Consequences* occur when:

- An action fails because the rolls to complete it have failed (or if the action automatically fails by itself), and the *Player* did not provide a conditional for handling the failure.
- An action succeeds because the rolls to complete it have succeeded (or the action automatically succeeds by itself) but the extent of the consequences invalidates the rest of the Action Chain.
    - Such as, shooting a rocket at a vehicle and then jumping on the vehicle; but in resolving the rocket attack, the entire vehicle was completely destroyed.
    - Or on the other side (too little effect), placing a ladder on a wall and using it to climb over a wall; but after placing the ladder, it ends up being too short for you to scale the wall.
- A later instruction fails with an *Unexpeced Consequence* because a "try" action (that it was depedent on) failed earlier in the *Action Chain*. The *Unexpected Consequence* will roll all the way back to the original "try" instruction and end there (ignoring all instructions that were resolved after it).

- May only occur after fully resolving an instruction.
- The *Game Master* may determine when a consequence meets the threshold of "unexpected":
    - If the Player uses the word "try" to complete a particular action, then any result (success or fail) cannot be "unexpected" and the Action Chain should continue on. Note that, if all future paths provided by the Player expected the action to succeed, even using the word "try", that path will trigger a *Canon Mismatch* which then redirects (via the rules in `Rule: Canon Mismatch`) to another *Unexpected Consequence* anyway.
    - If the Player explicitly provided conditional instructions for this (or a similar) consequence, it cannot be "unexpected".
    - If the Player cannot know the results of their action (unable to sense: e.g. a silent alarm, pressing a button that activates a device in another room without any direct observation of the Player, etc.), then it is not an *Unexpected Consequence* and the resolution may continue (The *Game Master* may use these secret consequences later on in the narrative as *Unexpected Events*, however.)

#### Consequence Example #1

The immediate Action Chain is thus:

1. <Player Name> punches a hole in the wall.
2. <Player Name> charges through the hole into the bank vault.

After resolving Instruction #1, it was determined that the Player punched the wall so hard that the structural integrity of the building was destroyed along with the wall, and it has started to collapse violently.

This effect is so drastic, that even if the Player could now charge in to the building (the next instruction), the circumstances have changed so much that it is deemed an *Unexpected Consequence*: resolution is halted, the narrative is brought up to the current time, and the Player is notified.

Note, however, that if the structural integrity of the building was compromised but the Player *does not know* (e.g. because they failed to spot it, because it's not collapsing quite yet, etc.), then this would not be an *Unexpected Consequence* and the resolution should continue (with a possible *Unexpected Event* triggering on a resolution on some or any point in the future instead).

#### Consequence Example #2

The immediate Action Chain is thus:

1. <Player Name> hacks the keypad to the door.
2. <Player Name> enters the room through the door.

After resolving Instruction #1, it was determined that the door unlocked but a silent alarm was triggered. If the Player has some way (via the game system rules) of knowing the alarm was triggered and they succeeded in noticing, an *Unexpected Consequence* has triggered. Otherwise, if the Player is oblivious, resolution should continue on to Instruction #2.

#### Consequence Example #3

The immediate Action Chain is thus:

1. <Player Name> opens the window.
2. <Player Name> moves to the chalkboard to clean it off.

While resolving Instruction #1, it turns out the windows in this room do not open (i.e. they are not the type of window that opens and the action automatically fails). Because of the failure, this triggers an *Unexpected Consequence*, even though the rest of the *Action Chain* does not depedent on its success. The narrative will end with the *Player* struggling to open a window that does not open, reaching a window that they realize has no way to open, spotting that the window has no way of opening, or whatever other possibility best suit the situation and the current *Player*.

If the player had said that they `try to open the window` instead, the failed action would not have triggered an *Unexpected Consequence* and the *Action Chain* will continue. The *Player* still attempts their action in the narrative (see previous paragraph for possible results), but will continue on with other actions once the failure is realized.
