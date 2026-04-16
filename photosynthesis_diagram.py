import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_photosynthesis_diagram():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Set background color
    ax.set_facecolor('#e0f7fa')
    
    # Title
    plt.text(0.5, 0.95, 'Photosynthesis Process', fontsize=30, ha='center', color='#004d40')

    # Sun
    sun = patches.Circle((0.85, 0.8), 0.05, color='#ffeb3b', ec='#fbc02d')
    ax.add_patch(sun)
    plt.text(0.85, 0.8, 'Sunlight', fontsize=14, ha='center', color='black')
    plt.text(0.85, 0.75, 'Provides energy for photosynthesis', fontsize=10, ha='center', color='black')

    # Plant Stem
    plt.plot([0.1, 0.1], [0.3, 0.6], color='#388e3c', linewidth=15)  # Stem
    plt.plot([0.05, 0.15], [0.6, 0.6], color='#388e3c', linewidth=15)  # Branch
    plt.text(0.1, 0.65, 'Plant', fontsize=20, ha='center', color='white')
    
    # Leaves
    leaf1 = patches.Ellipse((0.1, 0.75), 0.15, 0.05, angle=30, color='#4caf50', ec='#388e3c')
    leaf2 = patches.Ellipse((0.1, 0.78), 0.15, 0.05, angle=-30, color='#4caf50', ec='#388e3c')
    ax.add_patch(leaf1)
    ax.add_patch(leaf2)
    
    # Roots
    plt.plot([0.1, 0.05], [0.3, 0.1], color='#8d6e63', linewidth=5)  # Left Root
    plt.plot([0.1, 0.15], [0.3, 0.1], color='#8d6e63', linewidth=5)  # Right Root
    plt.text(0.1, 0.05, 'Absorbs H2O from Soil', fontsize=12, ha='center', color='black')

    # Chloroplasts
    chloroplast = patches.Ellipse((0.1, 0.7), 0.05, 0.02, color='#c5e1a5', ec='#a5d6a7')
    ax.add_patch(chloroplast)
    plt.text(0.1, 0.72, 'Chloroplasts', fontsize=12, ha='center', color='black')
    plt.text(0.1, 0.68, 'Site of Photosynthesis', fontsize=10, ha='center', color='black')

    # Light Reactions Box
    light_reactions = patches.FancyBboxPatch((0.05, 0.25), 0.3, 0.1, boxstyle="round,pad=0.05", color='#ffcc80', ec='#ffb300')
    ax.add_patch(light_reactions)
    plt.text(0.2, 0.3, 'Light Reactions', fontsize=14, ha='center', color='black')
    plt.text(0.2, 0.28, 'Produces O2, NADPH, and ATP', fontsize=10, ha='center', color='black')

    # Calvin Cycle Box
    calvin_cycle = patches.FancyBboxPatch((0.7, 0.25), 0.3, 0.1, boxstyle="round,pad=0.05", color='#81d4fa', ec='#4fc3f7')
    ax.add_patch(calvin_cycle)
    plt.text(0.85, 0.3, 'Calvin Cycle (Dark Reactions)', fontsize=14, ha='center', color='black')
    plt.text(0.85, 0.28, 'Uses CO2, NADPH, and ATP', fontsize=10, ha='center', color='black')

    # Glucose Production
    plt.text(0.85, 0.45, 'Glucose (C6H12O6)', fontsize=16, ha='center', color='black')
    plt.text(0.85, 0.42, 'Energy source for the plant', fontsize=10, ha='center', color='black')

    # Oxygen Release
    plt.text(0.85, 0.55, 'O2 released as waste', fontsize=12, ha='center', color='black')

    # Arrows
    plt.arrow(0.1, 0.75, 0.3, 0, head_width=0.02, head_length=0.05, fc='black', ec='black')  # Energy to Calvin Cycle
    plt.text(0.3, 0.77, 'Energy Transfer', fontsize=10, ha='center', color='black')

    # Final touches
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')  # Turn off the axis

    # Show the plot
    plt.show()

# Call the function to create the diagram
create_photosynthesis_diagram()
