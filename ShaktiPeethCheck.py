"""
@file ShaktiPeethCheck.py
@author Gandla Bhargavi 
@brief Check whether a given temple is in the sample list of Shakti Peethams.

Input  : Temple name (string)
Output : "Yes — it is a Shakti Peetham" or "No — it is not a Shakti Peetham"

Note: This program uses a sample list. Add more names to the list 'shakti_list'
if you want a larger database.

@date 2025-11-21
"""

# Normalize function: lowercase + remove extra spaces
def normalize(text: str) -> str:
    text = text.lower().strip()
    
    cleaned = []
    space_flag = False
    
    for ch in text:
        if ch.isspace():
            if not space_flag:
                cleaned.append(" ")
            space_flag = True
        else:
            cleaned.append(ch)
            space_flag = False

    return "".join(cleaned)


def main():
    # Sample Shakti Peetham list
    shakti_list_raw = [
        "kamakhya", "kalighat", "tarapith", "vishalakshi", "vadodara",
        "majuli", "trikuti", "jai shree", "ambika", "mahakali"
    ]

    # Normalize list
    shakti_list = [normalize(name) for name in shakti_list_raw]

    # User input
    temple_name = input("Enter temple name to search: ")
    key = normalize(temple_name)

    found = key in shakti_list

    print("\nDate: 21-11-2025")
    if found:
        print(f'Yes — "{temple_name}" is in the (sample) Shakti Peetham list.')
    else:
        print(f'No — "{temple_name}" is not in the (sample) Shakti Peetham list.')

    print("\nNote: Add more names in 'shakti_list_raw' for a complete database.")


if __name__ == "__main__":
    main()