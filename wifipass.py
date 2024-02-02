import subprocess

try:
    # Run the command to retrieve Wi-Fi profiles and passwords
    command_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8')
    profile_names = [line.split(':')[1].strip() for line in command_output.split('\n') if "All User Profile" in line]

    # Iterate over each Wi-Fi profile and retrieve the password
    for profile_name in profile_names:
        try:
            # Use 'findstr' to get the key content line directly, avoids multiple iterations
            profile_output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear']).decode('utf-8')
            password_line = [line.split(':')[1].strip() for line in profile_output.split('\n') if "Key Content" in line]

            if password_line:
                password = password_line[0]
                print(f'\nWi-Fi Profile: {profile_name}\nPassword: {password}')
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving password for profile '{profile_name}': {e}")
except subprocess.CalledProcessError as e:
    print(f"\nError retrieving Wi-Fi profiles: {e}")
else:
    print("\nWi-Fi passwords retrieved successfully.")
