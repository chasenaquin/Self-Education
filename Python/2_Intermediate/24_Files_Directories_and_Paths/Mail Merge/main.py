PLACEHOLDER = "[name]"

# Make a list of names.
with open("recipients.txt", mode="r") as recipients_file:
    recipients = recipients_file.readlines()


with open("mail_template.txt", mode="r") as mail_template:
    # Read in the letter
    content = mail_template.read()
    for recipient in recipients:
        # Strip the new line
        stripped_name = recipient.strip()
        # Replacing the name variable with names from the list
        new_letter = content.replace(PLACEHOLDER, stripped_name)
        # Create new letters named for each person.
        with open(f"Output Mail/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)







