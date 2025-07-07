# Projectile Trajectory Calculator

A Python program that calculates and visualizes the trajectory of a projectile based on initial speed, height, and launch angle.

## Features

- Calculate projectile motion using physics equations
- Generate a table of coordinates for the trajectory
- Create a visual ASCII representation of the trajectory
- Object-oriented design with `Projectile` and `Graph` classes

## Physics

The program uses the following physics principles:
- Gravitational acceleration: 9.81 m/s²
- Projectile motion equations accounting for initial height
- Parabolic trajectory calculation

## Classes

### Projectile
Represents a projectile with:
- **Properties**: speed (m/s), height (m), angle (degrees)
- **Methods**: 
  - Calculate displacement
  - Calculate y-coordinate for any x position
  - Generate all trajectory coordinates

### Graph
Handles visualization of trajectory data:
- **Methods**:
  - Create coordinates table
  - Generate ASCII trajectory visualization

## Usage

```python
# Import and run the calculator
from trajectory_calculator import projectile_helper

# Calculate trajectory with speed=15 m/s, height=5 m, angle=30°
projectile_helper(15, 5, 30)
```

## Sample Output

```
Projectile details:
speed: 15 m/s
height: 5 m
angle: 30°
displacement: 25.4 m

  x      y
  0   5.00
  1   5.45
  2   5.71
  ...

⊣     ∙       
⊣  ∙∙∙ ∙∙∙    
⊣ ∙       ∙   
⊣∙         ∙  
⊣           ∙ 
⊣            ∙
⊣             
 TTTTTTTTTTTTT
```

## File Structure

```
ProjectileTrajectoryCalculator/
├── trajectory_calculator.py    # Main program file
└── README.md                   # This file
```

## Requirements

- Python 3.x
- Standard library modules: `math`

## Installation

1. Clone or download the project files
2. Ensure Python 3.x is installed
3. Run the program:
   ```bash
   python trajectory_calculator.py
   ```

## Customization

You can modify the projectile parameters by changing the values in the `projectile_helper()` function call:

```python
# Example: High-speed, low-angle shot
projectile_helper(speed=25, height=10, angle=15)

# Example: High-angle shot
projectile_helper(speed=12, height=2, angle=60)
```

## Legend

- `∙` - Projectile position
- `⊣` - Y-axis markers
- `T` - X-axis markers

## Author

Created as part of Python programming exercises.