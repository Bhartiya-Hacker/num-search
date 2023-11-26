import asyncio
from truecallerpy import search_phonenumber

# Enter Your country code and installation ID:

COUNTRY_CODE = "YOUR_COUNTRY_CODE"
INSTALLATION_ID = "YOUR_INSTALLATION_ID"

# Fetching Data:

async def get_truecaller_info(phone_number):
    try:
        # Perform the phone number search
        response = await search_phonenumber(phone_number, COUNTRY_CODE, INSTALLATION_ID)

        # Extract and store specific information, including an image URL
        if response.get("status_code") == 200:
            data = response.get("data", {}).get("data", [])[0]
            if data:
                user_id = data.get("id")
                name = data.get("name")
                alt_name = data.get("altName")
                gender = data.get("gender")

                phone_info = data.get("phones", [])[0] if data.get("phones") else {}
                e164_format = phone_info.get("e164Format")
                number_type = phone_info.get("numberType")
                national_format = phone_info.get("nationalFormat")
                dialing_code = phone_info.get("dialingCode")
                country_code = phone_info.get("countryCode")
                carrier = phone_info.get("carrier")
                open_phone = phone_info.get("type")

                address_info = data.get("addresses", [])[0] if data.get("addresses") else {}
                address = address_info.get("address")
                city = address_info.get("city")
                country_code_address = address_info.get("countryCode")

                image_url = data.get("image", "Not available")

                # Store the information in a text file

                filename = f"{phone_number}.txt"
                with open(filename, "w") as file:
                    file.write(f"User ID: {user_id}\n")
                    file.write(f"Name: {name}\n")
                    file.write(f"Alt Name: {alt_name}\n")
                    file.write(f"Gender: {gender}\n")
                    file.write(f"Phone Information:\n")
                    file.write(f"- E164 Format: {e164_format}\n")
                    file.write(f"- Number Type: {number_type}\n")
                    file.write(f"- National Format: {national_format}\n")
                    file.write(f"- Dialing Code: {dialing_code}\n")
                    file.write(f"- Country Code: {country_code}\n")
                    file.write(f"- Carrier: {carrier}\n")
                    file.write(f"- Open Phone: {open_phone}\n")
                    file.write(f"Address Information:\n")
                    file.write(f"- Address: {address}\n")
                    file.write(f"- City: {city}\n")
                    file.write(f"- Country Code (Address): {country_code_address}\n")
                    file.write(f"Image URL: {image_url}\n")

                print(f"Truecaller information saved to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    # Prompt the user to enter a phone number

    phone_number_input = input("Enter the phone number: ")

    # Create an event loop and run the asynchronous function
    
    asyncio.run(get_truecaller_info(phone_number_input))
