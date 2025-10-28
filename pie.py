import matplotlib.pyplot as plt

# Data
labels = ['Tested Risks', 'Untested Risks']
sizes = [85.7, 14.3]
explode = (0.05, 0)  # Slightly pull out the first slice

# Create the pie chart
plt.figure(figsize=(6,6))
plt.pie(
    sizes,
    explode=explode,
    labels=labels,
    autopct='%1.1f%%',
    shadow=True,
    startangle=140,
)
plt.title('Risk Coverage Analysis', fontsize=14)
plt.axis('equal')
plt.savefig('risk_coverage.png')
plt.show()
