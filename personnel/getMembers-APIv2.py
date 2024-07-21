#!/usr/bin/env python3
import argparse
import csv
import re
import requests
import uuid
import xml.etree.ElementTree as ET

# Define the base URL of the DH4 API
BASE_URL = "https://api.team-manager.ca.d4h.com/v2"

def get_members():
    # Define the endpoint for fetching members
    endpoint = f"{BASE_URL}/team/members"

    # Set up the headers with the API key for authentication
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Make a GET request to the API endpoint
    response = requests.get(endpoint, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_json = response.json()

        # Check if 'data' key is present in the response
        if 'data' in response_json:
            members = response_json['data']
            return members
        else:
            raise ValueError("Unexpected response structure: 'data' key not found")
    else:
        # If the request was not successful, raise an error with the status code
        response.raise_for_status()

def get_member_qualifications(member_id):
    # Define the endpoint for fetching member qualifications
    endpoint = f"{BASE_URL}/team/members/{member_id}/qualification-awards?state=current"

    # Set up the headers with the API key for authentication
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Make a GET request to the API endpoint
    response = requests.get(endpoint, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_json = response.json()

        # Check if 'data' key is present in the response
        if 'data' in response_json:
            qualifications = response_json['data']
            return qualifications
        else:
            raise ValueError("Unexpected response structure: 'data' key not found")
    else:
        # If the request was not successful, raise an error with the status code
        response.raise_for_status()

def generate_uuid_from_32bit_int(int_32):
    # Ensure the input is a 32-bit integer
    if not (0 <= int_32 < 2**32):
        raise ValueError("The input must be a 32-bit integer")

    # Convert the 32-bit integer to a 128-bit integer by left-shifting and padding
    int_128 = int_32 << 96

    # Create a UUID using the 128-bit integer
    uuid_str = str(uuid.UUID(int=int_128))

    return uuid_str

def initcap(key):
    return key[0].upper() + key[1:] if key else key

def formatPhone(tel):
    AREA_BOUNDARY = 3           # 800.6288737
    SUBSCRIBER_SPLIT = 6        # 800628.8737

    tel = tel.removeprefix("1")     # remove leading +1, or 1
    tel = re.sub("[ ()-+]", '', tel) # remove space, (), -

    tel = (f"{tel[:AREA_BOUNDARY]}-"
           f"{tel[AREA_BOUNDARY:SUBSCRIBER_SPLIT]}-{tel[SUBSCRIBER_SPLIT:]}")
    return tel

def buildQualifications(member):
    qualifications = [False] * 28
    try:
        for qualification in member:
            qualification_id = qualification['qualification']['id']
            if qualification_id == 4834:
                qualifications[0] = True
            elif qualification_id == 4836:
                qualifications[1] = True
            elif qualification_id == 4838:
                qualifications[2] = True
            elif qualification_id == 4839:
                qualifications[3] = True
            elif qualification_id == 4822:
                qualifications[4] = True
            elif qualification_id == 4827:
                qualifications[5] = True
            elif qualification_id == 4824:
                qualifications[6] = True
            elif qualification_id == -1:
                qualifications[7] = True
            elif qualification_id == -1:
                qualifications[8] = True
            elif qualification_id == -1:
                qualifications[9] = True
            elif qualification_id == 4845:
                qualifications[10] = True
            elif qualification_id == 4846:
                qualifications[11] = True
            elif qualification_id == 4847:
                qualifications[12] = True
            elif qualification_id == 6296:
                qualifications[13] = True
            elif qualification_id == 6297:
                qualifications[14] = True
            elif qualification_id == 4832:
                qualifications[15] = True
            elif qualification_id == 4799:
                qualifications[16] = True
            elif qualification_id == 4798:
                qualifications[17] = True
            elif qualification_id == 4850:
                qualifications[18] = True
            elif qualification_id == 4851:
                qualifications[19] = True
            elif qualification_id == 4852:
                qualifications[20] = True
            elif qualification_id == 4828:
                qualifications[21] = True
            elif qualification_id == 4829:
                qualifications[22] = True
            elif qualification_id == 4830:
                qualifications[23] = True
            elif qualification_id == 4857:
                qualifications[24] = True
            elif qualification_id == 4801:
                qualifications[25] = True
            elif qualification_id == 4788:  # Hoist
                qualifications[26] = True
            elif qualification_id == 4847:  # CFDL
                qualifications[26] = True
            elif qualification_id == 4812:  # K9 Wilderness
                qualifications[27] = True
            elif qualification_id == 4811:  # K9 Tracker
                qualifications[27] = True
    except Exception as e:
        return ""
    return ",".join(map(str, qualifications))

def transform_member(member):
    # Create a new dictionary to hold the transformed member
    transformed_member = {}

    # Copy all fields except 'permission' and 'emergency_contacts'
    for key, value in member.items():
        # Rename 'ref' to 'Callsign'
        if key == 'ref':
            transformed_member['Callsign'] = value
        # Rename 'mobilephone' to 'Phone'
        elif key == 'mobilephone':
            transformed_member['Phone'] = formatPhone(value)
        elif key == 'id':
            transformed_member['D4HID'] = value
            transformed_member['PersonID'] = generate_uuid_from_32bit_int(value)
        elif key == 'name':
            transformed_member['Name'] = value
        elif key == 'email':
            transformed_member['Email'] = value
        elif key == 'address':
            transformed_member['Address'] = value
        elif key.lower() != 'permission' and key != 'emergency_contacts':
            transformed_member[key] = value

    # Extract the first emergency contact, and append to the dict
    if 'emergency_contacts' in member and member['emergency_contacts']:
        first_emg_contact = member['emergency_contacts'][0]
        transformed_member['NOKName'] = first_emg_contact.get('name')
        transformed_member['NOKRelation'] = first_emg_contact.get('relation')
        transformed_member['NOKPhone'] = formatPhone(first_emg_contact.get('phone'))

    if 'Group' not in member:
        transformed_member['Group'] = GROUP

    return transformed_member

def write_members_to_csv(members, filename="members.csv"):
    # Check if members list is not empty
    if members:

        # Get the keys from the first transformed member dictionary
        keys = members[0].keys() if members else []

        # Exclude 'permission' from keys if present
        keys = [key for key in keys if key.lower() != 'permission']

        # Open a file for writing
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=keys)

            # Write the header
            writer.writeheader()

            # Write the member data
            for member in transformed_members:
                writer.writerow(member)
        print(f"Members have been written to {filename}")
    else:
        print("No members to write to CSV")

def escape_xpath_string(value):
    # Handle cases with both single and double quotes
    if "'" in value and '"' in value:
        parts = value.split("'")
        return "concat('" + "', \"'\", '".join(parts) + "')"
    elif "'" in value:
        return f'"{value}"'
    else:
        return f"'{value}'"

def update_qualifications(qualifications_element, qualifications_str):
    qualifications_list = qualifications_str.split(",")
    boolean_elements = qualifications_element.findall("Boolean")

        # Ensure there are exactly 28 boolean elements
    if len(boolean_elements) != 28:
        raise ValueError("The number of Boolean elements in the XML does not match the expected count of 28.")
    for i, boolean_value in enumerate(qualifications_list):
        boolean_elements[i].text = boolean_value.strip()




def update_xml_with_members(members, xml_file="mySARAssistOptions.xml"):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    members_element = root.find(".//AllTeamMembers")

    if members_element is None:
        raise ValueError("No <AllTeamMembers> element found in the XML")

    # Iterate over the members and update/add their information in the Personnel tag
    for member in members:
        # Ensure 'D4HID' field is present

        member_name = member['Name']
        # Escape member name for XPath
        member_name_escaped = escape_xpath_string(member_name)
        member_element = all_team_members.find(f".//Personnel[Name={member_name_escaped}]")

        person_element = all_team_members.find(f".//Personnel[Name={member_name_escaped}]")
        if person_element is None:
          # If the Personnel element does not exist, create a new one
          print("Adding ", member_name, " to Team ", GROUP)
          person_element = ET.SubElement(all_team_members, 'Personnel')
          id_element = ET.SubElement(person_element, 'ID')
          id_element.text = str(generate_uuid_from_32bit_int(member['D4HID']))
          qualifications = ET.SubElement(person_element, 'Qualifications')
          for _ in range(28):
            boolean_element = ET.SubElement(qualifications, "Boolean")
            boolean_element.text = "False"
            for key, value in member.items():
                if key == "Qualifications":
                    qualifications_element = person_element.find("Qualifications")
                    if qualifications_element is not None:
                        update_qualifications(qualifications_element, value)
                else:
                    key_element = person_element.find(key)
                    if key_element is not None:
                        key_element.text = value
        else:
          # If the Personnel element exists, ensure the ID is not updated
          print("Updating ", member_name, " on Team ", GROUP)
          id_element = person_element.find('ID')
          if id_element is None:
            id_element = ET.SubElement(person_element, 'ID')
            id_element.text = str(generate_uuid_from_32bit_int(member['D4HID']))
        # Update or add the fields in the Personnel element
        for key, value in member.items():
          if key.lower() == 'permission' or key == 'ID':
            continue  # Skip the 'permission' and 'ID' fields
          # Rename 'ref' to 'Callsign' and 'mobilephone' to 'Phone'
          if key == 'ref':
            key = 'Callsign'
          elif key == 'mobilephone':
            key = 'Phone'
          elif  key == "Qualifications":
            qualifications_element = person_element.find("Qualifications")
            if qualifications_element is not None:
              update_qualifications(qualifications_element, value)
          else:
            element = person_element.find(key)
            if element is None:
              element = ET.SubElement(person_element, key)
            element.text = str(value)
    # Save the updated XML tree to a file
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)
    print(f"XML file '{xml_file}' has been updated with member information")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process member data and update XML file.' )
    parser.add_argument('-t', '--token', required=True, type=str, help='API key for authentication')
    parser.add_argument('-g', '--group', required=True, type=str, help='Group name to assign to members')
    args = parser.parse_args()

    global API_KEY, GROUP
    API_KEY=args.token
    GROUP=args.group


    try:
      members = get_members()
      transformed_members = [transform_member(member) for member in members]
      print(len(transformed_members))
      for mq in range(len(transformed_members)):
        member_id=transformed_members[mq-1]['D4HID']
        transformed_members[mq-1]['Endorcements']= get_member_qualifications(member_id)
        transformed_members[mq-1]['Qualifications']=buildQualifications(transformed_members[mq-1]['Endorcements'])

      write_members_to_csv(transformed_members, 'members.csv')
      update_xml_with_members('mySARAssistOptions.xml', transformed_members)
    except Exception as e:
      print(f"An error occurred: {e}")

