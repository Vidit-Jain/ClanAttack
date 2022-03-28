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
<kbd>j</kbd> <kbd>k</kbd> Choose character to play (Vim style).

<kbd>Enter</kbd> To select the character

<kbd>1</kbd><kbd>2</kbd><kbd>3</kbd> - Controls the spawning of barbarians

<kbd>4</kbd><kbd>5</kbd><kbd>6</kbd> - Controls the spawning of archers

<kbd>7</kbd><kbd>8</kbd><kbd>9</kbd> - Controls the spawning of balloons 

<kbd>w</kbd><kbd>a</kbd><kbd>s</kbd><kbd>d</kbd> - Controls the player 

<kbd>Space</kbd> - Player attack
<kbd>x</kbd> - Ultimate attack (Queen only)

<kbd>r</kbd> - Use rage spell
<kbd>h</kbd> - Use heal spell
 
<kbd>p</kbd> - To proceed to next level (For testing / evaluation)

<kbd>c</kbd> - Stop the game and save (You have to press <kbd>c</kbd> to save)

## Symbols
`K` - King (1 x 1) (Range = 5)

`Q` - Queen (1 x 1) (Range = 8)

`!` - Barbarian (1 x 1) 

`>` - Archer (1 x 1) (Range = 8)

`B` - Balloon (1 x 1) 

`X` - Spawn Point (1 x 1)

`$` - Townhall grid (4 x 3)

`^` - Hut grid (2 x 2)

`#` - Wall (1 x 1)

`Y` - Cannon (1 x 1) (Range = 7)

`W` - Wizard (1 x 1) (Range = 7)


## Bonus
### Assignment 1
- King's Leviathan Axe - Implemented
- Creative feature - Implemented audio for multiple actions, such as
    - King, Queen attack
    - Barbarian, Archer, Balloon attack
    - Cannon, Wizard tower attack
    - Rage, Heal spell

### Assignment 2
- Archer Queen's Eagle Arrow - Implemented
