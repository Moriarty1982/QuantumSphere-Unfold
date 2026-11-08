"""Evaluate the full double-pulse pointer for the four sign pairs."""
from cmath import exp
from math import cos, pi, sin, sqrt


def evolve(state, coupling, detuning, time):
    left, right = state
    half = detuning / 2
    rate = sqrt(coupling**2 + half**2)
    diagonal = cos(rate * time)
    off = -1j * sin(rate * time) / rate
    mean_phase = exp(-1j * half * time)
    return (
        mean_phase * (diagonal * left + off * (half * -left + coupling * right)),
        mean_phase * (diagonal * right + off * (coupling * left + half * right)),
    )


def pointer(n, r, a, b, step=5):
    strength = step * (a + b)
    detuning = 2 * step * (a * n - b * r)
    pulse = pi / (2 * sqrt(2) * strength)
    wait = pi * (1 - 1 / sqrt(2)) / strength
    state = evolve((1, 0), strength, detuning, pulse)
    left, right = evolve(state, -strength, detuning, pulse)
    state = (left, right * exp(-1j * detuning * wait))
    state = evolve(state, strength, detuning, pulse)
    left, right = evolve(state, -strength, detuning, pulse)
    return (abs(1 - left)**2 + abs(right)**2) / 4, abs(right)**2


if __name__ == "__main__":
    for a, b in ((1, 1), (1, 23)):
        for n, r in ((1, -1), (-1, 1), (1, 1), (-1, -1)):
            accept, leakage = pointer(n, r, a, b)
            print(f"{a}:{b}, ({n:+},{r:+}): accept={accept:.6f}, active leakage={leakage:.6f}")
