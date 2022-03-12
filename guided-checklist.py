#! python3
# Auto-guided Checklist 

# Put all of the steps in a list:
steps = ["Open the page", "Check for spelling errors", "Check for broken links", "Run unit tests", "Add to sitemap", "Check sitemap for the new URL"]

# Loop through each step in the list 
for step in steps:
    # Print out the instructions
    # print(step)
    
    # Pause until we finish the step and hit "Enter" to get the next step
    input(step)