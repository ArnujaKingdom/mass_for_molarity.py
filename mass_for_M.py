def mass_for_molarity ( molarity, volume_L, molar_mass):
    """ Calculates the mass (grams) needed to prepare a specific molar solution"""  
    mass = molarity*volume_L*molar_mass
   return round(mass,3)
def calculate_dilution(M1=None, V1=None, M1=None, V2=None):
    """Solves M1V1=M2V2 for the missing value."""
   if M1 is None: return f"M1={(M2*V2)/V1:.4f}M"
   if V1 is None: return f"V1={(M2*V2)/M1:.4f}L"
   if M2 is None: return f"M2={(M1*V1)/V2:.4f}M"
   if V2 is None: return f"V2={(M1*V1)/M2:.4f}L"
#Example 1: Preparation of 0.5L of a 2.0M NaCl solution (Molar mass= 58.44g/mol)
required_mass = mass_for_molarity(molarity=2.0, volume_L=0.5, molar_mass=58.44)
print(f"To make the solution, weigh out:{required_mass}g of NaCl")
#Example 2: Dilute a 12  M HCl stock solution to get 1 litre of 2 M HCl.
print ( f"Volume of stock needed: {calculate_dilution(M1=12.0,M2:2.0,V2=1.0)}")
