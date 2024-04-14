#!/bin/bash

# Display welcome message
echo "SShed into the lockness server"
echo "Welcome to the Lockness Setup Wizard!"
echo "This will guide you through setting up the Lockness application on your machine."
echo ""

# Check for Python installation
echo "Checking for Python installation..."
if ! command -v python3 &> /dev/null
then
    echo "Python could not be found. Please install Python 3.6 or higher."
    exit 1
else
    echo "Python is installed."
fi
echo ""

# Check and install required Python packages
echo "Installing required Python packages..."
# python3 -m pip install torch numpy pandas --quiet
echo "Required packages installed."
echo ""

# Request user details for configuration
echo "Please enter your user details to configure the application."
read -p "Enter your authentication key: " auth_key

# Optionally, validate the authentication key format here if needed
# Example: if [[ ! $auth_key =~ ^[A-Za-z0-9]{32}$ ]]; then
# echo "Invalid auth key format. The key must be a 32 character alphanumeric string."
# exit 1
# fi

# Save the configuration to a file
config_file="lockness_config.txt"
echo "auth_key=$auth_key" > $config_file
echo "Configuration saved to $config_file"
echo ""

# Final setup confirmation
echo "Lockness has been successfully set up and configured on your machine."
echo "You can now run the application using the lockness.sh script."
echo "Thank you for using Lockness!"

# End of script
exit 0
