import matplotlib.pyplot as plt

# Setting dimensions for each part of the road
total_road_width = .66  # Total width of the road, including all parts
border_width = total_road_width * 0.2  # 20% of the total width
lane_width = total_road_width * 0.3  # 30% of the total width
center_line_width = total_road_width * 0.1  # 20% of the total width

# Calculating radii for each part
outer_border_radius = 2  # Half the diameter
inner_border_radius = outer_border_radius - border_width
outer_lane_radius = inner_border_radius - lane_width
center_line_radius = outer_lane_radius - lane_width
inner_lane_radius = center_line_radius - center_line_width

# Creating the plot
# Adjusting the design to position the dashed line exactly between the two borders

# Redefining the plot
fig, ax = plt.subplots(figsize=(12, 12))
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('#333333')


# Calculating radii for each part
outer_border_radius = .99  # Half the diameter
inner_border_radius = outer_border_radius - border_width - lane_width
center_line_radius = (outer_border_radius + inner_border_radius) / 2  # Centered between the two borders

# Creating the outer border
outer_border = plt.Circle((0, 0), outer_border_radius, color='white', fill=False, linewidth=border_width * 100)
ax.add_artist(outer_border)

# Creating the inner border
inner_border = plt.Circle((0, 0), inner_border_radius, color='white', fill=False, linewidth=border_width * 100)
ax.add_artist(inner_border)

# Creating the lanes
outer_lane = plt.Circle((0, 0), outer_border_radius - border_width / 1, color='#333333', fill=False, linewidth=lane_width * 100)
inner_lane = plt.Circle((0, 0), inner_border_radius + border_width / 1, color='#333333', fill=False, linewidth=lane_width * 100)
ax.add_artist(outer_lane)
ax.add_artist(inner_lane)

# Creating the center dashed line
center_line = plt.Circle((0, 0), center_line_radius, color='white', fill=False, linewidth=center_line_width * 100, linestyle=(0, (5.55, 5.75)))
ax.add_artist(center_line)

# Remove padding and margins
plt.tight_layout(pad=0)
ax.margins(0)
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)


# Saving the image in different resolutions
plt.savefig('logo_dark.jpg', dpi=1000)  # 8K resolution

plt.show()
