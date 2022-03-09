# ClanAttack

## Installation
### Installing required libraries
```bash
pip install -r requirements.txt
```
### Run the game
```bash
python game.py
```
### Watch a replay
```bash
python replay.py id
```
Where id is a number (0, 1, 2, ...)


## Controls
<kbd>1</kbd><kbd>2</kbd><kbd>3</kbd> - Controls the spawning of barbarians

<kbd>w</kbd><kbd>a</kbd><kbd>s</kbd><kbd>d</kbd> - Controls the king

<kbd>Space</kbd> - King attack

<kbd>r</kbd> - Use rage spell
<kbd>h</kbd> - Use heal spell

<kbd>c</kbd> - Stop the game and save (You have to press <kbd>c</kbd> to save)

## Symbols
`K` - King (1 x 1) (Range = 5)

`!` - Barbarian (1 x 1)

`X` - Spawn Point (1 x 1)

`$` - Townhall grid (4 x 3)

`^` - Hut grid (2 x 2)

`#` - Wall (1 x 1)

`Y` - Cannon (1 x 1) (Range = 9)

## Bonus
- King's Leviathan Axe - Implemented
- Creative feature - Implemented audio for multiple actions, such as
    - King attack
    - Barbarian attack
    - Cannon attack
    - Rage spell
    - Heal spell