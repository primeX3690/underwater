# Deployment Guide - Underwater Defense Grid

## 1. Pre-Deployment Check
- Flash Rust firmware onto edge UUV microcontrollers.
- Verify acoustic modem time synchronization (`time_sync.rs`).

## 2. Ocean Floor Seating & Loitering
- Drop drones along designated maritime boundary coordinates.
- Drones automatically enter passive listening mode (Deep Sleep + Duty Cycling).

## 3. Command Center Monitoring
- Initialize Gateway Buoys on the surface.
- Launch the React Command Center Dashboard (`npm start` inside `command-center/frontend`).



