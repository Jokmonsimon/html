import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Define figure and axis
fig, ax = plt.subplots(figsize=(14, 10))

# Draw the boxes for each section (Environment, IS Research, Knowledge Base)
# Environment box
env_box = mpatches.FancyBboxPatch((0.05, 0.6), 0.25, 0.3, boxstyle="round,pad=0.05", 
                                  edgecolor="black", facecolor="#d9ead3")
ax.add_patch(env_box)
ax.text(0.175, 0.87, "Environment\n(Relevance)", ha="center", va="center", 
        fontsize=14, fontweight="bold")

# List elements inside Environment box
ax.text(0.175, 0.82, "• People\n• Organizations\n• Technology", ha="center", va="center", fontsize=12)

# IS Research box
is_research_box = mpatches.FancyBboxPatch((0.35, 0.3), 0.3, 0.6, boxstyle="round,pad=0.05", 
                                          edgecolor="black", facecolor="#cfe2f3")
ax.add_patch(is_research_box)
ax.text(0.5, 0.85, "IS Research", ha="center", va="center", fontsize=14, fontweight="bold")

# Develop/Build and Justify/Evaluate inside IS Research
ax.text(0.5, 0.7, "Develop/Build:\n• Theories\n• Artifacts", ha="center", va="center", fontsize=12)
ax.text(0.5, 0.5, "Justify/Evaluate:\n• Analytical\n• Case Study\n• Experimental\n• Field Study\n• Simulation",
        ha="center", va="center", fontsize=12)

# Knowledge Base box
kb_box = mpatches.FancyBboxPatch((0.7, 0.6), 0.25, 0.3, boxstyle="round,pad=0.05", 
                                 edgecolor="black", facecolor="#f4cccc")
ax.add_patch(kb_box)
ax.text(0.825, 0.87, "Knowledge Base\n(Rigor)", ha="center", va="center", 
        fontsize=14, fontweight="bold")

# List elements inside Knowledge Base box
ax.text(0.825, 0.82, "• Foundations\n• Methodologies", ha="center", va="center", fontsize=12)

# Adding arrows for flow and relationships
# Arrows from Environment to IS Research
ax.arrow(0.3, 0.75, 0.05, 0, head_width=0.02, head_length=0.02, fc='black', ec='black')
ax.text(0.32, 0.77, "Business Needs", ha="center", fontsize=10)

# Arrows from IS Research to Environment (application in appropriate environment)
ax.arrow(0.3, 0.45, -0.05, 0, head_width=0.02, head_length=0.02, fc='black', ec='black')
ax.text(0.23, 0.43, "Application in\nAppropriate\nEnvironment", ha="center", fontsize=10)

# Arrow from Knowledge Base to IS Research (Applicable Knowledge)
ax.arrow(0.7, 0.75, -0.05, 0, head_width=0.02, head_length=0.02, fc='black', ec='black')
ax.text(0.68, 0.77, "Applicable\nKnowledge", ha="center", fontsize=10)

# Arrow from IS Research to Knowledge Base (Additions to Knowledge Base)
ax.arrow(0.65, 0.45, 0.05, 0, head_width=0.02, head_length=0.02, fc='black', ec='black')
ax.text(0.72, 0.43, "Additions to\nKnowledge Base", ha="center", fontsize=10)

# Clean up plot area
ax.axis("off")

plt.show()
