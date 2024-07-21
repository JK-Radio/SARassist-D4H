#!/usr/bin/env python3
import argparse
import csv
import re
import requests
import uuid
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

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

    isGSAR=False
    isGSTL=False
    isSARM1=False
    isSARM2=False
    isFA7=False
    isFA40=False
    isFA70=False
    isFABLS=False
    isFAALS=False
    isFR=False
    isSWOP=False
    isSWTCH=False
    isSWADV=False
    isROPE1=False
    isROPE2=False
    isROPETL=False
    isOARTM=False
    isOARTL=False
    isTRACKA=False
    isTRACKER=False
    isTRACKADV=False
    isMTN1=False
    isMTN2=False
    isMTN3=False
    isORV=False
    isPCOP=False
    isAIRT=False
    isK9=False
    try:
        for qualification in member:
          if qualification['qualification']['id'] == 4834:
            isGSAR=True
          elif qualification['qualification']['id'] == 4836:
            isGSTL=True
          elif qualification['qualification']['id'] == 4838:
            isSARM1=True
          elif qualification['qualification']['id'] == 4839:
            isSARM2=True
          elif qualification['qualification']['id'] == 4822:
            isFA7=True
          elif qualification['qualification']['id'] == 4827:
            isFA40=True
          elif qualification['qualification']['id'] == 4824:
            isFA70=True
          elif qualification['qualification']['id'] == -1:
            isFABLS=True
          elif qualification['qualification']['id'] == -1:
            isFAALS=True
          elif qualification['qualification']['id'] == -1:
            isFR=True
          elif qualification['qualification']['id'] == 4845:
            isSWOP=True
          elif qualification['qualification']['id'] == 4846:
            isSWTCH=True
          elif qualification['qualification']['id'] == 4847:
            isSWADV=True
          elif qualification['qualification']['id'] == 6296:
            isROPE1=True
          elif qualification['qualification']['id'] == 6297:
            isROPE2=True
          elif qualification['qualification']['id'] == 4832:
            isROPETL=True
          elif qualification['qualification']['id'] == 4799:
            isOARTM=True
          elif qualification['qualification']['id'] == 4798:
            isOARTL=True
          elif qualification['qualification']['id'] == 4850:
            isTRACKA=True
          elif qualification['qualification']['id'] == 4851:
            isTRACKER=True
          elif qualification['qualification']['id'] == 4852:
            isTRACKADV=True
          elif qualification['qualification']['id'] == 4828:
            isMTN1=True
          elif qualification['qualification']['id'] == 4829:
            isMTN2=True
          elif qualification['qualification']['id'] == 4830:
            isMTN3=True
          elif qualification['qualification']['id'] == 4857:
            isORV=True
          elif qualification['qualification']['id'] == 4801:
            isPCOP=True
          elif qualification['qualification']['id'] == 4788:  #Hoist
            isAIRT=True
          elif qualification['qualification']['id'] == 4847:  #CFDL
            isAIRT=True
          elif qualification['qualification']['id'] == 4812:  #K9 Wilderness
            isK9=True
          elif qualification['qualification']['id'] == 4811:  #K9 Tracker
            isK9=True
    except Exception as e:
      return "False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False"
    return f"{isGSAR},{isGSTL},{isSARM1},{isSARM2},{isFA7},{isFA40},{isFA70},{isFABLS},{isFAALS},{isFR},{isSWOP},{isSWTCH},{isSWADV},{isROPE1},{isROPE2},{isROPETL},{isOARTM},{isOARTL},{isTRACKA},{isTRACKER},{isTRACKADV},{isMTN1},{isMTN2},{isMTN3},{isORV},{isPCOP},{isAIRT},{isK9}"

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

def update_xml_with_members(xml_filename, members):
    # Parse the existing XML file
    tree = ET.parse(xml_filename)
    root = tree.getroot()
    
    # Navigate to the AllTeamMembers subtree
    all_team_members = root.find(".//AllTeamMembers")
    if all_team_members is None:
        raise ValueError("AllTeamMembers subtree not found in the XML")

    # Iterate over the members and update/add their information in the Personnel tag
    for member in members:
        # Ensure 'D4HID' field is present
        if 'D4HID' not in member:
            print(f"Skipping member with missing 'D4HID' field: {member}")
            continue
        
        member_name = member['Name']
        
        # Escape member name for XPath
        member_name_escaped = escape_xpath_string(member_name)
        member_element = all_team_members.find(f".//Personnel[Name={member_name_escaped}]")
        
        if member_element is None:
            # If the Personnel element does not exist, create a new one
            print("Adding ", member_name, " to Team ", GROUP) 
            member_element = ET.SubElement(all_team_members, 'Personnel')
            id_element = ET.SubElement(member_element, 'ID')
            id_element.text = str(generate_uuid_from_32bit_int(member['D4HID']))
            qualifications = ET.SubElement(member_element, 'Qualifications')
            for _ in range(28):
              boolean_element = ET.SubElement(qualifications, "Boolean")
              boolean_element.text = "False"
        else:
            # If the Personnel element exists, ensure the ID is not updated
            print("Updating ", member_name, " on Team ", GROUP)
            id_element = member_element.find('ID')
            if id_element is None:
                id_element = ET.SubElement(member_element, 'ID')
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
                
            element = member_element.find(key)
            if element is None:
                element = ET.SubElement(member_element, key)
            element.text = str(value)
    
    # Save the updated XML tree to a file
    tree.write(xml_filename)
    print(f"XML file '{xml_filename}' has been updated with member information.")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Process member data and update XML file.' )
    parser.add_argument('-t', '--token', required=True, type=str, help='API key for authentication')
    parser.add_argument('-g', '--group', required=True, type=str, help='Group name to assign to members')
    args = parser.parse_args()
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

