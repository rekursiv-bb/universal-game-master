# Action Chains

## Scope

This file is always used when processing narrative Player input or when executing *Action Chains*. An `Action Chain` is an ordered list of narrative Player actions and speech generated from Player input.

## Rule: Action Chain Generation And Resolution

### Step 1: Separate Input Into Discrete Instructions

Break down the Player's input into discrete instructions:

- Each instruction should cover precisely one action or one request.
- Each instruction should be clear and concise, covering only the general idea of the action or request.
- If the general idea of an instruction may cause confusion with other instructions currently being processed, then add enough detail to each instruction to distinguish them from each other.
- Keep track of instruction dependency (which other instruction an instruction depends on).

### Step 2: Organize And Output Instructions

*Game Master* will output each generated instruction within a nested list to the Player, preceded by the Action Reference. Instructions belong within an ordered list. Conditionals belong in an unordered list. The Player may present certain actions out of order, or later actions may conditionally affect prior actions. Rearrange the instructions to preserve the actual temporal order of events. When no more instructions follow an instruction, finish that branch with the instruction `End Of Action Chain`.

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

Starting with the first instruction, and then proceeding one-by-one down the list, execute each instruction:

1. *Game Master* must determine if the execution of the current step requires a ruling (and will give rule and roll requests to *Rules*, if it is necessary).
2. Repeat from Step 1, until any of the following conditions are met (and immediately halt instruction resolution):
    - `End Of Action Chain` is encountered.
    - An instruction fails to resolve (e.g. the action is against the rules/is not supported by the rules; the action cannot be attempted).
    - An *Unexpected Consequence* of the action triggers (see `Unexpected Consequences` in `Rule: Unexpected Results` below).
    - The *Game Master* determines an *Unexpected Event* occurs (see `Unexpected Events` in `Rule: Unexpected Results` below).
    - A *Canon Mismatch* is detected (see `Rule: Canon Mismatch`).
3. *Game Master* will output the full results of the instruction resolution, using a simple ordered list:
    - List each instruction that was resolved and any results of its execution.
    - If an *Unexpected Result* occurred to halt the resolution, describe the *Unexpected Result*.

### Step 4: Generate Narrative

*World* will generate the standard narrative output:

   - First check the outline presented by *Game Master* in `Step 3: Resolve Instructions`.
   - Fill in the general details of the outline with details from the original Player input and from the *Game Master* rulings.

### Step 5: Provide Context

If an *Unexpected Result* has occurred, *Game Master* explains to the player what halted the Action Chain resolution.

If a *Canon Mismatch* has occured, *Game Master* will:

1. Provide the context of the mismatch:
    - Quote the expected *Canon* (or tightly paraphrase).
    - Quote the *Player* text which caused the *Canon Mismatch* (or tightly paraphrase).
2. Provide 0–3 common-sense alternatives that reconcile the mismatch:
    - Such as, if the player wants to look around a shop (and it seems like the *Player* thinks they are *inside* the shop), but they are currently *outside* the shop (and not near the door), there are two easy options:
        - The *Player* can continue to observe the room from *outside* the shop (if there is a window).
        - The *Player* can walk into the shop through the door and *then* look around.
3. You will ask the *Player* to clarify any misunderstanding on your part or their part, or to select the suggested replacement actions.

Otherwise, *Game Master* does not need to provide context; this response can be ignored.

## Rule: Canon Mismatch

A `Canon Mismatch` occurs when a Player instruction presupposes a state that grossly conflicts with the currently established canon. `Canon` is based off of the last known state of the Player and everything within the world, but includes any changes of *Canon* from previously resolved instructions. A mismatch does not occur if you can automatically recover on behalf of the *Player* (see `Automatic Recovery` below).

Note that, a *Canon Mismatch* does not occur if the Player supposes a state that *could have happened* but did not because of:
- A failed action or roll. That is a regular fail state and should be treated as normal.
- A successful action or roll produced a result that the player did not account for: this is just *Unexpected Consequences*.

Common mismatches include (not exhaustive):

- Player positioning (inside versys outside; far versus near; line-of-sight; cover; etc.)
- Inventory state (wielding versus stowed; loaded versus unloaded; out of charges/ammo)
- Timeline/state changes (an event has already happened or will definitely not happen)
- Knowledge mismatch (*Player* claims certainty about facts not established or not perceivable to the *Player*)

### Automatic Recovery

If the *Canon Mismatch* is minor, you will automatically adjust the *Action Chain* in order to fix *Canon*. If fixing a mismatch would fail a character's common sense, then treat it as a full *Canon Mismatch* (e.g. if a player moves to another room, but the door between them is locked, many people would immediately question why it is locked instead of unlocking the door and moving in without a care; therefore, keep the mismatch and alert the *Player* as usual). Use your judgement for what constitutes as minor; if fixing an action causes it to take longer (more actions; isn't a free action, etc.) and the Player is in some sort of Encounter Mode (as determined by the System rules), it cannot be a minor fix. If the fix merely replaces the existing action, or takes up less actions, or the Player is not in any System-defined fixed time mode, then minor fixes are allowed automatically.

Common examples of easy fixes:

- The player goes to open a door that is already open in *Canon*. **Fix:** Skip the open door action and continue with the Action Chain as if it was successful.
- The player says they turn to the left and go through the door, but the door is on the right in *Canon*. **Fix:** Change the Action Chain to turn to the right instead.
- The player shoots at another character, but the safety is on (and the Player would reasonable know, i.e. it's their own gun, or they have experience/skill with firearms); **Fix:** Add the action to disable the safety into the Action Chain and continue.
- 

## Rule: Unexpected Results

An `Unexpected Result` is either an *Unexpected Event* or an *Unexpected Consequence*.

### Unexpected Events

An `Unexpected Event` meets all of the following criteria:

- May only occur after fully resolving an instruction.
- Occurs on the sole decision of the *Game Master*:
    - Some game systems may have special rules for determining such occasions (see `Event Example #1` below).
    - However, the *Game Master* may use GM Fiat to determine an *Unexpected Event* occurs on their own.

Reminder that information the Player cannot know should be kept secret from the player in *World's* narrative response and the final *Game Master* response to the Player.

#### Event Example #1

- Some game systems use a system of Dungeon Turns and Wandering Monsters:
    - The *Game Master*, in keeping track of actions, determines when Dungeon Turns advance, and roll for Wandering Monsters as detailed within the game system rules.
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
