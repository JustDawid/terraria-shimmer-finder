# Terraria Shimmer Finder

## Overview
This is a lightweight Python tool designed to help Terraria players locate the **Aether Biome** (where the Shimmer liquid is found) without using map viewers or external websites.

The tool calculates the horizontal position of the Aether based on the **Guide's name**, which dictates the specific generation offset in the game code.

## How it Works
Terraria determines the exact location of the Aether based on:
1.  **World Size** (Small, Medium, Large).
2.  **Jungle Side** (Left or Right).
3.  **The Guide's Name** (The first Guide that spawned in the world determines a specific float value offset).

This script reverses that logic to give you the exact compass coordinate.

## Usage

1.  Ensure you have Python installed.
2.  Run the main script:
    ```bash
    python find_shimmer.py
    ```
3.  Follow the on-screen prompts:
    * Enter the **Guide's Name** (Must be the very first name he had upon world creation!).
    * Select **World Size**.
    * Select **Jungle Direction**.

4.  The script will output the distance in feet (Compass) and tiles.

## Files
* `find_shimmer.py` - Main logic and calculator.
* `guide_name.py` - Database of Guide names and their corresponding generation values.

---
*Note: This tool assumes standard seed generation rules.*
