import numpy as np
import matplotlib.pyplot as plt

# DTFT function
def H(z):
    num = np.polyval([1, 0, 1], z**(-1))
    den = np.polyval([0.5, 1], z**(-1))
    H = num / den
    return H

# Input and Output
omega = np.linspace(-3 * np.pi, 3 * np.pi, 100)

# Plotting
plt.plot(omega, abs(H(np.exp(1j * omega))))
plt.xlabel(r'$\omega$')  
plt.ylabel(r'$|H(e^{j\omega})|$') 
plt.grid()
plt.savefig('3_5.png')
