def split_before_uppercases(formula):
    upper_index = []
    new_formula = []
    
    # find the index of the upper letters
    for i in range(len(formula)):
      if formula[i].isupper():
        upper_index.append(i)

    # slices
    if upper_index:
      for i in range(len(upper_index) - 1):
        new_word = formula[upper_index[i]:upper_index[i+1]]
        new_formula.append(new_word)

      # add the last one
      last_upper = upper_index[len(upper_index) - 1]
      new_word = formula[last_upper:]
      new_formula.append(new_word)
    elif formula:
      new_formula.append(formula)
    return new_formula

def split_at_digit(formula):
  count = 0
  for l in formula:
    count += 1
    if l.isdigit():
      letters = formula[:count - 1]
      digits = formula[count - 1:]
      return letters, int(digits)
  return formula, 1

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.  
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    atom_counts = {}

    for atom in split_by_capitals(molecular_formula):
        atom_name, atom_count = split_at_number(atom)
        
        # Step 2: Update the dictionary with the atom name and count
        atom_counts[atom_name] = atom_count

    # Step 3: Return the completed dictionary
    return atom_counts



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
