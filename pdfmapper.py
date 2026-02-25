def map_skills_to_pdf(agent_skills):
    """
    agent_skills: Dictionary from your profession/bonus logic 
    e.g., {"Accounting": 50, "Craft (Electrician)": 30}
    """
    pdf_data = {}
    
    # Static mapping for skills with weird base values in field IDs
    SKILL_FIELD_MAP = {
        "Accounting": "Accounting 10", "Alertness": "Alertness 20",
        "Athletics": "Athletics 30", "Bureaucracy": "Bureaucracy 10",
        "Criminology": "Criminology 10", "Dodge": "Dodge 30",
        "Drive": "Drive 20", "Firearms": "Firearms 20",
        "First Aid": "First Aid 10", "History": "History 10",
        "HUMINT": "HUMINT 10", "Melee Weapons": "Melee Weapons 30",
        "Navigate": "Navigate 10", "Occult": "Occult 10",
        "Persuade": "20", "Psychotherapy": "10",
        "Search": "20", "Stealth": "10", "Survival": "10",
        "Swim": "20", "Unarmed Combat": "40"
    }

    for skill, value in agent_skills.items():
        # Handle specialized skills like "Craft (Electrician)"
        if "(" in skill:
            base_skill = skill.split(" (")[0] # e.g., "Craft"
            specialty = skill.split("(")[1].replace(")", "") # e.g., "Electrician"
            
            pdf_data[base_skill] = specialty # Sets the label text
            pdf_data[f"{base_skill} 0"] = value # Sets the numeric score
            
        elif "Foreign Language" in skill:
            # You'll need a counter to fill 'Foreign Languages and Other Skills 1', etc.
            pass 
            
        elif skill in SKILL_FIELD_MAP:
            field_id = SKILL_FIELD_MAP[skill]
            full_id = field_id if " " in field_id else f"{skill} {field_id}"
            pdf_data[full_id] = value
            
    return pdf_data