#!/usr/bin/env python3
"""
Lottery Simulation - Determine how many draws until a specific ticket wins.
Based on the lottery model in Chapter9Classes/lottery.py
"""
import random
from typing import List, Any

def main():
    """Simulate a lottery until our ticket wins, based on the existing lottery model."""
    # Create a list containing 10 numbers and 5 letters (from your original lottery.py)
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
    
    # Define your ticket - 4 random elements
    my_ticket = random.sample(elements, 4)
    
    # Initialize counter
    attempts = 0
    winning_elements = []
    
    print(f"Your ticket: {my_ticket}")
    print(f"Available elements: {elements}")
    print(f"We need to match all 4 elements to win")
    print("Starting simulation...")
    
    # Keep drawing until we win
    while True:
        attempts += 1
        
        # Randomly select 4 elements from the list (same as your original lottery)
        winning_elements = random.sample(elements, 4)
        
        # Check if we won by seeing if all elements in our ticket are in the winning draw
        # This matches the message in your original lottery.py: "Any ticket matching these 4 elements wins"
        if sorted(my_ticket) == sorted(winning_elements):
            break
        
        # Optional: Show progress periodically
        if attempts % 100_000 == 0:
            print(f"Still trying after {attempts:,} attempts...")
    
    # Report results
    print(f"\nYou won after {attempts:,} attempts!")
    print(f"Your ticket: {my_ticket}")
    print(f"Winning draw: {winning_elements}")

if __name__ == "__main__":
    main()