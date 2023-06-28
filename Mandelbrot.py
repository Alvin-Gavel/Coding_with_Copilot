"""
This is an experiment in using GitHub Copilot, by testing how quickly I can
make a module that prints out the Mandelbrot set, using spaces to denote
those points in the complex plane that do not converge, asterisks to
denote those that seem to converge, but periods for points that were only
shown to diverge in the last 50% of the iterations.
"""
import numpy as np

def iterate(real_steps, imag_steps, maxiter):
    min_real = -2.0
    max_real = 0.5
    min_imag = -1.2
    max_imag = 1.2

    real = np.linspace(min_real, max_real, real_steps)
    imag = np.linspace(min_imag, max_imag, imag_steps)

    c = real + 1j * imag[:, np.newaxis]
    z = c

    turns_to_diverge = np.zeros(c.shape, dtype=int)
    for i in range(maxiter):
        z = z**2 + c
        diverged = np.abs(z) > 2
        turns_to_diverge[diverged & (turns_to_diverge == 0)] = i
    return turns_to_diverge


def print_mandelbrot(real_steps, imag_steps, maxiter):
    turns_to_diverge = iterate(real_steps, imag_steps, maxiter)
    for row in turns_to_diverge:
        for z in row:
            if z == 0:
                print("*", end="")
            elif z < maxiter / 2:
                print(" ", end="")
            else:
                print(".", end="")
        print()
    return