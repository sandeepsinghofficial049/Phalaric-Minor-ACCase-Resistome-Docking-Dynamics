
import sys
import numpy as np
from Bio.PDB import PDBParser
import warnings
from Bio import BiopythonWarning

warnings.simplefilter('ignore', BiopythonWarning)

def calculate_3k8x_center(pdb_file, target_residues):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('protein', pdb_file)
    coords = []
    for model in structure:
        for chain in model:
            for residue in chain:
                if residue.id[1] in target_residues:
                    for atom in residue:
                        coords.append(atom.get_coord())
    if not coords:
        return None
    return np.mean(np.array(coords), axis=0)

def calculate_1uyr_center(pdbqt_file):
    x_coords, y_coords, z_coords = [], [], []
    with open(pdbqt_file, "r") as f:
        for line in f:
            if line.startswith("ATOM") or line.startswith("HETATM"):
                x_coords.append(float(line[30:38]))
                y_coords.append(float(line[38:46]))
                z_coords.append(float(line[46:54]))
    if not x_coords:
        return None
    return [np.mean(x_coords), np.mean(y_coords), np.mean(z_coords)]

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit(1)
    rec_name = sys.argv[1]
    
    if "3k8x" in rec_name:
        pocket_residues = [65, 68, 84, 86, 117, 118]
        center = calculate_3k8x_center(f"{rec_name}_clean.pdb", pocket_residues)
    else:
        center = calculate_1uyr_center("WT_1uyr_clean.pdbqt")
        
    if center is not None:
        print(f"center_x = {center[0]:.3f}\ncenter_y = {center[1]:.3f}\ncenter_z = {center[2]:.3f}")
    else:
        print("ERROR")
