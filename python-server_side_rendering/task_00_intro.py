#!/usr/bin/python3

def generate_invitations(template, attendees):
    """
    function to generate invitations
    """
    if not isinstance(template, str):
        print("Template is empty, no output files generated.")
        return
    
    if not isinstance(attendees, list):
        print("No data provided, no output files generated.")
        return
    
    for part in attendees:
        if not isinstance(part, dict):
            return
        
    if template == "":
        print("template is empty")
        return
    
    i = 0

    for attendee in attendees:
        data = {
            "name": attendee.get("name", "N/A"),
            "event_title": attendee.get("event_title", "N/A"),
            "event_date": attendee.get("event_date", "N/A"),
            "event_location": attendee.get("event_location", "N/A")
        }

        invitation = template.format(**data)

        filename = f"output_{i + 1}.txt"
        i = i+1

        with open(filename, 'w') as file:
            file.write(invitation)
        
        print(f"Generated: {filename}")
