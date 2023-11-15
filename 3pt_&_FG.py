import matplotlib.pyplot as plt
# Data for Eastern Kentucky
eastern_kentucky_fg = 47
eastern_kentucky_fga = 81
eastern_kentucky_3pt = 11
eastern_kentucky_3pta = 33
# Data for Wilberforce
wilberforce_fg = 29
wilberforce_fga = 76
wilberforce_3pt = 3
wilberforce_3pta = 21
# Calculate percentages
eastern_kentucky_fg_percentage = eastern_kentucky_fg / eastern_kentucky_fga * 100
eastern_kentucky_3pt_percentage = eastern_kentucky_3pt / eastern_kentucky_3pta * 100
wilberforce_fg_percentage = wilberforce_fg / wilberforce_fga * 100
wilberforce_3pt_percentage = wilberforce_3pt / wilberforce_3pta * 100
# Create the graph
fig, ax = plt.subplots()
# Set the labels
ax.set_xlabel("Team")
ax.set_ylabel("Percentage")
ax.set_title("Field Goal and 3-Point Percentages")
# Set the bars
ax.bar(["Eastern Kentucky", "Wilberforce"], [eastern_kentucky_fg_percentage, wilberforce_fg_percentage], label="Field Goal Percentage")
ax.bar(["Eastern Kentucky", "Wilberforce"], [eastern_kentucky_3pt_percentage, wilberforce_3pt_percentage], label="3-Point Percentage")
# Set the colors
eastern_kentucky_color = "#800000"  # Maroon
eastern_kentucky_3pt_color = "#000000"  # Black
wilberforce_color = "#FFFF00"  # Yellow
wilberforce_3pt_color = "#002D72"  # Blue
# Set the bars with custom colors
ax.bar(["Eastern Kentucky", "Wilberforce"], [eastern_kentucky_fg_percentage, wilberforce_fg_percentage], label="Field Goal Percentage", color=[eastern_kentucky_color, wilberforce_color])
ax.bar(["Eastern Kentucky", "Wilberforce"], [eastern_kentucky_3pt_percentage, wilberforce_3pt_percentage], label="3-Point Percentage", color=[eastern_kentucky_3pt_color, wilberforce_3pt_color])

# Add a legend
ax.legend()
ax.legend(loc='center right', bbox_to_anchor=(1.13, 0.5))

# Show the graph
plt.show()